"""Parallel processing utilities for proselint."""

import multiprocessing as mp
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, Iterator, List, Optional, TypeVar

from proselint.registry.checks import Check, CheckResult

T = TypeVar('T')


class ParallelProcessor:
    """Process checks in parallel for improved performance."""
    
    def __init__(self, max_workers: Optional[int] = None):
        """Initialize parallel processor."""
        self.max_workers = max_workers or mp.cpu_count()
    
    def process_checks(
        self, 
        text: str, 
        checks: List[Check],
        parallel: bool = True
    ) -> Iterator[CheckResult]:
        """Process multiple checks in parallel."""
        if not parallel or len(checks) <= 2:
            # Sequential processing for small number of checks
            for check in checks:
                yield from check.check_with_flags(text)
            return
        
        # Parallel processing using ThreadPoolExecutor
        with ThreadPoolExecutor(max_workers=min(self.max_workers, len(checks))) as executor:
            # Submit all checks
            futures = {
                executor.submit(check.check_with_flags, text): check
                for check in checks
            }
            
            # Yield results as they complete
            for future in as_completed(futures):
                try:
                    results = future.result(timeout=10)
                    yield from results
                except Exception as e:
                    # Log error but continue processing
                    check = futures[future]
                    print(f"Error in check {check.path}: {e}")
    
    def batch_process_files(
        self,
        files: List[str],
        processor: Callable[[str], T],
        parallel: bool = True
    ) -> Iterator[tuple[str, T]]:
        """Process multiple files in parallel."""
        if not parallel or len(files) <= 1:
            # Sequential processing
            for file in files:
                yield file, processor(file)
            return
        
        # Parallel file processing
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(processor, file): file
                for file in files
            }
            
            for future in as_completed(futures):
                file = futures[future]
                try:
                    result = future.result(timeout=30)
                    yield file, result
                except Exception as e:
                    print(f"Error processing {file}: {e}")
                    yield file, None