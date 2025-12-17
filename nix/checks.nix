{
	attrs,
	self,
	lib,
	...
}: let
	inherit (attrs) system pkgs;
in {
	pre-commit =
		self.inputs.hooks.lib.${system}.run {
			src = ./.;
			package = pkgs.prek;

			hooks = {
				trim-trailing-whitespace.enable = true;
				end-of-file-fixer.enable = true;
				mixed-line-endings.enable = true;
				markdownlint.enable = true;
				alejandra.enable = true;
				convco.enable = true;
				ruff.enable = true;

				statix = {
					enable = true;
					settings.ignore = ["/.direnv"];
				};

				pyright = {
					enable = true;
					package = pkgs.basedpyright;
					entry = lib.getExe pkgs.basedpyright;
				};
			};
		};
}
