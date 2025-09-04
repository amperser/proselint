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
				then "3.12"
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
					...
				}: let
					check = self.checks.${system}.pre-commit-check;
				in {
					# note: impure, editable overlays in uv2nix are unstable
					default =
						pkgs.mkShell {
							packages = check.enabledPackages ++ [python pkgs.uv];
							env =
								{
									UV_PYTHON_DOWNLOADS = "never";
									UV_PYTHON = python.interpreter;
								}
								// lib.optionalAttrs pkgs.stdenv.isLinux {
									LD_LIBRARY_PATH = lib.makeLibraryPath pkgs.pythonManylinuxPackages.manylinux1;
								};
						};

					shellHook =
						''
							unset PYTHONPATH
						''
						++ check.shellHook;
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
