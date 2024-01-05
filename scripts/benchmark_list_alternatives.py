from collections import deque
from timeit import timeit

print("############# assemble with list-comprehension")

el = deque(_i for _i in range(10))
print(el)

_dur = timeit(
    stmt="el = deque(_i for _i in range(100))", globals=locals(), number=100_000
)
print(f"dq_1k_a took {_dur * 1000:.2f} ms")
_dur = timeit(
    stmt="el = deque([_i for _i in range(100)])", globals=locals(), number=100_000
)
print(f"dq_l1k_a took {_dur * 1000:.2f} ms")
_dur = timeit(
    stmt="el = list([_i for _i in range(100)])", globals=locals(), number=100_000
)
print(f"lst_1k_a took {_dur * 1000:.2f} ms")

print("############# assemble with iterable")
_dur = timeit(stmt="el = deque(range(100))", globals=locals(), number=100_000)
print(f"dq_1k_b took {_dur * 1000:.2f} ms")
_dur = timeit(stmt="el = deque([range(100)])", globals=locals(), number=100_000)
print(f"dq_l1k_b took {_dur * 1000:.2f} ms")
_dur = timeit(stmt="el = list(range(100))", globals=locals(), number=100_000)
print(f"lst_1k_b took {_dur * 1000:.2f} ms")

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
