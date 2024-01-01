from __future__ import annotations

import contextlib
import functools
import pickle
import shutil
import traceback
from datetime import datetime, timedelta
from typing import Callable

from typing_extensions import Self

from .logger import log
from .config_paths import cache_user_path
from .lint_checks import ResultCheck


class Cache:
    save_path = cache_user_path / "cache.pickle"

    def __init__(self) -> None:
        self.data: dict[str, list[ResultCheck]] = {}
        self.age: dict[str, int] = {}
        self.ts_now: int = round(datetime.now().timestamp())

    def __exit__(self) -> None:
        """Close previously opened cache shelves."""
        self.to_file()
        self.data.clear()

    def __del__(self):
        self.to_file()

    def to_file(self) -> None:
        if len(self.data) < 1:
            return
        if not cache_user_path.is_dir():
            cache_user_path.mkdir(parents=True)
        age_max: int = self.ts_now - round(timedelta(days=1).total_seconds())
        for _key in self.data:
            # TODO: could be speed up with dict_base - dict_entries_to_remove
            if self.age[_key] < age_max:
                self.age.pop(_key)
                self.data.pop(_key)
        with self.save_path.open("wb", buffering=-1) as fd:
            pickle.dump(
                [self.data, self.age],
                fd,
                fix_imports=False,
                protocol=pickle.HIGHEST_PROTOCOL,
            )
        log.debug(" -> stored cache")

    @classmethod
    def from_file(cls) -> Self:
        instance = cls()
        if cls.save_path.exists():
            with contextlib.suppress(EOFError):
                with cls.save_path.open("rb", buffering=-1) as fd:
                    data = pickle.load(fd, fix_imports=False)  # noqa: S301
                    # TODO: consider replacing pickle with something faster
                instance.data = data[0]
                instance.age = data[1]
                log.debug(" -> found & restored cache")
        return instance

    def clear(self) -> None:
        """Delete the contents of the cache."""
        log.debug("Deleting the cache...")
        with contextlib.suppress(OSError):
            shutil.rmtree(cache_user_path)
        self.data.clear()
        self.age.clear()


cache = Cache.from_file()


###############################################################################
# Wrapper #####################################################################
###############################################################################

def memoize(
    fn: Callable,
) -> Callable:
    """Cache results of computations on disk.
    Note: fn-signature gets changed! bad design, but good speed-improvement
        -> wrapped_fn(text: str) -> list[Results]
        -> called_fn(text: str, text_hash: str) -> list[Results]
    TODO: decide what to do: extend args of wrapped fn, feed dict into fn?
    """
    _filename = f"{fn.__module__}.{fn.__name__}"

    @functools.wraps(fn)
    def wrapped(text: str, hash_text: str):
        key = _filename + hash_text

        try:
            return cache.data[key]
        except KeyError:
            value = fn(text)
            cache.data[key] = value
            cache.age[key] = cache.ts_now
            return value
        except TypeError:
            log.error(
                "Warning: could not disk cache call to %s;"
                "it probably has unhashable args. Error: %s",
                _filename,
                traceback.format_exc(),
            )
            return fn(text)

    return wrapped
