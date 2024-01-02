from timeit import timeit

import proselint
from proselint import lint_cache


def test_speed():
    """compare uncached vs cached reads"""
    import proselint

    demo_path = proselint.path / "demo.md"
    _code = "errors = proselint.tools.lint(demo_fh)"
    repetitions = 2

    # make sure it works
    lint_cache.cache.clear()
    with demo_path.open(encoding="utf-8", errors="replace") as demo_fh:
        errors = proselint.tools.lint(demo_fh)
    assert len(errors) > 0

    # without cache
    _dur1 = 0.0
    for _ in range(repetitions):
        with demo_path.open(encoding="utf-8", errors="replace") as demo_fh:
            lint_cache.cache.clear()
            _dur1 += timeit(_code, globals=locals(), number=1)

    # with cache
    _dur2 = 0.0
    for _ in range(repetitions):
        with demo_path.open(encoding="utf-8", errors="replace") as demo_fh:
            _dur2 += timeit(_code, globals=locals(), number=1)

    # without cache, confirmation
    _dur3 = 0.0
    for _ in range(repetitions):
        with demo_path.open(encoding="utf-8", errors="replace") as demo_fh:
            lint_cache.cache.clear()
            _dur3 += timeit(_code, globals=locals(), number=1)

    assert _dur2 < 0.7 * _dur1
    assert _dur2 < 0.7 * _dur3


def test_consistency():
    """compare result-count"""
    demo_path = proselint.path / "demo.md"
    demo_fh = demo_path.open(encoding="utf-8", errors="replace")
    demo_str = demo_fh.read()
    lint_cache.cache.clear()
    errors_a = proselint.tools.lint(demo_str)
    errors_b = proselint.tools.lint(demo_str)

    assert len(errors_a) == len(errors_b)
