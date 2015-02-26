"""Insert the demo into the codemirror site."""

import os
import fileinput

proselint_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

code_mirror_demo_path = os.path.join(
    proselint_path,
    "plugins",
    "webeditor",
    "index.html")

demo_path = os.path.join(proselint_path, "demo.md")

with open(demo_path, "r") as f:
    demo = f.read()

for line in fileinput.input(code_mirror_demo_path, inplace=True):

    if "##DEMO_PLACEHOLDER##" in line:
        print demo,
    else:
        print line,
