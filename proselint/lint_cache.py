from __future__ import annotations

import contextlib
import functools
import hashlib
import pickle
import shutil
import traceback
from datetime import datetime, timedelta
from typing import IO, Callable, Optional, Union

from typing_extensions import Self

from .config_paths import cache_user_path
from .logger import log


class Cache:
    save_path = cache_user_path / "cache.pickle"

    def __init__(self) -> None:
        self.data: dict[str, list] = {}
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
        # log.debug(" -> stored cache")  # too late when exiting

    @classmethod
    def from_file(cls) -> Self:
        _inst = cls()
        if cls.save_path.exists():
            with contextlib.suppress(EOFError):
                with cls.save_path.open("rb", buffering=-1) as fd:
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


def memoize_lint(
    fn: Callable,
) -> Callable:
    """Cache results of lint() on disk."""
    _filename = f"{fn.__module__}.{fn.__name__}"

    @functools.wraps(fn)
    def wrapped(
        content: Union[str, IO],
        config: Optional[dict] = None,
        checks: Optional[list[Callable]] = None,
        hash_content: Optional[str] = None,
    ) -> list:
        if not isinstance(content, str):
            return fn(content, config, checks, hash_content)
            # TODO: also allowing IO would enable 2d-dict d[funcSig,fileSig] = (input_hash,result)
            #                        -> smaller dicts

        if hash_content is None:
            hash_content = hashlib.sha224(content.encode("utf-8")).hexdigest()

        # TODO: assume for now that config & checks don't change between runs -> WRONG!
        #   hash at least frozenset of checks-list

        key = _filename + hash_content

        try:
            return cache.data[key]
        except KeyError:
            value = fn(content, config, checks, hash_content)
            cache.data[key] = value
            cache.age[key] = cache.ts_now
            return value
        except TypeError:  # TODO: can be removed?
            log.error(
                "Warning: could not disk cache call to %s;"
                "it probably has unhashable args. Error: %s",
                _filename,
                traceback.format_exc(),
            )
            return fn(content, config, checks, hash_content)

    return wrapped
