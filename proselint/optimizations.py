"""Performance optimizations for proselint."""

from typing import List, Iterator, Iterable
import io


def efficient_string_builder(parts: Iterable[str]) -> str:
    """
    Efficiently build a string from parts.
    
    Uses StringIO for better performance than repeated concatenation.
    
    Args:
        parts: Iterable of string parts
    
    Returns:
        Combined string
    """
    buffer = io.StringIO()
    for part in parts:
        buffer.write(part)
    return buffer.getvalue()


def batch_process(items: List, batch_size: int = 100) -> Iterator[List]:
    """
    Process items in batches for better memory efficiency.
    
    Args:
        items: List of items to process
        batch_size: Size of each batch
    
    Yields:
        Batches of items
    """
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]


def deduplicate_preserving_order(items: List) -> List:
    """
    Remove duplicates while preserving order.
    
    More efficient than list(set(items)) and preserves order.
    
    Args:
        items: List with potential duplicates
    
    Returns:
        List without duplicates, order preserved
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def lazy_chain(*iterables):
    """
    Lazy version of itertools.chain that doesn't evaluate until needed.
    
    Args:
        *iterables: Multiple iterables to chain
    
    Yields:
        Items from all iterables
    """
    for iterable in iterables:
        yield from iterable


def memoize_method(method):
    """
    Decorator to memoize instance method results.
    
    Stores results in instance._cache dictionary.
    
    Args:
        method: Method to memoize
    
    Returns:
        Memoized method
    """
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, '_cache'):
            self._cache = {}
        
        # Create cache key from method name and arguments
        key = (method.__name__, args, tuple(sorted(kwargs.items())))
        
        if key not in self._cache:
            self._cache[key] = method(self, *args, **kwargs)
        
        return self._cache[key]
    
    wrapper.__name__ = method.__name__
    wrapper.__doc__ = method.__doc__
    return wrapper


class StringAccumulator:
    """Efficient string accumulator using list join."""
    
    def __init__(self):
        """Initialize accumulator."""
        self._parts = []
    
    def append(self, text: str) -> None:
        """Add text to accumulator."""
        if text:
            self._parts.append(text)
    
    def extend(self, texts: Iterable[str]) -> None:
        """Add multiple texts to accumulator."""
        self._parts.extend(filter(None, texts))
    
    def get_result(self) -> str:
        """Get accumulated string."""
        return ''.join(self._parts)
    
    def clear(self) -> None:
        """Clear accumulator."""
        self._parts.clear()
    
    def __len__(self) -> int:
        """Get number of parts."""
        return len(self._parts)
    
    def __bool__(self) -> bool:
        """Check if accumulator has content."""
        return bool(self._parts)