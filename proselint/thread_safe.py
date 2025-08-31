"""Thread-safe utilities for proselint."""

import threading
from typing import Any, Callable, Optional, TypeVar

T = TypeVar('T')


class ThreadSafeSingleton(type):
    """Thread-safe singleton metaclass."""
    
    _instances = {}
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        """Create or return singleton instance thread-safely."""
        if cls not in cls._instances:
            with cls._lock:
                # Double-check pattern
                if cls not in cls._instances:
                    instance = super().__call__(*args, **kwargs)
                    cls._instances[cls] = instance
        return cls._instances[cls]


class ThreadSafeCache:
    """Thread-safe cache implementation."""
    
    def __init__(self, maxsize: int = 128):
        """Initialize thread-safe cache."""
        self._cache = {}
        self._lock = threading.RLock()
        self._maxsize = maxsize
        self._access_count = {}
    
    def get(self, key: Any, default: Any = None) -> Any:
        """Get value from cache thread-safely."""
        with self._lock:
            if key in self._cache:
                self._access_count[key] = self._access_count.get(key, 0) + 1
                return self._cache[key]
            return default
    
    def set(self, key: Any, value: Any) -> None:
        """Set value in cache thread-safely."""
        with self._lock:
            if len(self._cache) >= self._maxsize and key not in self._cache:
                # Remove least recently accessed item
                if self._access_count:
                    lru_key = min(self._access_count, key=self._access_count.get)
                    del self._cache[lru_key]
                    del self._access_count[lru_key]
                elif self._cache:
                    # Fallback to removing first item
                    first_key = next(iter(self._cache))
                    del self._cache[first_key]
            
            self._cache[key] = value
            self._access_count[key] = 0
    
    def clear(self) -> None:
        """Clear cache thread-safely."""
        with self._lock:
            self._cache.clear()
            self._access_count.clear()


def synchronized(lock: Optional[threading.Lock] = None):
    """Decorator to make a method thread-safe."""
    def decorator(func: Callable) -> Callable:
        func_lock = lock or threading.RLock()
        
        def wrapper(*args, **kwargs):
            with func_lock:
                return func(*args, **kwargs)
        
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper
    
    return decorator