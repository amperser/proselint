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

learnings

- python seems to automatically cache internal calculation for reruns (if const)
- lru_cache and memoizer only call for trouble during multiprocessing

"""
from timeit import timeit

import proselint
from proselint import memoizer

file_path = proselint.path / "demo.md"

_cfg = proselint.config_default


with file_path.open(encoding="utf-8", errors="replace") as fh:
    _text = fh.read()

_checks = proselint.tools.get_checks(_cfg)

# #########################################################################
print("\n############# Benchmark manually optimized Checks ###################")
print("\n############# * or with calculations in check()   ###################")

specials = [
    "proselint.checks.misc.waxed.check",
    "proselint.checks.terms.venery.check",
    "proselint.checks.uncomparables.misc.check_1",
]

memoizer.cache.clear()
for check in _checks:
    _name = f"{check.__module__}.{check.__name__}"
    if _name in specials:
        memoizer.cache.clear()
        _dur = timeit("_e = check(_text)", globals=locals(), number=1)
        print(f"{_name} took {_dur * 1000:.3f} ms -> uncached")
        _dur = timeit("_e = check(_text)", globals=locals(), number=1)
        print(f"{_name} took {_dur * 1000:.3f} ms -> cached")
        _dur = timeit("_e = check(_text)", globals=locals(), number=1)
        print(f"{_name} took {_dur * 1000:.3f} ms -> cached")
        _dur = timeit("_e = check(_text)", globals=locals(), number=1)
        print(f"{_name} took {_dur * 1000:.3f} ms -> cached")

# ########## output with memoize_const
#
# proselint.checks.misc.waxed.check took 0.067 ms -> uncached
# proselint.checks.misc.waxed.check took 0.029 ms -> cached
# proselint.checks.terms.venery.check took 7.476 ms -> uncached
# proselint.checks.terms.venery.check took 7.208 ms -> cached
# proselint.checks.uncomparables.misc.check_1 took 19.959 ms -> uncached
# proselint.checks.uncomparables.misc.check_1 took 19.694 ms -> cached

# ########## output without extra caching (except uncomparables)

# proselint.checks.misc.waxed.check took 0.077 ms -> uncached
# proselint.checks.misc.waxed.check took 0.029 ms -> cached
# proselint.checks.terms.venery.check took 10.782 ms -> uncached
# proselint.checks.terms.venery.check took 7.339 ms -> cached
# proselint.checks.uncomparables.misc.check_1 took 24.678 ms -> uncached
# proselint.checks.uncomparables.misc.check_1 took 20.797 ms -> cached

print("\n############# Benchmark all Checks ###################")

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
print(f"median: {_val[round(len(_val) / 2)]}")
