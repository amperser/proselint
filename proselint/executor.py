"""Robust check executor with error isolation and recovery."""

from __future__ import annotations

import multiprocessing as mp
import queue
import signal
import threading
import time
import traceback
from concurrent.futures import Future, ThreadPoolExecutor, TimeoutError
from dataclasses import dataclass
from typing import Any, Callable, Iterator, List, Optional

from proselint.core import CircuitBreaker, ProcessingContext
from proselint.errors import CheckError
from proselint.logger import CheckLogger, get_logger
from proselint.registry.checks import Check, CheckResult

logger = get_logger("executor")


@dataclass
class CheckExecution:
    """Result of check execution."""
    check_path: str
    success: bool
    results: List[CheckResult]
    error: Optional[str] = None
    execution_time: float = 0.0


class IsolatedCheckExecutor:
    """Execute checks in isolated environment with timeout and error handling."""
    
    def __init__(
        self,
        timeout_seconds: int = 10,
        max_retries: int = 2,
        use_process_isolation: bool = False
    ):
        """Initialize executor."""
        self.timeout_seconds = timeout_seconds
        self.max_retries = max_retries
        self.use_process_isolation = use_process_isolation
        self.circuit_breakers: dict[str, CircuitBreaker] = {}
    
    def execute_check(
        self,
        check: Check,
        text: str,
        context: Optional[ProcessingContext] = None
    ) -> CheckExecution:
        """Execute a single check with full error isolation."""
        start_time = time.perf_counter()
        
        # Get or create circuit breaker for this check
        if check.path not in self.circuit_breakers:
            self.circuit_breakers[check.path] = CircuitBreaker(
                failure_threshold=3,
                reset_timeout=300
            )
        
        circuit_breaker = self.circuit_breakers[check.path]
        
        # Check if we should skip this check
        if context and not context.should_run_check(check.path):
            return CheckExecution(
                check_path=check.path,
                success=True,
                results=[],
                execution_time=0.0
            )
        
        # Try executing with circuit breaker
        try:
            results = circuit_breaker.call(
                self._execute_with_timeout,
                check,
                text,
                context
            )
            
            execution_time = time.perf_counter() - start_time
            
            return CheckExecution(
                check_path=check.path,
                success=True,
                results=list(results),
                execution_time=execution_time
            )
            
        except Exception as e:
            execution_time = time.perf_counter() - start_time
            error_msg = f"{type(e).__name__}: {str(e)}"
            
            logger.error(f"Check {check.path} failed: {error_msg}")
            
            return CheckExecution(
                check_path=check.path,
                success=False,
                results=[],
                error=error_msg,
                execution_time=execution_time
            )
    
    def _execute_with_timeout(
        self,
        check: Check,
        text: str,
        context: Optional[ProcessingContext]
    ) -> Iterator[CheckResult]:
        """Execute check with timeout."""
        if self.use_process_isolation:
            return self._execute_in_process(check, text)
        else:
            return self._execute_in_thread(check, text)
    
    def _execute_in_thread(
        self,
        check: Check,
        text: str
    ) -> Iterator[CheckResult]:
        """Execute check in thread with timeout."""
        results = []
        exception = None
        
        def worker():
            nonlocal results, exception
            try:
                with CheckLogger(check.path):
                    results = list(check.check_with_flags(text))
            except Exception as e:
                exception = e
        
        thread = threading.Thread(target=worker)
        thread.daemon = True
        thread.start()
        thread.join(timeout=self.timeout_seconds)
        
        if thread.is_alive():
            # Thread is still running - timeout
            raise TimeoutError(f"Check {check.path} timed out after {self.timeout_seconds}s")
        
        if exception:
            raise exception
        
        return iter(results)
    
    def _execute_in_process(
        self,
        check: Check,
        text: str
    ) -> Iterator[CheckResult]:
        """Execute check in separate process with timeout."""
        # This provides stronger isolation but is slower
        ctx = mp.get_context('spawn')
        result_queue = ctx.Queue()
        
        def worker(check, text, queue):
            try:
                results = list(check.check_with_flags(text))
                queue.put(('success', results))
            except Exception as e:
                queue.put(('error', str(e)))
        
        process = ctx.Process(target=worker, args=(check, text, result_queue))
        process.start()
        process.join(timeout=self.timeout_seconds)
        
        if process.is_alive():
            process.terminate()
            process.join(timeout=1)
            if process.is_alive():
                process.kill()
            raise TimeoutError(f"Check {check.path} timed out after {self.timeout_seconds}s")
        
        try:
            status, data = result_queue.get_nowait()
            if status == 'error':
                raise CheckError(check.path, data)
            return iter(data)
        except queue.Empty:
            return iter([])


