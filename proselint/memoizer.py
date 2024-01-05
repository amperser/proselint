from __future__ import annotations

import contextlib
import functools
import hashlib
import pickle
import shutil
from concurrent.futures import Executor
from concurrent.futures import Future
from datetime import datetime
from datetime import timedelta
from typing import IO
from typing import TYPE_CHECKING
from typing import Callable
from typing import Optional
from typing import TypedDict
from typing import Union

from typing_extensions import Self
from typing_extensions import Unpack

from .config_paths import cache_user_path
from .logger import log
from .version import __version__ as version

if TYPE_CHECKING:
    from types import TracebackType

    from .tools import ResultLint


class Cache:
    save_path = cache_user_path / "cache.pickle"
    _instance: Optional[Self] = None

    @classmethod
    def __new__(cls, *_args: tuple, **_kwargs: Unpack[TypedDict]) -> Self:
        """Implements singleton class."""
        if cls._instance is None:
            cls._instance = object.__new__(cls)
            return cls._instance
        return cls._instance

    def __init__(self) -> None:
        self._data: dict[str, list[ResultLint]] = {}
        self._age: dict[str, int] = {}
        self._ts_now: int = round(datetime.now().timestamp())
        self._modified: bool = False
        self.fname2key: dict[str, str] = {}

    def __exit__(
        self,
        typ: Optional[type[BaseException]] = None,
        exc: Optional[BaseException] = None,
        tb: Optional[TracebackType] = None,
        extra_arg: int = 0,
    ) -> None:
        """Close previously opened cache shelves."""
        self.to_file()
        self._data.clear()
        Cache._instance = None

    def __del__(self):
        self.to_file()
        Cache._instance = None

    def __getitem__(self, key: str) -> list[ResultLint]:
        """Allows dict access -> instance["key"], in addition to instance.data["key"]"""
        return self._data[key]

    def __setitem__(self, key: str, value: list[ResultLint]):
        self._data[key] = value
        self._age[key] = self._ts_now
        self._modified = True

    def to_file(self) -> None:
        # only save when needed
        if (not self._modified) or len(self._data) < 1:
            return
        if not cache_user_path.is_dir():
            cache_user_path.mkdir(parents=True)
        age_max: int = self._ts_now - round(timedelta(days=1).total_seconds())
        # todo: reread on file-change. parallel runs,
        for _key in self._data:
            # TODO: could be speed up with dict_base - dict_entries_to_remove
            if self._age[_key] < age_max:
                self._age.pop(_key)
                self._data.pop(_key)

        with self.save_path.open("wb", buffering=-1) as fd:
            pickle.dump(
                [self._data, self._age, version],
                fd,
                fix_imports=False,
                protocol=pickle.HIGHEST_PROTOCOL,
            )
        # log.debug(" -> stored cache")  # too late when exiting

    @classmethod
    def from_file(cls) -> Self:
        _inst = cls()
        if cls.save_path.exists():
            with (
                contextlib.suppress(EOFError),
                cls.save_path.open("rb", buffering=-1) as fd,
            ):
                data = pickle.load(fd, fix_imports=False)  # noqa: S301
                # TODO: consider replacing pickle with something faster
                # only restore if data fits and package-version matches
                if isinstance(data, list) and len(data) >= 3 and data[2] == version:
                    _inst._data = data[0]
                    _inst._age = data[1]
                    log.debug(" -> found & restored cache")
        return _inst

    def clear(self) -> None:
        """Delete the contents of the cache."""
        log.debug("Deleting the cache...")
        with contextlib.suppress(OSError):
            shutil.rmtree(cache_user_path)
        self._data.clear()
        self._age.clear()

    @staticmethod
    def calculate_key(text: str, checks: list[Callable]) -> str:
        """For accessing Cache-entry"""

        text_hash = hashlib.sha224(text.encode("utf-8")).hexdigest()[:50]
        chck_list = [f"{c.__module__}.{c.__name__}" for c in checks]
        chck_hash = hashlib.sha224(" ".join(chck_list).encode("utf-8")).hexdigest()[:10]
        # NOTE: Skip hashing config!
        #   -> Valid assumption that (current) config has
        #      no influence on result below this level
        # WARNING: frozenset(checks).__hash__() varies between runs

        return text_hash + chck_hash


cache = Cache.from_file()


###############################################################################
# Memoizer Access -> Wrapper ##################################################
###############################################################################


def memoize_future(result: list[ResultLint], file_name: str) -> None:
    """used to later add result -> when working with multiprocessing"""
    key = cache.fname2key.get(file_name)
    log.debug("[Memoizer] LateStore %s", key)
    cache[key] = result


def memoize_lint(
    fn: Callable,
) -> Callable:
    """Cache results of lint() on disk."""

    @functools.wraps(fn)
    def wrapped(
        content: Union[str, IO],
        config: Optional[dict] = None,
        checks: Optional[list[Callable]] = None,
        file_name: Optional[str] = None,
        *,
        _exe: Optional[Executor] = None,
    ) -> list:
        if not isinstance(content, str):
            return fn(content, config, checks, file_name, _exe=_exe)
            # TODO: filename enables 2d-dict
            #       d[funcSig,fileSig] = (input_hash,result)
            #                        -> smaller dicts

        key = cache.calculate_key(content, checks)

        try:
            return cache[key]
        except KeyError:
            _res = fn(content, config, checks, file_name, _exe=_exe)
            # only store finished results
            if len(_res) == 0 or not isinstance(_res[0], Future):
                log.debug("[Memoizer] Store %s", key)
                cache[key] = _res
            cache.fname2key[file_name] = key
            return _res

    return wrapped
