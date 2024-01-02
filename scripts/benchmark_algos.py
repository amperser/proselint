import cProfile
import hashlib
from pathlib import Path
from timeit import timeit

import proselint
from proselint import lint_cache

##################################################################
# Benchmark Linter & Cache
# -> on newer computer overhead is ~ 100 ms
# -> demo-lint finishes in 500 ms / 100 ms (uncached, cached)
##################################################################

file_path = Path(__file__).parent / "proselint/demo.md"
f = file_path.open(encoding="utf-8", errors="replace")

lint_cache.cache.clear()

sort_by = "tottime"  # tottime or cumtime, see readme

cProfile.run("errors = proselint.tools.lint(f)", sort=sort_by)
cProfile.run('errors = proselint.tools.lint(f)', sort=sort_by)
# cProfile.run(f'proselint --compact {file_path.absolute()}', sort=sort_by)

errors = proselint.tools.lint(f)
num_errors = len(errors)
print(f"Errors found {num_errors}")


##################################################################
# Benchmark Hash-Algos
# -> on newer computer md5 is only slightly faster than sha256 (6%)
# -> choose sha224 for now (fastest on newer computers)
# TODO: test on old hw, x32
##################################################################

file_path = Path(__file__).parent / "proselint/demo.md"
f = file_path.open(encoding="utf-8", errors="replace")
text = f.read()

contenders = {
    "md5": "hashlib.md5(text.encode('utf-8')).hexdigest()",
    "sha1": "hashlib.sha1(text.encode('utf-8')).hexdigest()",
    "sha224": "hashlib.sha224(text.encode('utf-8')).hexdigest()",
    "sha256": "hashlib.sha256(text.encode('utf-8')).hexdigest()",
    "sha384": "hashlib.sha384(text.encode('utf-8')).hexdigest()",
    "sha512": "hashlib.sha512(text.encode('utf-8')).hexdigest()",
    "builtin": "hash(text)",
    "strhash": "text.__hash__()",
}

for _key, _val in contenders.items():
    _dur = timeit(_val, globals=globals(), number=1000)
    _hash = eval(_val)
    print(f"{_key} took {_dur * 1000:.2f} ms, result= {_hash}")


