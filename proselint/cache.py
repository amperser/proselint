"""Caching utilities for proselint."""

from functools import lru_cache
from re import Pattern, compile as rcompile
from typing import Union


@lru_cache(maxsize=512)
def get_compiled_pattern(pattern: str, flags: int = 0) -> Pattern[str]:
    """Get a compiled regex pattern with caching."""
    return rcompile(pattern, flags)


class PatternCache:
    """A cache for compiled regex patterns."""
    
    def __init__(self, maxsize: int = 1024):
        """Initialize the pattern cache."""
        self._cache: dict[tuple[str, int], Pattern[str]] = {}
        self._maxsize = maxsize
        self._hits = 0
        self._misses = 0
    
    def get(self, pattern: str, flags: int = 0) -> Pattern[str]:
        """Get a compiled pattern from cache or compile and cache it."""
        key = (pattern, flags)
        if key in self._cache:
            self._hits += 1
            return self._cache[key]
        
        self._misses += 1
        compiled = rcompile(pattern, flags)
        
        # Simple LRU: if cache is full, remove oldest entry
        if len(self._cache) >= self._maxsize:
            # Remove first (oldest) item
            del self._cache[next(iter(self._cache))]
        
        self._cache[key] = compiled
        return compiled
    
    def clear(self) -> None:
        """Clear the cache."""
        self._cache.clear()
        self._hits = 0
        self._misses = 0
    
    @property
    def hit_rate(self) -> float:
        """Get the cache hit rate."""
        total = self._hits + self._misses
        return self._hits / total if total > 0 else 0.0


# Global pattern cache instance
pattern_cache = PatternCache()