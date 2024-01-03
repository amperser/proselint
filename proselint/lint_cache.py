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
from .lint_checks import ResultCheck
from .logger import log


class Cache:
    save_path = cache_user_path / "cache.pickle"

    def __init__(self) -> None:
        self.data_check: dict[str, list[ResultCheck]] = {}
        self.data_lint: dict[str, list] = {}
        self.age: dict[str, int] = {}
        self.ts_now: int = round(datetime.now().timestamp())

    def __exit__(self) -> None:
        """Close previously opened cache shelves."""
        self.to_file()
        self.data_check.clear()

    def __del__(self):
        self.to_file()

    def to_file(self) -> None:
        if len(self.data_check) + len(self.data_lint) < 1:
            return
        if not cache_user_path.is_dir():
            cache_user_path.mkdir(parents=True)
        age_max: int = self.ts_now - round(timedelta(days=1).total_seconds())
        for _key in self.data_check:
            # TODO: could be speed up with dict_base - dict_entries_to_remove
            if self.age[_key] < age_max:
                self.age.pop(_key)
                self.data_check.pop(_key)

        with self.save_path.open("wb", buffering=-1) as fd:
            pickle.dump(
                [self.data_check, self.data_lint, self.age],
                fd,
                fix_imports=False,
                protocol=pickle.HIGHEST_PROTOCOL,
            )
        # log.debug(" -> stored cache")  # too late when exiting

    @classmethod
    def from_file(cls) -> Self:
        instance = cls()
        if cls.save_path.exists():
            with contextlib.suppress(EOFError):
                with cls.save_path.open("rb", buffering=-1) as fd:
                    data = pickle.load(fd, fix_imports=False)  # noqa: S301
                    # TODO: consider replacing pickle with something faster
            if isinstance(data, list) and len(data) > 2:
                instance.data_check = data[0]
                instance.data_lint = data[1]
                instance.age = data[2]
                log.debug(" -> found & restored cache")
        return instance

    def clear(self) -> None:
        """Delete the contents of the cache."""
        log.debug("Deleting the cache...")
        with contextlib.suppress(OSError):
            shutil.rmtree(cache_user_path)
        self.data_check.clear()
        self.data_lint.clear()
        self.age.clear()


cache = Cache.from_file()


###############################################################################
# Wrapper #####################################################################
###############################################################################


def memoize_o(
    fn: Callable,
) -> Callable:
    """Cache results of check-computations on disk.
    Note: fn-signature gets changed! bad design, but good speed-improvement
        -> wrapped_fn(text: str) -> list[Results]
        -> called_fn(text: str, text_hash: str) -> list[Results]
    TODO: decide what to do: extend args of wrapped fn, feed dict into fn?
    """
    _filename = f"{fn.__module__}.{fn.__name__}"

    @functools.wraps(fn)
    def wrapped(text: str, hash_text: Optional[str] = None):
        if hash_text is None:
            # disable cache when used without hash
            return fn(text)
        key = _filename + hash_text

        try:
            return cache.data_check[key]
        except KeyError:
            value = fn(text)
            cache.data_check[key] = value
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


def memoize(
    fn: Callable,
) -> Callable:
    """null, neutral"""

    @functools.wraps(fn)
    def wrapped(text: str, hash_text: Optional[str] = None):
        return fn(text)

    return wrapped


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
        # if not isinstance(config, dict):
        #    config = config_default.proselint_base

        # if checks is None:
        #    checks = get_checks(config)

        key = _filename + hash_content

        try:
            return cache.data_lint[key]
        except KeyError:
            value = fn(content, config, checks, hash_content)
            cache.data_lint[key] = value
            # cache.age[key] = cache.ts_now
            return value
        except TypeError:
            log.error(
                "Warning: could not disk cache call to %s;"
                "it probably has unhashable args. Error: %s",
                _filename,
                traceback.format_exc(),
            )
            return fn(content, config, checks, hash_content)

    return wrapped
