from collections import deque
from collections import namedtuple
from dataclasses import dataclass
from timeit import timeit
from typing import NamedTuple

print("############# assemble with list-comprehension")

el = deque(_i for _i in range(10))
print(el)

_dur = timeit(
    stmt="el = deque(_i for _i in range(100))", globals=locals(), number=100_000
)
print(f"dq_1k_a took {_dur * 1000:.2f} ms")
_dur = timeit(
    stmt="el = deque([_i for _i in range(100)])",
    globals=locals(),
    number=100_000,
)
print(f"dq_l1k_a took {_dur * 1000:.2f} ms")
_dur = timeit(
    stmt="el = list([_i for _i in range(100)])",
    globals=locals(),
    number=100_000,
)
print(f"lst_1k_a took {_dur * 1000:.2f} ms")

print("############# assemble with iterable")
_dur = timeit(stmt="el = deque(range(100))", globals=locals(), number=100_000)
print(f"dq_1k_b took {_dur * 1000:.2f} ms")
_dur = timeit(stmt="el = deque([range(100)])", globals=locals(), number=100_000)
print(f"dq_l1k_b took {_dur * 1000:.2f} ms")
_dur = timeit(stmt="el = list(range(100))", globals=locals(), number=100_000)
print(f"lst_1k_b took {_dur * 1000:.2f} ms")

print("\n################### creating lint-results")
# learning:
# - list is fastest, but not the best result type to hand to user
# - dict is slower (halve as fast) and wins against named tuple
# - frozenmap is still not implemented, https://peps.python.org/pep-0603/

Const = namedtuple("ResultLint", ("val1", "val2", "val3"))  # noqa: PYI024
res1 = Const(val1=457, val2=458, val3=120)
res2 = [457, 458, 120]


# @dataclass(eq=False, frozen=True, slots=True,match_args=False, repr=False)
# -> tried to optimize for speed, but this stays slow
@dataclass(
    eq=True,
    frozen=True,
)
class ConstDC:
    val1: int
    val2: int
    val3: int


class ConstClass:
    __slots__ = ("val1", "val2", "val3")

    def __init__(self, val1: int, val2: int, val3: int):
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3


class TupleClass(NamedTuple):
    val1: int
    val2: int
    val3: int


print(res1._asdict())

contenders = {
    "plain list": "res2 = [457, 458, 120]",
    "dict": "res4 ={'val1': 457, 'val2':458, 'val3':120}",
    "namedTuple A": "res1 = Const(val1=457, val2=458, val3=120)",
    "namedTuple B": "res1 = Const(457, 458, 120)",
    "dataClass A": "res5 = ConstDC(val1=457, val2=458, val3=120)",
    "dataClass B": "res5 = ConstDC(457, 458, 120)",
    "constClass A": "res5 = ConstClass(val1=457, val2=458, val3=120)",
    "constClass B": "res5 = ConstClass(457, 458, 120)",
    "tupleClass A": "res5 = ConstClass(val1=457, val2=458, val3=120)",
    "tupleClass B": "res5 = ConstClass(457, 458, 120)",
}

for _name, _code in contenders.items():
    _dur = timeit(stmt=_code, globals=locals())
    print(f"{_name} took {_dur * 1000:.2f} ms")

print("############# extend with append()")
el = deque()
for _i in range(10):
    el.append(_i)
print(el)

x = 5
_dur = timeit(
    stmt="el.append(x)", setup="el = deque()", globals=locals(), number=100_000
)
print(f"dq_app took {_dur * 1000:.2f} ms")
_dur = timeit(stmt="el.append(x)", setup="el = []", globals=locals(), number=100_000)
print(f"dq_app took {_dur * 1000:.2f} ms")

print("############# extend with extend(iterable)")
x = list(range(100))
_dur = timeit(
    stmt="el.extend(x)", setup="el = deque()", globals=locals(), number=100_000
)
print(f"dq_app took {_dur * 1000:.2f} ms")
_dur = timeit(stmt="el.extend(x)", setup="el = []", globals=locals(), number=100_000)
print(f"dq_app took {_dur * 1000:.2f} ms")
