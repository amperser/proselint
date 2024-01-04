""" Benchmark Checks

goal: find slowest ones, equalize them a bit


rules of thumb

- only adjust extreme cases
- fastest
    - if they are in same file, try to combine them in one check
- slowest
    - find ways to optimize
    - maybe split them up if >> 10x of mean()
- alternative: add prio to scheduler by sorting checks (keyword in fn-name)

# todo: look at our cached constants - test behavior
"""
from timeit import timeit

import proselint
import proselint.lint_checks

file_path = proselint.path / "demo.md"

_cfg = proselint.config_default


with file_path.open(encoding="utf-8", errors="replace") as fh:
    _text = fh.read()

_checks = proselint.lint_checks.get_checks(_cfg)

result = {}
for check in _checks:
    _name = f"{check.__module__}.{check.__name__}"
    result[_name] = timeit("_e = check(_text)", globals=locals(), number=10)

result = dict(sorted(result.items(), key=lambda item: item[1]))
for _key, _value in result.items():
    print(f"{_key}: {_value}")

_val = list(result.values())
print(f"count:  {len(_val)}")
print(f"min:    {min(_val)}")
print(f"max:    {max(_val)}")
print(f"mean:   {sum(_val) / len(_val)}")
print(f"median: {_val[round(len(_val)/2)]}")
