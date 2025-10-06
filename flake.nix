{
	inputs = {
		nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
		hooks = {
			url = "github:cachix/git-hooks.nix";
			inputs.nixpkgs.follows = "nixpkgs";
		};

		uv = {
			url = "github:pyproject-nix/uv2nix";
			inputs = {
				nixpkgs.follows = "nixpkgs";
				pyproject-nix.follows = "pyproject";
			};
		};

		build-systems = {
			url = "github:pyproject-nix/build-system-pkgs";
			inputs = {
				uv2nix.follows = "uv";
				nixpkgs.follows = "nixpkgs";
				pyproject-nix.follows = "pyproject";
			};
		};

		pyproject = {
			url = "github:pyproject-nix/pyproject.nix";
			inputs.nixpkgs.follows = "nixpkgs";
		};
	};

	outputs = {
		uv,
		self,
		hooks,
		nixpkgs,
		pyproject,
		build-systems,
		...
	}: let
		inherit (nixpkgs) lib;

		getPythonVersion = let
			val = builtins.getEnv "PYTHON_VERSION";
			result =
				if val == ""
				then "3.13"
				else val;
		in
			builtins.replaceStrings ["."] [""] result;

		workspace = uv.lib.workspace.loadWorkspace {workspaceRoot = ./.;};
		overlay = workspace.mkPyprojectOverlay {sourcePreference = "wheel";};

		forAllSystems = f:
			lib.genAttrs [
				"x86_64-linux"
				"aarch64-linux"
				"x86_64-darwin"
				"aarch64-darwin"
			] (system:
					f rec {
						inherit system;

						pkgs = nixpkgs.legacyPackages.${system};
						python = pkgs."python${getPythonVersion}";

						pythonSet =
							(pkgs.callPackage pyproject.build.packages {inherit python;}).overrideScope (
								lib.composeManyExtensions [
									build-systems.overlays.default
									overlay
								]
							);
					});
	in {
		devShells =
			forAllSystems ({
					pkgs,
					system,
					python,
					pythonSet,
					...
				}: let
					check = self.checks.${system}.pre-commit-check;
				in {
					default = let
						editableOverlay =
							workspace.mkEditablePyprojectOverlay {
								root = "$REPO_ROOT";
							};

						editablePythonSet =
							pythonSet.overrideScope (
								lib.composeManyExtensions [
									editableOverlay

									(final: prev: {
											proselint =
												prev.proselint.overrideAttrs (old: {
														nativeBuildInputs =
															old.nativeBuildInputs
															++ final.resolveBuildSystem {
																editables = [];
															};
													});
										})
								]
							);

						virtualenv = editablePythonSet.mkVirtualEnv "proselint-env" {proselint = ["test" "dev"];};
					in
						pkgs.mkShell {
							buildInputs = check.enabledPackages;

							packages = [
								virtualenv
								pkgs.nodePackages_latest.prettier
								pkgs.git-cliff
								pkgs.typos
								pkgs.uv
							];

							env = {
								UV_NO_SYNC = "1";
								UV_PYTHON = python.interpreter;
								UV_PYTHON_DOWNLOADS = "never";
							};

							shellHook =
								''
									export REPO_ROOT=$(git rev-parse --show-toplevel)
									unset PYTHONPATH
								''
								+ check.shellHook;
						};
				});

		packages =
			forAllSystems ({pythonSet, ...}: {
					default = pythonSet.mkVirtualEnv "proselint-env" workspace.deps.default;

					wheel =
						pythonSet.proselint.override {
							pyprojectHook = pythonSet.pyprojectDistHook;
						};

					sdist =
						(pythonSet.proselint.override {
								pyprojectHook = pythonSet.pyprojectDistHook;
							}).overrideAttrs (old: {
								env.uvBuildType = "sdist";
							});
				});

		apps =
			forAllSystems ({system, ...}: {
					default = {
						type = "app";
						program = "${self.packages.${system}.default}/bin/proselint";
					};
				});

		checks =
			forAllSystems ({
					system,
					pkgs,
					...
				}: {
					pre-commit-check =
						hooks.lib.${system}.run {
							src = ./.;
							hooks = {
								trim-trailing-whitespace.enable = true;
								end-of-file-fixer.enable = true;
								mixed-line-endings.enable = true;
								markdownlint.enable = true;
								ruff.enable = true;
								pyright = let
									pyright = pkgs.basedpyright;
								in {
									enable = true;
									package = pyright;
									entry = "${pyright}/bin/basedpyright";
								};
								convco.enable = true;
								alejandra.enable = true;
								statix = {
									enable = true;
									settings.ignore = ["/.direnv"];
								};
							};
						};
				});
	};
}
