""" Benchmark different levels of access
- proselint executable, lint_path(), lint() -> each a level lower

learnings:
- lint() vs lint_path(): overhead of cached-runs is ~50% (0.4 ms) - significant but irrelevant
- proselint vs lint_path(): overhead is >~65 ms for one file
    - linting  demo-file is only half as fast
    - cached-version is even 60x slower ... -> abs. relevant
    - TODO: find faster alternative to click
"""
import platform
import subprocess  # noqa: S404
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
    _os = platform.system()

    _cfg = proselint.config_default
    options = {
        "serial": (False, True),
        "serial-cached": (False, False),
        "parallel": (True, True),
        "parallel-cached": (True, False),
    }
    _num_checks = len(proselint.tools.get_checks(_cfg))

    print(f"\n############# lint(demo.md) - {_os}, {_num_checks} checks")

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

    print(f"\n############# lint_path(demo.md) - {_os}, {_num_checks} checks")

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

    print(f"\n############# proselint(demo.md) - parallel, {_os}, {_num_checks} checks")

    cmds = {
        "parallel": ["proselint", file_path.as_posix(), "-o", "compact"],
        "parallel-cached": ["proselint", file_path.as_posix(), "-o", "compact"],
    }
    _cmd1 = "subprocess.call("
    _cmd3 = ", timeout=4, shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)"

    # test
    subprocess.call(
        cmds["parallel"],
        timeout=4,
        shell=False,  # noqa: S603
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    memoizer.cache.clear()
    for _name, _cmd in cmds.items():
        _cmd2 = f"""[{', '.join("'" + _p + "'" for _p in _cmd)}]"""
        t1 = timeit(
            _cmd1 + _cmd2 + _cmd3,
            globals=locals(),
            number=1,
        )
        print(f"{_name} took {t1 * 1e3:4.3f} ms")

    print(f"\n############# lint_path(corpora) - {_os}, {_num_checks} checks")

    for _name, _val in options.items():
        _cfg["parallelize"] = _val[0]
        for _i in range(2):
            if _val[1]:
                memoizer.cache.clear()
            t1 = timeit(
                "e1 = proselint.tools.lint_path(corp_path, _cfg)",
                globals=locals(),
                number=1,
            )
            print(f"{_name} took {t1 * 1e3:4.3f} ms -> run{_i}")

    print(f"\n############# proselint ./corpora - {_os}, {_num_checks} checks")

    cmds = {
        "parallel": ["proselint", corp_path.as_posix(), "-o", "compact"],
        "parallel-cached": ["proselint", corp_path.as_posix(), "-o", "compact"],
    }
    _cmd1 = "subprocess.call("
    _cmd3 = ", timeout=60, shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)"

    memoizer.cache.clear()
    for _name, _cmd in cmds.items():
        _cmd2 = f"""[{', '.join("'" + _p + "'" for _p in _cmd)}]"""
        t1 = timeit(
            _cmd1 + _cmd2 + _cmd3,
            globals=locals(),
            number=1,
        )
        print(f"{_name} took {t1 * 1e3:4.3f} ms")
