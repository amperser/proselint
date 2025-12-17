{
	inputs = {
		nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.11";

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

		pyproject = {
			url = "github:pyproject-nix/pyproject.nix";
			inputs.nixpkgs.follows = "nixpkgs";
		};

		build-systems = {
			url = "github:pyproject-nix/build-system-pkgs";
			inputs = {
				uv2nix.follows = "uv";
				nixpkgs.follows = "nixpkgs";
				pyproject-nix.follows = "pyproject";
			};
		};
	};

	outputs = {
		uv,
		self,
		nixpkgs,
		...
	}: let
		inherit (nixpkgs) lib;
		inherit (import ./nix/helpers.nix {inherit self nixpkgs overlay;}) forAllSystems;

		workspace = uv.lib.workspace.loadWorkspace {workspaceRoot = ./.;};
		overlay = workspace.mkPyprojectOverlay {sourcePreference = "wheel";};

		importWithAttrs = path:
			forAllSystems (attrs: import path {inherit workspace self lib attrs;});
	in {
		devShells = importWithAttrs ./nix/dev-shells.nix;
		packages = importWithAttrs ./nix/packages.nix;
		checks = importWithAttrs ./nix/checks.nix;
		apps = importWithAttrs ./nix/apps.nix;
	};
}