class ParallelCheckExecutor:
    """Execute multiple checks in parallel with robust error handling."""
    
    def __init__(
        self,
        max_workers: Optional[int] = None,
        timeout_per_check: int = 10,
        use_process_pool: bool = False
    ):
        """Initialize parallel executor."""
        self.max_workers = max_workers or mp.cpu_count()
        self.timeout_per_check = timeout_per_check
        self.use_process_pool = use_process_pool
        self.isolated_executor = IsolatedCheckExecutor(
            timeout_seconds=timeout_per_check,
            use_process_isolation=use_process_pool
        )
    
    def execute_checks(
        self,
        checks: List[Check],
        text: str,
        context: Optional[ProcessingContext] = None,
        progress_callback: Optional[Callable[[int, int], None]] = None
    ) -> Iterator[CheckExecution]:
        """Execute multiple checks in parallel."""
        total_checks = len(checks)
        completed = 0
        
        # Filter checks based on context
        if context:
            checks = [c for c in checks if context.should_run_check(c.path)]
        
        if not checks:
            return
        
        # Use thread pool for parallel execution
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Submit all checks
            futures: dict[Future, Check] = {
                executor.submit(
                    self.isolated_executor.execute_check,
                    check,
                    text,
                    context
                ): check
                for check in checks
            }
            
            # Process results as they complete
            for future in futures:
                check = futures[future]
                
                try:
                    execution = future.result(timeout=self.timeout_per_check * 2)
                    yield execution
                    
                except Exception as e:
                    # Even if the future fails, return an execution result
                    yield CheckExecution(
                        check_path=check.path,
                        success=False,
                        results=[],
                        error=str(e),
                        execution_time=0.0
                    )
                
                finally:
                    completed += 1
                    if progress_callback:
                        progress_callback(completed, total_checks)


class CheckScheduler:
    """Smart scheduler for check execution based on priority and dependencies."""
    
    # Priority levels for different check types
    PRIORITIES = {
        'spelling': 1,
        'grammar': 1,
        'typography': 2,
        'consistency': 3,
        'style': 4,
        'misc': 5,
    }
    
    def __init__(self):
        """Initialize scheduler."""
        self.execution_stats: dict[str, float] = {}
    
    def schedule_checks(
        self,
        checks: List[Check],
        context: Optional[ProcessingContext] = None
    ) -> List[Check]:
        """
        Schedule checks in optimal order.
        
        Returns checks ordered by:
        1. Priority (critical checks first)
        2. Historical execution time (fast checks first)
        3. Alphabetical (for determinism)
        """
        def get_priority(check: Check) -> tuple[int, float, str]:
            # Get category priority
            category = check.path.split('.')[0] if '.' in check.path else check.path
            priority = self.PRIORITIES.get(category, 10)
            
            # Get historical execution time
            exec_time = self.execution_stats.get(check.path, 1.0)
            
            # Return sort key
            return (priority, exec_time, check.path)
        
        # Filter checks if context provided
        if context:
            checks = [c for c in checks if context.should_run_check(c.path)]
        
        # Sort by priority
        return sorted(checks, key=get_priority)
    
    def update_stats(self, execution: CheckExecution) -> None:
        """Update execution statistics."""
        if execution.success:
            # Use exponential moving average
            alpha = 0.3
            old_time = self.execution_stats.get(execution.check_path, execution.execution_time)
            new_time = alpha * execution.execution_time + (1 - alpha) * old_time
            self.execution_stats[execution.check_path] = new_time


class ResilientProcessor:
    """Main processor with full resilience and recovery capabilities."""
    
    def __init__(
        self,
        parallel: bool = True,
        max_workers: Optional[int] = None,
        timeout_per_check: int = 10,
        cache_results: bool = True
    ):
        """Initialize resilient processor."""
        self.parallel = parallel
        self.scheduler = CheckScheduler()
        
        if parallel:
            self.executor = ParallelCheckExecutor(
                max_workers=max_workers,
                timeout_per_check=timeout_per_check
            )
        else:
            self.executor = IsolatedCheckExecutor(
                timeout_seconds=timeout_per_check
            )
        
        self.cache_results = cache_results
        
        if cache_results:
            from proselint.core import ResultCache
            self.cache = ResultCache()
        else:
            self.cache = None
    
    def process(
        self,
        text: str,
        checks: List[Check],
        context: ProcessingContext,
        progress_callback: Optional[Callable[[int, int], None]] = None
    ) -> List[CheckResult]:
        """Process text with all checks, handling errors gracefully."""
        # Check cache if enabled
        if self.cache and context.metadata:
            cached = self.cache.get(context.metadata.hash)
            if cached is not None:
                logger.info(f"Using cached results for {context.metadata.path}")
                return cached
        
        # Schedule checks optimally
        scheduled_checks = self.scheduler.schedule_checks(checks, context)
        
        all_results = []
        failed_checks = []
        
        # Execute checks
        if self.parallel and isinstance(self.executor, ParallelCheckExecutor):
            executions = self.executor.execute_checks(
                scheduled_checks,
                text,
                context,
                progress_callback
            )
        else:
            # Sequential execution
            executions = []
            for i, check in enumerate(scheduled_checks):
                execution = self.executor.execute_check(check, text, context)
                executions.append(execution)
                
                if progress_callback:
                    progress_callback(i + 1, len(scheduled_checks))
        
        # Process results
        for execution in executions:
            self.scheduler.update_stats(execution)
            
            if execution.success:
                all_results.extend(execution.results)
            else:
                failed_checks.append(execution.check_path)
                logger.warning(
                    f"Check {execution.check_path} failed: {execution.error}"
                )
            
            # Respect max_errors limit
            if len(all_results) >= context.max_errors:
                logger.info(f"Reached max_errors limit ({context.max_errors})")
                break
        
        # Log summary
        if failed_checks:
            logger.warning(f"Failed checks: {', '.join(failed_checks)}")
        
        # Cache results if enabled
        if self.cache and context.metadata:
            self.cache.set(context.metadata.hash, all_results)
        
        return all_results