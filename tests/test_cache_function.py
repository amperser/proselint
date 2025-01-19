from __future__ import annotations

from timeit import timeit

import proselint
from proselint import memoizer

DEMO_PATH = proselint.path / "demo.md"
DEMO_TEXT = DEMO_PATH.open(encoding="utf-8", errors="replace").read()


def test_speed() -> None:
    """Compare uncached vs cached reads."""
    repetitions = 3

    demo_path = proselint.path / "demo.md"
    _text = DEMO_TEXT
    _code = "errors = proselint.tools.lint(_text)"
    _setup = "import proselint"
    # make sure it works
    memoizer.cache.clear_internal()
    errors = proselint.tools.lint(DEMO_TEXT)
    assert len(errors) > 0

    # without cache
    _dur1 = 0.0
    for _ in range(repetitions):
        memoizer.cache.clear_internal()
        _dur1 += timeit(_code, setup=_setup, globals=locals(), number=1)

    # with cache
    _dur2 = 0.0
    for _ in range(repetitions):
        _dur2 += timeit(_code, setup=_setup, globals=locals(), number=1)

    # without cache, confirmation
    _dur3 = 0.0
    for _ in range(repetitions):
        memoizer.cache.clear_internal()
        _dur3 += timeit(_code, setup=_setup, globals=locals(), number=1)

    assert _dur2 < 0.7 * _dur1
    assert _dur2 < 0.7 * _dur3


def test_consistency() -> None:
    """Compare result count from cached and uncached runs."""
    memoizer.cache.clear_internal()
    errors_a = proselint.tools.lint(DEMO_TEXT)
    errors_b = proselint.tools.lint(DEMO_TEXT)
    assert len(errors_a) == len(
        list(memoizer.cache.values())[-1]
    ), "Errors were not cached correctly - quantity mismatch."
    assert len(errors_a) == len(
        errors_b
    ), "Errors were not cached correctly - differing output."
