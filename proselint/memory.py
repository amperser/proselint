"""Memory management utilities for proselint."""

import gc
import mmap
import os
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, Optional, Union

from proselint.errors import ProselintError


class MemoryEfficientFileReader:
    """Memory-efficient file reader for large files."""
    
    # Thresholds for different reading strategies
    SMALL_FILE_SIZE = 1024 * 1024  # 1MB
    MEDIUM_FILE_SIZE = 10 * 1024 * 1024  # 10MB
    LARGE_FILE_SIZE = 100 * 1024 * 1024  # 100MB
    
    def __init__(self, filepath: Union[str, Path]):
        """Initialize the reader with a file path."""
        self.filepath = Path(filepath) if isinstance(filepath, str) else filepath
        
        if not self.filepath.exists():
            raise ProselintError(f"File not found: {self.filepath}")
        
        if not self.filepath.is_file():
            raise ProselintError(f"Not a file: {self.filepath}")
        
        self.file_size = self.filepath.stat().st_size
    
    def read(self) -> str:
        """Read the file using the most appropriate method based on size."""
        if self.file_size <= self.SMALL_FILE_SIZE:
            return self._read_small()
        elif self.file_size <= self.MEDIUM_FILE_SIZE:
            return self._read_medium()
        elif self.file_size <= self.LARGE_FILE_SIZE:
            return self._read_large()
        else:
            return self._read_mmap()
    
    def _read_small(self) -> str:
        """Read small files directly into memory."""
        try:
            return self.filepath.read_text(encoding='utf-8')
        except (IOError, OSError) as e:
            raise ProselintError(f"Failed to read file {self.filepath}: {e}")
    
    def _read_medium(self) -> str:
        """Read medium files with buffering."""
        try:
            with open(self.filepath, 'r', encoding='utf-8', buffering=8192) as f:
                return f.read()
        except (IOError, OSError) as e:
            raise ProselintError(f"Failed to read file {self.filepath}: {e}")
    
    def _read_large(self) -> str:
        """Read large files in chunks."""
        chunks = []
        try:
            with open(self.filepath, 'r', encoding='utf-8', buffering=65536) as f:
                while True:
                    chunk = f.read(65536)
                    if not chunk:
                        break
                    chunks.append(chunk)
            return ''.join(chunks)
        except (IOError, OSError) as e:
            raise ProselintError(f"Failed to read file {self.filepath}: {e}")
        finally:
            # Explicitly release memory from chunks
            del chunks
            gc.collect()
    
    def _read_mmap(self) -> str:
        """Read very large files using memory mapping."""
        try:
            with open(self.filepath, 'rb') as f:
                with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                    # Decode in chunks to avoid memory spike
                    text = mm.read().decode('utf-8', errors='replace')
                    return text
        except (IOError, OSError) as e:
            raise ProselintError(f"Failed to memory-map file {self.filepath}: {e}")
    
    def read_lines(self, max_lines: Optional[int] = None) -> Iterator[str]:
        """Read file line by line for memory efficiency."""
        try:
            with open(self.filepath, 'r', encoding='utf-8', buffering=8192) as f:
                line_count = 0
                for line in f:
                    yield line
                    line_count += 1
                    if max_lines and line_count >= max_lines:
                        break
        except (IOError, OSError) as e:
            raise ProselintError(f"Failed to read lines from {self.filepath}: {e}")


@contextmanager
def memory_efficient_context(threshold_mb: float = 100):
    """Context manager for memory-intensive operations.
    
    Args:
        threshold_mb: Memory threshold in megabytes to trigger cleanup
    
    Yields:
        None
    """
    import psutil
    
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    try:
        yield
    finally:
        current_memory = process.memory_info().rss / 1024 / 1024  # MB
        memory_increase = current_memory - initial_memory
        
        if memory_increase > threshold_mb:
            # Force garbage collection for large memory increases
            gc.collect()
            # For very large increases, do a full collection
            if memory_increase > threshold_mb * 2:
                gc.collect(2)


class ChunkedTextProcessor:
    """Process text in chunks to avoid memory issues."""
    
    def __init__(self, text: str, chunk_size: int = 1024 * 1024):
        """Initialize with text and chunk size."""
        self.text = text
        self.chunk_size = chunk_size
    
    def process_chunks(self, processor_func):
        """Process text in chunks with a given function.
        
        Args:
            processor_func: Function that takes a text chunk and returns results
        
        Yields:
            Results from processing each chunk
        """
        text_len = len(self.text)
        offset = 0
        
        while offset < text_len:
            # Find a good break point (e.g., newline)
            end = min(offset + self.chunk_size, text_len)
            
            # If not at the end, try to break at a newline
            if end < text_len:
                newline_pos = self.text.rfind('\n', offset, end)
                if newline_pos > offset:
                    end = newline_pos + 1
            
            chunk = self.text[offset:end]
            
            # Process the chunk
            result = processor_func(chunk)
            if result:
                yield result
            
            offset = end
            
            # Hint to garbage collector after each chunk
            if offset < text_len:
                gc.collect(0)


def estimate_memory_usage(text: str) -> dict[str, float]:
    """Estimate memory usage for processing text.
    
    Args:
        text: Text to analyze
    
    Returns:
        Dictionary with memory estimates in MB
    """
    text_size_mb = len(text.encode('utf-8')) / 1024 / 1024
    
    estimates = {
        'text_size': text_size_mb,
        'estimated_peak': text_size_mb * 3,  # Conservative estimate
        'recommended_available': text_size_mb * 5,
    }
    
    try:
        import psutil
        available_mb = psutil.virtual_memory().available / 1024 / 1024
        estimates['available_memory'] = available_mb
        estimates['memory_sufficient'] = available_mb > estimates['recommended_available']
    except ImportError:
        pass
    
    return estimates