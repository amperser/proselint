from timeit import timeit

import proselint
from proselint import memoizer


def test_speed():
    """compare uncached vs cached reads"""
    repetitions = 2

    demo_path = proselint.path / "demo.md"
    _code = "errors = proselint.tools.lint(_text)"
    _setup = "import proselint"
    with demo_path.open(encoding="utf-8", errors="replace") as demo_fh:
        _text = demo_fh.read()

    # make sure it works
    memoizer.cache.clear()
    errors = proselint.tools.lint(_text)
    assert len(errors) > 0

    # without cache
    _dur1 = 0.0
    for _ in range(repetitions):
        memoizer.cache.clear()
        _dur1 += timeit(_code, setup=_setup, globals=locals(), number=1)

    # with cache
    _dur2 = 0.0
    for _ in range(repetitions):
        _dur2 += timeit(_code, setup=_setup, globals=locals(), number=1)

    # without cache, confirmation
    _dur3 = 0.0
    for _ in range(repetitions):
        memoizer.cache.clear()
        _dur3 += timeit(_code, setup=_setup, globals=locals(), number=1)

    assert _dur2 < 0.7 * _dur1
    assert _dur2 < 0.7 * _dur3


def test_consistency():
    """compare result-count"""
    demo_path = proselint.path / "demo.md"
    demo_fh = demo_path.open(encoding="utf-8", errors="replace")
    demo_str = demo_fh.read()
    memoizer.cache.clear()
    errors_a = proselint.tools.lint(demo_str)
    errors_b = proselint.tools.lint(demo_str)

    assert len(errors_a) == len(errors_b)
