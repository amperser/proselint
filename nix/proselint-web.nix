{
	stdenv,
	nodejs,
	pnpm,
	lib,
	apiURL ? "http://localhost:8000",
	...
}: let
	inherit (lib) importJSON fileset;
	inherit (manifest) name version;

	manifest = importJSON ../website/package.json;
in
	stdenv.mkDerivation (final: {
			inherit version;

			src =
				fileset.toSource {
					root = ../.;
					fileset =
						fileset.union
						../website
						../proselint/checks;
				};

			pname = name;
			sourceRoot = "source/website";

			nativeBuildInputs = [nodejs pnpm.configHook];
			pnpmDeps =
				pnpm.fetchDeps {
					inherit (final) pname;
					src = ../website;

					hash = "sha256-kxKZuowOGgxXKMyn66pqkPQv/xgJlnpVE5r5rYyuBOk=";
					fetcherVersion = 2;
				};

			postUnpack = ''
				mkdir -p $sourceRoot/public
			'';

			buildPhase = ''
				export VITE_API_URL="${apiURL}"
				pnpm run build
			'';

			installPhase = ''
				mkdir -p $out/share/proselint-web
				cp -r dist/* $out/share/proselint-web/
			'';
		})
