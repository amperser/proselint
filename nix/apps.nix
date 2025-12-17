{
	attrs,
	self,
	lib,
	...
}: let
	inherit (attrs) system;
in {
	default = {
		type = "app";
		program = lib.getExe' self.packages.${system}.default "proselint";
	};

	api = {
		type = "app";
		program = lib.getExe' self.packages.${system}.api "proselint-api-run";
	};
}
