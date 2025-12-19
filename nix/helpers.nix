{
	self,
	nixpkgs,
	overlay,
}: let
	getPythonVersion = let
		val = builtins.getEnv "PYTHON_VERSION";

		result =
			if val == ""
			then "3.13"
			else val;
	in
		builtins.replaceStrings ["."] [""] result;
in {
	forAllSystems = f:
		nixpkgs.lib.genAttrs [
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
						(pkgs.callPackage self.inputs.pyproject.build.packages {inherit python;}).overrideScope (
							nixpkgs.lib.composeManyExtensions [
								self.inputs.build-systems.overlays.default
								overlay
							]
						);
				});
}
