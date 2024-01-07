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

    _cfg = proselint.config_default
    options = {
        "serial": False,
        "PAR": True,
    }

    with file_path.open(encoding="utf-8", errors="replace") as fh:
        _text = fh.read()
    _checks = get_checks(_cfg)
    # TODO: experiment with overhead of these

    for _name, _val in options.items():
        _cfg["parallelize"] = _val
        memoizer.cache.clear()
        t1 = timeit(
            "e1 = proselint.tools.lint(_text, _cfg, _checks)",
            globals=locals(),
            number=1,
        )
        print(f"Lint with cfg={_name} took {t1 * 1e3:4.3f} ms uncached")
        memoizer.cache.clear()
        t2 = timeit(
            "e1 = proselint.tools.lint(_text, _cfg, _checks)",
            globals=locals(),
            number=1,
        )
        print(f"Lint with cfg={_name} took {t2 * 1e3:4.3f} ms uncached rerun")
        t3 = timeit(
            "e2 = proselint.tools.lint(_text, _cfg, _checks)",
            globals=locals(),
            number=1,
        )
        print(f"Lint with cfg={_name} took {t3 * 1e3:4.3f} ms cached")
