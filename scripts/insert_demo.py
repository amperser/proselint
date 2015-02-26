"""Insert the demo into the codemirror site."""

import os
import fileinput
import shutil

proselint_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

code_mirror_path = os.path.join(
    proselint_path,
    "plugins",
    "webeditor")

code_mirror_demo_path = os.path.join(code_mirror_path, "index.html")

live_write_path = os.path.join(proselint_path, "site", "write")

shutil.copytree(code_mirror_path, live_write_path)

demo_path = os.path.join(proselint_path, "demo.md")

with open(demo_path, "r") as f:
    demo = f.read()

for line in fileinput.input(code_mirror_demo_path, inplace=True):

    if "##DEMO_PLACEHOLDER##" in line:
        print demo,
    else:
        print line,
