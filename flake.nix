# TODO: use uv2nix
{
  inputs = {
    utils.url = "github:numtide/flake-utils";
    hooks.url = "github:cachix/git-hooks.nix";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-25.05";
    pyproject = {
      url = "github:pyproject-nix/pyproject.nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    self,
    hooks,
    utils,
    nixpkgs,
    pyproject,
    ...
  }:
    utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {inherit system;};
      python = pkgs.python312;
      project = pyproject.lib.project.loadPyproject {projectRoot = ./.;};
    in {
      devShells.default = let
        arg = project.renderers.withPackages {inherit python;};
        pyenv = python.withPackages arg;
        check = self.checks.${system}.pre-commit-check;
      in
        pkgs.mkShell {
          inherit (check) shellHook;

          packages = check.enabledPackages ++ [
            pyenv
            pkgs.uv
          ];
        };

      packages.default = let
        attrs = project.renderers.buildPythonPackage {inherit python;};
      in
        python.pkgs.buildPythonPackage attrs;

      apps.default = {
        type = "app";
        program = "${self.packages.${system}.default}/bin/proselint";
      };

      checks = {
        pre-commit-check = hooks.lib.${system}.run {
          src = ./.;
          hooks = {
            ruff.enable = true;
          };
        };
      };
    });
}
