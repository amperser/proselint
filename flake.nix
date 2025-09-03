# TODO: use uv2nix
{
	inputs = {
		nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
		hooks = {
			url = "github:cachix/git-hooks.nix";
			inputs.nixpkgs.follows = "nixpkgs";
		};

		pyproject = {
			url = "github:pyproject-nix/pyproject.nix";
			inputs.nixpkgs.follows = "nixpkgs";
		};
	};

	outputs = {
		self,
		hooks,
		nixpkgs,
		pyproject,
		...
	}: let
		forAllSystems = function:
			nixpkgs.lib.genAttrs [
				"x86_64-linux"
				"aarch64-linux"
				"x86_64-darwin"
				"aarch64-darwin"
			] (system: function system nixpkgs.legacyPackages.${system});

		getPythonVersion = let
			val = builtins.getEnv "PYTHON_VERSION";
			result =
				if val == ""
				then "3.12"
				else val;
		in
			builtins.replaceStrings ["."] [""] result;

		project = pyproject.lib.project.loadPyproject {projectRoot = ./.;};
	in {
		devShells =
			forAllSystems (system: pkgs: let
					python = pkgs."python${getPythonVersion}";
					arg =
						project.renderers.withPackages {
							inherit python project;
							groups = ["test"];
						};

					pyenv = python.withPackages arg;
					check = self.checks.${system}.pre-commit-check;
				in {
					default =
						pkgs.mkShell {
							inherit (check) shellHook;

							packages =
								check.enabledPackages
								++ [
									pyenv
									pkgs.uv
								];
						};
				});

		packages =
			forAllSystems (system: pkgs: let
					python = pkgs."python${getPythonVersion}";
					attrs = project.renderers.buildPythonPackage {inherit python project;};
				in rec {
					default = python.pkgs.buildPythonPackage attrs;
					wheel = default.dist;
				});

		apps =
			forAllSystems (system: _: {
					default = {
						type = "app";
						program = "${self.packages.${system}.default}/bin/proselint";
					};
				});

		checks =
			forAllSystems (system: pkgs: {
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
