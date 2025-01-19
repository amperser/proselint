"""Insert the demo into the codemirror site."""
import fileinput
import shutil
from pathlib import Path

project_path = Path(__file__).parent.parent

code_mirror_path = project_path / "plugins" / "webeditor"

code_mirror_demo_path = code_mirror_path / "index.html"

live_write_path = project_path / "site" / "write"

if live_write_path.exists():
    shutil.rmtree(live_write_path)
shutil.copytree(code_mirror_path, live_write_path)

demo_path = project_path / "proselint" / "demo.md"

with demo_path.open() as f:
    demo = f.read()

for line in fileinput.input(live_write_path / "index.html", inplace=True):
    if "##DEMO_PLACEHOLDER##" in line:
        print(demo)
    else:
        print(line)
