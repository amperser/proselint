"""Optimized check implementations with aggressive caching."""

from __future__ import annotations
import re
from functools import lru_cache
from typing import Iterator, NamedTuple, Optional, Pattern, Dict, Tuple
from collections.abc import Callable

from proselint.registry.checks import Check, CheckResult, Padding


# Global compiled pattern cache
_PATTERN_CACHE: Dict[Tuple[str, int], Pattern[str]] = {}
_COMBINED_PATTERNS: Dict[Tuple[Tuple[str, ...], str, int], Pattern[str]] = {}


@lru_cache(maxsize=2048)
def get_pattern(pattern: str, flags: int = 0) -> Pattern[str]:
    """Get compiled pattern with aggressive caching."""
    key = (pattern, flags)
    if key not in _PATTERN_CACHE:
        _PATTERN_CACHE[key] = re.compile(pattern, flags)
    return _PATTERN_CACHE[key]


def combine_patterns(items: Tuple[str, ...], padding: str, flags: int = 0) -> Pattern[str]:
    """Combine multiple patterns into a single regex for efficiency."""
    key = (items, padding, flags)
    if key not in _COMBINED_PATTERNS:
        if len(items) == 1:
            pattern = padding.format(items[0])
        else:
            # Combine all patterns into a single alternation
            combined = "|".join(f"(?:{item})" for item in items)
            pattern = padding.format(combined)
        _COMBINED_PATTERNS[key] = re.compile(pattern, flags)
    return _COMBINED_PATTERNS[key]


class OptimizedExistence:
    """Optimized existence checker with pattern caching."""
    
    def __init__(self, items: Tuple[str, ...], padding: Padding = Padding.WORDS_IN_TEXT, 
                 exceptions: Tuple[str, ...] = ()):
        self.items = items
        self.padding = padding
        self.exceptions = exceptions
        self._compiled_pattern: Optional[Pattern[str]] = None
        self._compiled_exceptions: list[Pattern[str]] = []
    
    def _get_pattern(self, flags: int) -> Pattern[str]:
        """Get or create the compiled pattern."""
        if self._compiled_pattern is None:
            self._compiled_pattern = combine_patterns(
                self.items, self.padding.value, flags
            )
        return self._compiled_pattern
    
    def _get_exceptions(self, flags: int) -> list[Pattern[str]]:
        """Get compiled exception patterns."""
        if not self._compiled_exceptions and self.exceptions:
            self._compiled_exceptions = [
                get_pattern(exc, flags) for exc in self.exceptions
            ]
        return self._compiled_exceptions
    
    def check(self, text: str, check: Check) -> Iterator[CheckResult]:
        """Optimized check with cached patterns."""
        pattern = self._get_pattern(check.re_flag)
        exceptions = self._get_exceptions(check.re_flag)
        offset = self.padding.to_offset_from(check.offset)
        
        for match in pattern.finditer(text):
            matched_text = match.group(0).strip()
            
            # Skip if matches any exception
            if exceptions and any(exc.search(matched_text) for exc in exceptions):
                continue
            
            yield CheckResult(
                start_pos=match.start() + offset[0],
                end_pos=match.end() + offset[1],
                check_path=check.path,
                message=check.message.format(matched_text),
                replacements=None,
            )


class OptimizedPreferredForms:
    """Optimized preferred forms checker."""
    
    def __init__(self, items: Dict[str, str], padding: Padding = Padding.WORDS_IN_TEXT):
        self.items = items
        self.padding = padding
        self._compiled_pattern: Optional[Pattern[str]] = None
        self._pattern_to_replacement: Dict[str, str] = {}
    
    def _build_pattern(self, flags: int) -> Pattern[str]:
        """Build a single combined pattern for all items."""
        if self._compiled_pattern is None:
            # Sort by length (longest first) to ensure correct matching
            sorted_items = sorted(self.items.keys(), key=len, reverse=True)
            combined = "|".join(f"(?:{re.escape(item)})" for item in sorted_items)
            pattern_str = self.padding.value.format(combined)
            self._compiled_pattern = re.compile(pattern_str, flags)
            
            # Build lookup for replacements
            for wrong, right in self.items.items():
                self._pattern_to_replacement[wrong.lower()] = right
        
        return self._compiled_pattern
    
    def check(self, text: str, check: Check) -> Iterator[CheckResult]:
        """Optimized check with single pattern for all items."""
        pattern = self._build_pattern(check.re_flag)
        offset = self.padding.to_offset_from(check.offset)
        
        for match in pattern.finditer(text):
            matched_text = match.group(0)
            matched_lower = matched_text.lower()
            
            # Find the replacement
            replacement = self._pattern_to_replacement.get(matched_lower)
            if not replacement:
                # Try to find which pattern matched
                for wrong, right in self.items.items():
                    if wrong.lower() in matched_lower:
                        replacement = right
                        break
            
            yield CheckResult(
                start_pos=match.start() + offset[0],
                end_pos=match.end() + offset[1],
                check_path=check.path,
                message=check.message.format(matched_text, replacement),
                replacements=replacement,
            )


# Optimized line boundary calculation
@lru_cache(maxsize=16)
def calculate_line_bounds(text: str) -> Tuple[int, ...]:
    """Calculate line boundaries with caching."""
    lines = []
    pos = 0
    for line in text.splitlines(keepends=True):
        lines.append(pos)
        pos += len(line)
    return tuple(lines)


def find_line_col(position: int, line_bounds: Tuple[int, ...]) -> Tuple[int, int]:
    """Binary search for line and column."""
    if not line_bounds or position < 0:
        return (1, 1)
    
    # Binary search for the line
    left, right = 0, len(line_bounds) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if line_bounds[mid] <= position:
            left = mid
        else:
            right = mid - 1
    
    line = left + 1
    col = position - line_bounds[left] + 1
    return (line, col)