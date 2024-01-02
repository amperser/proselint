from timeit import timeit

import proselint
from proselint import lint_cache


def test_speed():
    """compare uncached vs cached reads"""
    demo_path = proselint.path / "demo.md"
    demo_fh = demo_path.open(encoding="utf-8", errors="replace")
    _code_a = """
    lint_cache.cache.clear()
    errors = proselint.tools.lint(demo_fh)
    """
    _code_b = """errors = proselint.tools.lint(demo_fh)"""

    lint_cache.cache.clear()

    _dur1 = timeit(_code_a, globals=globals(), number=4)
    _dur2 = timeit(_code_b, globals=globals(), number=4)
    _dur3 = timeit(_code_a, globals=globals(), number=4)

    assert _dur2 < 0.7 * _dur1
    assert _dur2 < 0.7 * _dur3


def test_consistency():
    """compare result-count"""
    demo_path = proselint.path / "demo.md"
    demo_fh = demo_path.open(encoding="utf-8", errors="replace")
    lint_cache.cache.clear()
    errors_a = proselint.tools.lint(demo_fh)
    errors_b = proselint.tools.lint(demo_fh)

    assert len(errors_a) == len(errors_b)
