"""
learnings:
- precompiling regex patterns can speed up find() >30% for small texts
- is less relevant for large texts, demo is 2930 vs 2922 ms
- BUT re-module seems to memoize
"""

import pickle
import re
from pathlib import Path
from timeit import timeit

import proselint

use_demo = True

regex_str = r"(\b\w+\s+\w+\s+\w+\b)\s+\1\b"
regex_pat = re.compile(regex_str, flags=re.IGNORECASE)
setup = "re.purge()"

print("\n# ################# short string #################")

text = "this is an example is an example of a regular expression"

_dur = timeit("_e = re.findall(regex_str, text, flags=re.IGNORECASE)", setup=setup, globals=locals(), number=100_000)
print(f"{_dur * 1000:.3f} ms -> re.find()")

_dur = timeit("_e = regex_pat.findall(text)", setup=setup, globals=locals(), number=100_000)
print(f"{_dur * 1000:.3f} ms -> pattern.find()")

re.findall(regex_str, text, flags=re.IGNORECASE)

print("\n# ################# demo.md #################")

file_path = proselint.path / "demo.md"
with file_path.open() as fh:
    text = fh.read()

_dur = timeit("_e = re.findall(regex_str, text, flags=re.IGNORECASE)", setup=setup, globals=locals(), number=1_000)
print(f"{_dur * 1000:.3f} ms -> re.find(demo.md)")

_dur = timeit("_e = regex_pat.findall(text)", setup=setup, globals=locals(), number=1_000)
print(f"{_dur * 1000:.3f} ms -> pattern.find(demo.md)")

re.findall(regex_str, text, flags=re.IGNORECASE)

print("\n# ################# does it pickle? #################")

save_path = Path(__file__).parent / "regex.pickle"
with save_path.open("wb", buffering=-1) as fd:
    pickle.dump(
        [regex_pat, regex_str],
        fd,
        fix_imports=False,
        protocol=pickle.HIGHEST_PROTOCOL,
    )

print("no exceptions -> it works")
