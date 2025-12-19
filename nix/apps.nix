{
	lib,
	self,
	system,
	...
}: {
	default = {
		type = "app";
		program = lib.getExe' self.packages.${system}.default "proselint";
	};

	api = {
		type = "app";
		program = lib.getExe' self.packages.${system}.api "proselint-api-run";
	};
}
