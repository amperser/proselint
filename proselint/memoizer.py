from __future__ import annotations

import contextlib
import functools
import hashlib
import pickle
import shutil
import traceback
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

if TYPE_CHECKING:
    from types import TracebackType


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
        self.data: dict[str, list] = {}
        self.age: dict[str, int] = {}
        self.ts_now: int = round(datetime.now().timestamp())
        self.fname2key: dict[str, str] = {}
        # TODO: from_file can also just be done here

    # TODO: add dict-access-fn and add timestamp there
    def __exit__(
        self,
        typ: Optional[type[BaseException]] = None,
        exc: Optional[BaseException] = None,
        tb: Optional[TracebackType] = None,
        extra_arg: int = 0,
    ) -> None:
        """Close previously opened cache shelves."""
        self.to_file()
        self.data.clear()
        Cache._instance = None

    def __del__(self):
        self.to_file()
        Cache._instance = None

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
                # todo: compare version or similar and delete if different
            if isinstance(data, list) and len(data) >= 2:
                _inst.data = data[0]
                _inst.age = data[1]
                log.debug(" -> found & restored cache")
        return _inst

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


def calculate_key(text: str, checks: list[Callable]) -> str:
    """For accessing Cache"""

    text_hash = hashlib.sha224(text.encode("utf-8")).hexdigest()[:50]
    chck_list = [f"{c.__module__}.{c.__name__}" for c in checks]
    chck_hash = hashlib.sha224(" ".join(chck_list).encode("utf-8")).hexdigest()[:10]
    # NOTE: Skip hashing config!
    #   -> Valid assumption that (current) config has
    #      no influence on result below this level
    # WARNING: frozenset(checks).__hash__() varies between runs

    return text_hash + chck_hash


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
            # TODO: also adding filename would enable 2d-dict
            #       d[funcSig,fileSig] = (input_hash,result)
            #                        -> smaller dicts

        key = calculate_key(content, checks)

        try:
            return cache.data[key]
        except KeyError:
            _res = fn(content, config, checks, file_name, _exe=_exe)
            # only store finished results
            if len(_res) == 0 or not isinstance(_res[0], Future):
                log.debug("[Memoizer] Store %s", key)
                cache.data[key] = _res
                cache.age[key] = cache.ts_now
            cache.fname2key[file_name] = key
            return _res
        except TypeError:  # TODO: can be removed?
            log.error(
                "Warning: could not disk cache call to %s;"
                "it probably has unhashable args. Error: %s",
                f"{fn.__module__}.{fn.__name__}",
                traceback.format_exc(),
            )
            return fn(content, config, checks, file_name, _exe=_exe)

    return wrapped
