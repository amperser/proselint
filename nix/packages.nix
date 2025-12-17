{
	workspace,
	attrs,
	...
}: let
	inherit (attrs) pkgs pythonSet;
in {
	default = pythonSet.mkVirtualEnv "proselint-env" workspace.deps.default;

	wheel = pythonSet.proselint.override {pyprojectHook = pythonSet.pyprojectDistHook;};
	sdist = (pythonSet.proselint.override {pyprojectHook = pythonSet.pyprojectDistHook;}).overrideAttrs (old: {env.uvBuildType = "sdist";});

	api = pkgs.callPackage ./proselint-api.nix {inherit pythonSet pkgs;};
}
