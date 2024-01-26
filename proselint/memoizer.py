from __future__ import annotations

import contextlib
import hashlib
import pickle  # noqa: S403
import shutil
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import TYPE_CHECKING
from typing import Callable
from typing import Optional
from typing import TypedDict

from typing_extensions import Self
from typing_extensions import Unpack

from .config_paths import cache_user_path
from .logger import log
from .version import __version__ as version

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
        self._data: dict[str, list[dict]] = {}
        self._age: dict[str, int] = {}
        self._ts_now: int = round(datetime.now(tz=timezone.utc).timestamp())
        self._modified: bool = False
        self.name2key: dict[str, str] = {}

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

    def __getitem__(self, key: str) -> list:
        """Allows direct dict access.
        This allows instance["key"], in addition to instance.data["key"]"""
        return self._data[key]

    def __setitem__(self, key: str, value: list[dict]):
        log.debug("[Memoizer] Store %s", key)
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
        # TODO: reread on file-change. parallel runs,
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
                    _inst._data = data[0]  # noqa: SLF001
                    _inst._age = data[1]  # noqa: SLF001
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
