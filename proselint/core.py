"""Core functionality for proselint with robust error handling."""

from __future__ import annotations

import hashlib
import mmap
import os
import sys
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from typing import Any, Iterator, Optional, Union

from proselint.errors import FileProcessingError, ProselintError
from proselint.logger import get_logger

logger = get_logger("core")


class FileType(Enum):
    """Supported file types."""
    PLAIN_TEXT = auto()
    MARKDOWN = auto()
    LATEX = auto()
    HTML = auto()
    RST = auto()
    UNKNOWN = auto()


class ProcessingMode(Enum):
    """Processing modes for different performance/quality tradeoffs."""
    FAST = auto()      # Skip expensive checks
    NORMAL = auto()    # Default mode
    THOROUGH = auto()  # Run all checks including expensive ones


@dataclass
class FileMetadata:
    """Metadata about a file being processed."""
    path: Path
    size: int
    hash: str
    file_type: FileType
    encoding: str = "utf-8"
    line_count: int = 0
    word_count: int = 0
    
    @classmethod
    def from_path(cls, path: Path) -> FileMetadata:
        """Create metadata from file path."""
        if not path.exists():
            raise FileProcessingError(str(path), "File does not exist")
        
        stat = path.stat()
        file_type = detect_file_type(path)
        
        # Calculate hash for caching
        with open(path, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
        
        # Count lines and words efficiently
        line_count = 0
        word_count = 0
        
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line in f:
                    line_count += 1
                    word_count += len(line.split())
        except UnicodeDecodeError:
            # Try with latin-1 as fallback
            try:
                with open(path, 'r', encoding='latin-1') as f:
                    for line in f:
                        line_count += 1
                        word_count += len(line.split())
                    encoding = 'latin-1'
            except Exception as e:
                raise FileProcessingError(str(path), f"Cannot read file: {e}")
        
        return cls(
            path=path,
            size=stat.st_size,
            hash=file_hash,
            file_type=file_type,
            encoding='utf-8',
            line_count=line_count,
            word_count=word_count
        )


def detect_file_type(path: Path) -> FileType:
    """Detect file type from extension and content."""
    suffix = path.suffix.lower()
    
    type_map = {
        '.md': FileType.MARKDOWN,
        '.markdown': FileType.MARKDOWN,
        '.tex': FileType.LATEX,
        '.html': FileType.HTML,
        '.htm': FileType.HTML,
        '.rst': FileType.RST,
        '.txt': FileType.PLAIN_TEXT,
    }
    
    return type_map.get(suffix, FileType.UNKNOWN)


class SafeFileReader:
    """Safe file reader with memory mapping for large files."""
    
    LARGE_FILE_THRESHOLD = 10 * 1024 * 1024  # 10MB
    
    def __init__(self, path: Path, encoding: str = 'utf-8'):
        """Initialize safe file reader."""
        self.path = path
        self.encoding = encoding
        self._content: Optional[str] = None
        self._mmap: Optional[mmap.mmap] = None
        self._file = None
        
    def __enter__(self):
        """Enter context manager."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit context manager."""
        self.close()
    
    def read(self) -> str:
        """Read file content safely."""
        if self._content is not None:
            return self._content
        
        file_size = self.path.stat().st_size
        
        if file_size > self.LARGE_FILE_THRESHOLD:
            # Use memory mapping for large files
            return self._read_mmap()
        else:
            # Regular read for small files
            return self._read_normal()
    
    def _read_normal(self) -> str:
        """Read file normally."""
        try:
            with open(self.path, 'r', encoding=self.encoding) as f:
                self._content = f.read()
                return self._content
        except UnicodeDecodeError:
            # Fallback to binary mode and detect encoding
            with open(self.path, 'rb') as f:
                raw = f.read()
                # Try common encodings
                for enc in ['utf-8', 'latin-1', 'cp1252', 'ascii']:
                    try:
                        self._content = raw.decode(enc)
                        self.encoding = enc
                        return self._content
                    except UnicodeDecodeError:
                        continue
                
                # Last resort - ignore errors
                self._content = raw.decode('utf-8', errors='ignore')
                return self._content
    
    def _read_mmap(self) -> str:
        """Read file using memory mapping."""
        self._file = open(self.path, 'rb')
        self._mmap = mmap.mmap(self._file.fileno(), 0, access=mmap.ACCESS_READ)
        
        try:
            self._content = self._mmap.read().decode(self.encoding)
        except UnicodeDecodeError:
            # Fallback decoding
            self._content = self._mmap.read().decode('utf-8', errors='ignore')
        
        return self._content
    
    def close(self):
        """Clean up resources."""
        if self._mmap:
            self._mmap.close()
            self._mmap = None
        if self._file:
            self._file.close()
            self._file = None


@dataclass
class ProcessingContext:
    """Context for processing with all necessary information."""
    content: str
    metadata: FileMetadata
    mode: ProcessingMode = ProcessingMode.NORMAL
    max_errors: int = 1000
    checks_to_skip: set[str] = field(default_factory=set)
    checks_to_run: set[str] = field(default_factory=set)
    
    @property
    def should_skip_expensive_checks(self) -> bool:
        """Check if expensive checks should be skipped."""
        return self.mode == ProcessingMode.FAST or self.metadata.size > 1024 * 1024
    
    def should_run_check(self, check_path: str) -> bool:
        """Determine if a check should run."""
        if check_path in self.checks_to_skip:
            return False
        
        if self.checks_to_run and check_path not in self.checks_to_run:
            return False
        
        # Skip expensive checks in fast mode
        expensive_checks = {
            'lexical_illusions',
            'misc.debased',
            'consistency.spelling',
        }
        
        if self.should_skip_expensive_checks and check_path in expensive_checks:
            logger.debug(f"Skipping expensive check: {check_path}")
            return False
        
        return True


class ResultCache:
    """Cache for lint results to avoid reprocessing."""
    
    def __init__(self, cache_dir: Optional[Path] = None):
        """Initialize result cache."""
        if cache_dir is None:
            cache_dir = Path.home() / '.cache' / 'proselint'
        
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self._memory_cache: dict[str, Any] = {}
    
    def get(self, file_hash: str) -> Optional[list]:
        """Get cached results for file hash."""
        # Check memory cache first
        if file_hash in self._memory_cache:
            logger.debug(f"Memory cache hit for {file_hash}")
            return self._memory_cache[file_hash]
        
        # Check disk cache
        cache_file = self.cache_dir / f"{file_hash}.json"
        if cache_file.exists():
            try:
                import json
                with open(cache_file, 'r') as f:
                    results = json.load(f)
                    self._memory_cache[file_hash] = results
                    logger.debug(f"Disk cache hit for {file_hash}")
                    return results
            except Exception as e:
                logger.warning(f"Failed to load cache: {e}")
        
        return None
    
    def set(self, file_hash: str, results: list) -> None:
        """Cache results for file hash."""
        # Update memory cache
        self._memory_cache[file_hash] = results
        
        # Update disk cache
        cache_file = self.cache_dir / f"{file_hash}.json"
        try:
            import json
            with open(cache_file, 'w') as f:
                json.dump(results, f)
            logger.debug(f"Cached results for {file_hash}")
        except Exception as e:
            logger.warning(f"Failed to save cache: {e}")
    
    def clear(self) -> None:
        """Clear all caches."""
        self._memory_cache.clear()
        
        # Clear disk cache
        for cache_file in self.cache_dir.glob("*.json"):
            try:
                cache_file.unlink()
            except Exception:
                pass
        
        logger.info("Cache cleared")


def validate_input(text: str, max_size: int = 10 * 1024 * 1024) -> str:
    """
    Validate and sanitize input text.
    
    Args:
        text: Input text to validate
        max_size: Maximum allowed size in bytes
    
    Returns:
        Sanitized text
    
    Raises:
        ProselintError: If input is invalid
    """
    if not isinstance(text, str):
        raise ProselintError("Input must be a string")
    
    # Check size
    if len(text.encode('utf-8')) > max_size:
        raise ProselintError(f"Input exceeds maximum size of {max_size} bytes")
    
    # Remove null bytes
    text = text.replace('\0', '')
    
    # Normalize line endings
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    return text


class CircuitBreaker:
    """Circuit breaker pattern for handling failures gracefully."""
    
    def __init__(self, failure_threshold: int = 5, reset_timeout: int = 60):
        """Initialize circuit breaker."""
        self.failure_threshold = failure_threshold
        self.reset_timeout = reset_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.is_open = False
    
    def call(self, func, *args, **kwargs):
        """Call function with circuit breaker protection."""
        import time
        
        # Check if circuit should be reset
        if self.is_open and self.last_failure_time:
            if time.time() - self.last_failure_time > self.reset_timeout:
                self.reset()
        
        # If circuit is open, fail fast
        if self.is_open:
            raise ProselintError("Circuit breaker is open - too many failures")
        
        try:
            result = func(*args, **kwargs)
            # Success - reset failure count
            self.failure_count = 0
            return result
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            if self.failure_count >= self.failure_threshold:
                self.is_open = True
                logger.error(f"Circuit breaker opened after {self.failure_count} failures")
            
            raise e
    
    def reset(self):
        """Reset circuit breaker."""
        self.failure_count = 0
        self.is_open = False
        self.last_failure_time = None
        logger.info("Circuit breaker reset")