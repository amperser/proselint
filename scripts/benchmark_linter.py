from pathlib import Path
from timeit import timeit

import proselint
from proselint import memoizer
from proselint.tools import get_checks

##################################################################
# Benchmark Linter & Cache
##################################################################

if __name__ == "__main__":
    # NOTE: Safeguard for windows + multiprocessing + python
    #  -> This script crashes when par=True

    file_path = proselint.path / "demo.md"
    corp_path = Path(__file__).parent.parent / "corpora"

    _cfg = proselint.config_default
    options = {
        "serial": (False, True),
        "serial-cached": (False, False),
        "parallel": (True, True),
        "parallel-cached": (True, False),
    }

    print("\n############# lint(demo.md)")

    for _name, _val in options.items():
        _cfg["parallelize"] = _val[0]
        for _i in range(3):
            _checks = get_checks(_cfg)
            with file_path.open() as f_handler:
                _text = f_handler.read()
            if _val[1]:
                memoizer.cache.clear()
            t1 = timeit(
                "e1 = proselint.tools.lint(_text, _cfg, _checks)",
                globals=locals(),
                number=1,
            )
            print(f"{_name} took {t1 * 1e3:4.3f} ms -> run{_i}")

    print("\n############# lint_path(demo.md)")

    for _name, _val in options.items():
        _cfg["parallelize"] = _val[0]
        for _i in range(3):
            if _val[1]:
                memoizer.cache.clear()
            t1 = timeit(
                "e1 = proselint.tools.lint_path(file_path, _cfg)",
                globals=locals(),
                number=1,
            )
            print(f"{_name} took {t1 * 1e3:4.3f} ms -> run{_i}")

    print("\n############# lint_path(corpora)")

    for _name, _val in options.items():
        _cfg["parallelize"] = _val[0]
        for _i in range(3):
            if _val[1]:
                memoizer.cache.clear()
            t1 = timeit(
                "e1 = proselint.tools.lint_path(corp_path, _cfg)",
                globals=locals(),
                number=1,
            )
            print(f"{_name} took {t1 * 1e3:4.3f} ms -> run{_i}")

    print("\n############# proselint ./demo.md")
