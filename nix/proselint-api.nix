{
	pythonSet,
	stdenv,
	bash,
	lib,
	...
}: let
	name = "proselint-api";
	env =
		pythonSet.mkVirtualEnv "${name}-env" {
			proselint = ["web"];
		};
in
	stdenv.mkDerivation {
		inherit name;
		src = ../.;

		dontBuild = true;
		dontConfigure = true;

		installPhase = ''
			mkdir -p $out/bin $out/share/${name}
			cp $src/app.py $out/share/${name}

			cat > $out/bin/${name}-run <<-EOF
			#!${lib.getExe bash}
			cd $out/share/${name}
			exec ${lib.getExe' env "uvicorn"} app:app "\$@"
			EOF

			chmod +x $out/bin/${name}-run
		'';
	}
