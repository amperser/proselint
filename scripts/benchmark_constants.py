from __future__ import annotations

from functools import cached_property
from functools import lru_cache
from timeit import timeit

# LEARNING:
#   - results of fns are not automatically cached
#   - something like @lru_cache can speed up reruns during runtime
#   - cached_property only works on classes and behaves like lru-cache
#   -> switch to persistent cache by extending proselints memoizer
# TODO: add unittests for FNs in proselint to detect regressions

print("\n################################### LRU-Cache")


@lru_cache
def costly_fn() -> list[int]:
    return list(range(10_000_000))


_t = timeit("_e = costly_fn()", globals=globals(), number=1)
print(f"1st fn-call took {_t * 1e3:4.3f} ms -> cached from now on")

_t = timeit("_e = costly_fn()", globals=globals(), number=1)
print(f"2nd fn-call took {_t * 1e3:4.3f} ms")

_t = timeit("_e = costly_fn()", globals=globals(), number=1)
print(f"3rd fn-call took {_t * 1e3:4.3f} ms")

_t = timeit("_e = costly_fn()", globals=globals(), number=1)
print(f"4th fn-call took {_t * 1e3:4.3f} ms")

_t = timeit("_e = list(range(10_000_000))", globals=globals(), number=1)
print(f"raw-call took {_t * 1e3:4.3f} ms -> seems to be always a bit slower")


print("\n################################### cached property")


class Costly:
    @cached_property
    def compute(self) -> list:
        return list(range(10_000_000))


_t = timeit("_e = Costly().compute", globals=globals(), number=1)
print(f"1st prop-call with instantiation {_t * 1e3:4.3f} ms -> uncached")

_t = timeit("_e = Costly().compute", globals=globals(), number=1)
print(
    f"2nd prop-call with instantiation {_t * 1e3:4.3f} ms -> newly created, uncached)",
)

_c = Costly()

_t = timeit("_e = _c.compute", globals=globals(), number=1)
print(f"1nd prop-call took {_t * 1e3:4.3f} ms ->")

_t = timeit("_e = _c.compute", globals=globals(), number=1)
print(f"1st prop-call took {_t * 1e3:4.3f} ms -> now cached property)")
