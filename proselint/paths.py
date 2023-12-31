from pathlib import Path

proselint_path = Path(__file__).parent
demo_file = proselint_path / "demo.md"

user_path = Path("~").expanduser()
cwd_path = Path.cwd()