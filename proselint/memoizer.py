"""The cache system."""

from __future__ import annotations

import contextlib
import hashlib
import pickle  # noqa: S403
import shutil
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, Optional, TypedDict

from cachetools import TTLCache
from typing_extensions import Self, Unpack

from .config_paths import cache_user_path
from .logger import log
from .version import __version__ as version

if TYPE_CHECKING:
    from proselint.checks import CheckSpec


class Cache(TTLCache):
    """The cache system."""

    save_path = cache_user_path / "cache.pickle"
    _instance: Optional[Self] = None

    @classmethod
    def __new__(cls, *_args: tuple, **_kwargs: Unpack[TypedDict]) -> Self:
        """Form a singleton class."""
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, max_size: int = 128) -> None:
        """Create a cache instance."""
        super().__init__(max_size, ttl=timedelta(days=1), timer=datetime.now)
        self.name_to_key: dict[str, str] = {}

    def __setitem__(self, key: str, value: list) -> None:
        """Set or update a cache entry."""
        log.debug("[Memoizer] Store %s", key)
        super().__setitem__(key, value)

    def to_file(self) -> None:
        """Save the cache to its save path."""
        # TODO: reimplement _modified check
        # this is difficult because loading the whole cache instance from
        # pickle may trigger _modified, and it will also persist across runs,
        # so it ends up being useless
        if len(self) < 1:
            return
        if not cache_user_path.is_dir():
            cache_user_path.mkdir(parents=True)

        with self.save_path.open("wb", buffering=-1) as fd:
            pickle.dump(
                [self, version],
                fd,
                fix_imports=False,
                protocol=pickle.HIGHEST_PROTOCOL,
            )
        log.debug("[Memoizer] Persisted to disk")  # too late when exiting

    @classmethod
    def from_file(cls) -> Self:
        """Get a cache instance from a file."""
        if cls.save_path.exists():
            with (
                contextlib.suppress(EOFError),
                cls.save_path.open("rb", buffering=-1) as fd,
            ):
                data = pickle.load(fd, fix_imports=False)  # noqa: S301
                # TODO: consider replacing pickle with something faster
                # only restore if data fits and package-version matches
                if (
                    isinstance(data, list)
                    and len(data) >= 2
                    and data[1] == version
                ):
                    log.debug("[Memoizer] Found and restored cache")
                    return data[0]
        return cls()

    def clear_internal(self) -> None:
        """Delete the contents of the cache."""
        super().clear()

    def clear(self) -> None:
        """Delete the contents of the cache, including the on-disk copy."""
        log.debug("Deleting the cache...")
        with contextlib.suppress(OSError):
            shutil.rmtree(cache_user_path)
        self.clear_internal()

    @staticmethod
    def calculate_key(text: str, checks: list[CheckSpec]) -> str:
        """Compute the key for accessing a cache entry."""
        text_hash = hashlib.sha224(text.encode("utf-8")).hexdigest()[:50]
        chck_text = " ".join(sorted([c.path for c in checks]))
        chck_hash = hashlib.sha224(chck_text.encode("utf-8")).hexdigest()[:10]
        # NOTE: Skip hashing config!
        #   -> Valid assumption that (current) config has
        #      no influence on result below this level
        # WARNING: frozenset(checks).__hash__() varies between runs

        return text_hash + chck_hash


cache = Cache.from_file()
