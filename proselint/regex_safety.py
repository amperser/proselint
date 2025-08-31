"""Regex safety utilities to prevent catastrophic backtracking."""

import re
import signal
import functools
from typing import Pattern, Optional, Iterator, Match
from contextlib import contextmanager


class RegexTimeout(Exception):
    """Raised when regex operation times out."""
    pass


@contextmanager
def timeout(seconds: int = 5):
    """Context manager for timing out operations."""
    def handler(signum, frame):
        raise RegexTimeout(f"Operation timed out after {seconds} seconds")
    
    # Set the signal handler and alarm
    old_handler = signal.signal(signal.SIGALRM, handler)
    signal.alarm(seconds)
    
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old_handler)


def safe_finditer(
    pattern: Pattern[str] | str,
    string: str,
    flags: int = 0,
    timeout_seconds: int = 5
) -> Iterator[Match[str]]:
    """
    Safe version of re.finditer with timeout protection.
    
    Prevents catastrophic backtracking by timing out long-running regex operations.
    """
    if isinstance(pattern, str):
        pattern = re.compile(pattern, flags)
    
    try:
        with timeout(timeout_seconds):
            yield from pattern.finditer(string)
    except RegexTimeout:
        # Return empty iterator if regex times out
        return
    except Exception:
        # Other exceptions should still propagate
        raise


def safe_search(
    pattern: Pattern[str] | str,
    string: str,
    flags: int = 0,
    timeout_seconds: int = 5
) -> Optional[Match[str]]:
    """
    Safe version of re.search with timeout protection.
    """
    if isinstance(pattern, str):
        pattern = re.compile(pattern, flags)
    
    try:
        with timeout(timeout_seconds):
            return pattern.search(string)
    except RegexTimeout:
        return None
    except Exception:
        raise


def validate_regex_safety(pattern: str) -> tuple[bool, str]:
    """
    Validate if a regex pattern is safe from catastrophic backtracking.
    
    Returns:
        (is_safe, warning_message)
    """
    dangerous_patterns = [
        (r'\(.*\)\+', 'Nested quantifiers with .* can cause exponential backtracking'),
        (r'\(.+\)\+', 'Nested quantifiers with .+ can cause exponential backtracking'),
        (r'\(.*\)\*', 'Nested quantifiers with .* can cause exponential backtracking'),
        (r'\(.+\)\*', 'Nested quantifiers with .+ can cause exponential backtracking'),
        (r'(\w+\s*)+\w+', 'Overlapping quantifiers can cause catastrophic backtracking'),
        (r'(\s+\w+)*\s+', 'Overlapping quantifiers with alternation'),
        (r'(a+)+b', 'Nested quantifiers without possessive/atomic groups'),
    ]
    
    for dangerous, message in dangerous_patterns:
        if re.search(dangerous, pattern, re.VERBOSE):
            return False, message
    
    return True, ""


def optimize_regex(pattern: str) -> str:
    """
    Attempt to optimize a regex pattern to prevent catastrophic backtracking.
    """
    # Convert common dangerous patterns to safer alternatives
    optimizations = [
        # Use atomic groups for nested quantifiers
        (r'\((\.[*+])\)\+', r'(?>\1)+'),
        (r'\((\.[*+])\)\*', r'(?>\1)*'),
        
        # Use possessive quantifiers where possible
        (r'(\w+)\+(\s|$)', r'\1++\2'),
        (r'(\w+)\*(\s|$)', r'\1*+\2'),
        
        # Limit repetition ranges
        (r'\{(\d+),\}', r'{{\1,100}}'),  # Cap unlimited ranges at 100
    ]
    
    result = pattern
    for dangerous, safe in optimizations:
        result = re.sub(dangerous, safe, result)
    
    return result


@functools.lru_cache(maxsize=256)
def compile_safe_pattern(pattern: str, flags: int = 0) -> Optional[Pattern[str]]:
    """
    Compile a pattern with safety checks.
    
    Returns None if pattern is deemed unsafe.
    """
    is_safe, warning = validate_regex_safety(pattern)
    
    if not is_safe:
        # Try to optimize the pattern
        optimized = optimize_regex(pattern)
        is_safe, _ = validate_regex_safety(optimized)
        
        if is_safe:
            pattern = optimized
        else:
            # Pattern cannot be made safe
            return None
    
    try:
        return re.compile(pattern, flags)
    except re.error:
        return None