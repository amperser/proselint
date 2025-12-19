{
	workspace,
	self,
	lib,
	system,
	pkgs,
	python,
	pythonSet,
}: let
	check = self.checks.${system}.pre-commit;

	editablePythonSet =
		pythonSet.overrideScope (
			lib.composeManyExtensions [
				(workspace.mkEditablePyprojectOverlay {root = "$REPO_ROOT";})

				(final: prev: {
						proselint =
							prev.proselint.overrideAttrs (old: {
									nativeBuildInputs =
										old.nativeBuildInputs
										++ final.resolveBuildSystem {
											editables = [];
										};
								});
					})

				(final: prev: {
						google-re2 =
							prev.google-re2.overrideAttrs (old: {
									nativeBuildInputs =
										(old.nativeBuildInputs or [])
										++ (with final; [setuptools pybind11])
										++ (with pkgs; [re2 abseil-cpp]);
								});
					})
			]
		);
in {
	default =
		pkgs.mkShell {
			buildInputs = check.enabledPackages;

			packages =
				[(editablePythonSet.mkVirtualEnv "proselint-env" {proselint = ["test" "dev" "web"];})]
				++ (with pkgs; [
						git-cliff
						prettier
						nodejs
						typos
						pnpm
						uv
					]);

			env = {
				UV_NO_SYNC = "1";
				UV_PYTHON = python.interpreter;
				UV_PYTHON_DOWNLOADS = "never";
				LD_LIBRARY_PATH = "${pkgs.stdenv.cc.cc.lib}/lib";
			};

			shellHook =
				''
					export REPO_ROOT=$(git rev-parse --show-toplevel)
					unset PYTHONPATH
				''
				+ check.shellHook;
		};
}
