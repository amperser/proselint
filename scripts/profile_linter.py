import cProfile
from pathlib import Path

import proselint
from proselint import lint_cache

##################################################################
# Profile Linter & Cache
# -> on newer computer overhead is ~ 100 ms
# -> demo-lint finishes in 500 ms / 100 ms (uncached, cached)
##################################################################

file_path = proselint.path / "demo.md"
f = file_path.open(encoding="utf-8", errors="replace")

lint_cache.cache.clear()

sort_by = "tottime"  # tottime or cumtime, see readme

cProfile.run("errors = proselint.tools.lint(f)", sort=sort_by)
cProfile.run("errors = proselint.tools.lint(f)", sort=sort_by)
# cProfile.run(f'proselint --compact {file_path.absolute()}', sort=sort_by)

errors = proselint.tools.lint(f)
num_errors = len(errors)
print(f"Errors found {num_errors}")