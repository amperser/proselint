#!/usr/bin/env python3
"""Ultra-fast command line interface for proselint using multiprocessing."""

import json
import sys
from pathlib import Path
from multiprocessing import Pool, cpu_count
from typing import List, Tuple

import click

from proselint.checks import __register__
from proselint.config import load_from
from proselint.registry import CheckRegistry
from proselint.tools import LintFile, extract_files
from proselint.version import __version__


# Global registry to be shared across processes
_registry = None


def init_worker():
    """Initialize worker process with pre-loaded registry."""
    global _registry
    _registry = CheckRegistry()
    _registry.register_many(__register__)


def lint_file_worker(args: Tuple[Path, dict]) -> Tuple[str, List]:
    """Worker function to lint a single file."""
    filepath, config = args
    try:
        lint_file = LintFile(filepath)
        results = lint_file.lint(config)
        return str(filepath), results
    except Exception as e:
        return str(filepath), []


@click.command()
@click.version_option(__version__, '--version', '-v', message='%(version)s')
@click.option('--config', type=click.Path(exists=True, path_type=Path),
              help="Path to configuration file.")
@click.option('--json', '-j', 'output_json', is_flag=True,
              help="Output as JSON.")
@click.option('--compact', is_flag=True, help="Shorten output.")
@click.option('--parallel/--no-parallel', default=True,
              help="Use parallel processing (default: enabled)")
@click.option('--workers', '-w', type=int, default=None,
              help="Number of parallel workers (default: CPU count)")
@click.argument('paths', nargs=-1, type=click.Path(exists=True, path_type=Path))
def fast_lint(paths, config=None, output_json=False, compact=False, 
              parallel=True, workers=None):
    """Fast parallel linter for prose."""
    config = load_from(config)
    
    # Get files to lint
    if len(paths) == 0:
        # stdin mode
        CheckRegistry().register_many(__register__)
        lint_file = LintFile.from_stdin()
        results = lint_file.lint(config)
        lint_file.output_errors(results, output_json=output_json, compact=compact)
        sys.exit(int(len(results) > 0))
    
    lint_files = list(extract_files(paths))
    
    if not parallel or len(lint_files) <= 1:
        # Sequential processing
        CheckRegistry().register_many(__register__)
        num_errors = 0
        for filepath in lint_files:
            lint_file = LintFile(filepath)
            results = lint_file.lint(config)
            num_errors += len(results)
            lint_file.output_errors(results, output_json=output_json, compact=compact)
        sys.exit(int(num_errors > 0))
    
    # Parallel processing
    if workers is None:
        workers = min(cpu_count(), len(lint_files))
    
    # Prepare arguments for workers
    work_items = [(filepath, config) for filepath in lint_files]
    
    # Process files in parallel
    num_errors = 0
    with Pool(processes=workers, initializer=init_worker) as pool:
        for filepath, results in pool.imap_unordered(lint_file_worker, work_items):
            num_errors += len(results)
            
            if output_json:
                print(json.dumps({
                    "file": filepath,
                    "errors": [r._asdict() for r in results]
                }))
            else:
                for result in results:
                    name = "-" if compact else filepath
                    print(f"{name}{result}")
    
    sys.exit(int(num_errors > 0))


if __name__ == '__main__':
    fast_lint()