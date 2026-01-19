{pkgs ? import <nixpkgs> {}}: let
	python =
		pkgs.python3.override {
			packageOverrides = self: super: {
				frictionless =
					super.frictionless.overridePythonAttrs (_: {
							doCheck = false;
							doInstallCheck = false;
						});
			};
		};
in
	pkgs.mkShell {
		packages = [(python.withPackages (ps: [ps.frictionless]))];
	}
