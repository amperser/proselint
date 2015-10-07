"""Insert the demo into the codemirror site."""
from __future__ import print_function

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

if os.path.exists(live_write_path):
    shutil.rmtree(live_write_path)
shutil.copytree(code_mirror_path, live_write_path)

demo_path = os.path.join(proselint_path, "proselint", "demo.md")

with open(demo_path, "r") as f:
    demo = f.read()

for line in fileinput.input(
        os.path.join(live_write_path, "index.html"), inplace=True):

    if "##DEMO_PLACEHOLDER##" in line:
        print(demo)
    else:
        print(line)
