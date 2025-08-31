#!/usr/bin/env python3
"""Modern, robust CLI for proselint with enhanced features."""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from typing import List, Optional

import click
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich import print as rprint

from proselint import __version__
from proselint.checks import __register__
from proselint.config import load_from
from proselint.core import (
    FileMetadata,
    FileType,
    ProcessingContext,
    ProcessingMode,
    ResultCache,
    SafeFileReader,
    validate_input
)
from proselint.executor import ResilientProcessor
from proselint.logger import setup_logging, get_logger
from proselint.registry import CheckRegistry
from proselint.tools import LintFile, extract_files

console = Console()
logger = get_logger("cli")


class OutputFormatter:
    """Format output in various styles."""
    
    def __init__(self, format_type: str = "text"):
        """Initialize formatter."""
        self.format_type = format_type
    
    def format_results(self, results: list, filename: str = "-") -> str:
        """Format lint results."""
        if self.format_type == "json":
            return json.dumps({
                "file": filename,
                "errors": [r._asdict() for r in results]
            }, indent=2)
        
        elif self.format_type == "github":
            # GitHub Actions format
            lines = []
            for r in results:
                level = "warning" if r.severity == "warning" else "error"
                lines.append(
                    f"::{level} file={filename},line={r.line},col={r.column}::"
                    f"{r.check_path}: {r.message}"
                )
            return "\n".join(lines)
        
        elif self.format_type == "compact":
            lines = []
            for r in results:
                lines.append(f"{r.line}:{r.column}: {r.message}")
            return "\n".join(lines)
        
        else:  # Default text format
            lines = []
            for r in results:
                lines.append(
                    f"{filename}:{r.line}:{r.column}: "
                    f"{r.check_path} {r.message}"
                )
            return "\n".join(lines)


class InteractiveMode:
    """Interactive mode for proselint."""
    
    def __init__(self):
        """Initialize interactive mode."""
        self.processor = ResilientProcessor(parallel=False)
        self.registry = CheckRegistry()
        self.registry.register_many(__register__)
    
    def run(self):
        """Run interactive mode."""
        console.print(
            Panel.fit(
                f"[bold cyan]Proselint Interactive Mode v{__version__}[/]\n"
                "Type text and press Ctrl+D to check, or Ctrl+C to exit",
                border_style="cyan"
            )
        )
        
        while True:
            try:
                # Read input
                console.print("\n[bold green]Enter text:[/]")
                lines = []
                while True:
                    try:
                        line = input()
                        lines.append(line)
                    except EOFError:
                        break
                
                if not lines:
                    continue
                
                text = "\n".join(lines)
                
                # Process text
                with console.status("[cyan]Analyzing text...[/]"):
                    context = ProcessingContext(
                        content=text,
                        metadata=FileMetadata(
                            path=Path("<stdin>"),
                            size=len(text),
                            hash="",
                            file_type=FileType.PLAIN_TEXT
                        ),
                        mode=ProcessingMode.NORMAL
                    )
                    
                    checks = self.registry.get_all_enabled()
                    results = self.processor.process(text, checks, context)
                
                # Display results
                if results:
                    table = Table(title="Issues Found", show_header=True)
                    table.add_column("Line", style="cyan")
                    table.add_column("Column", style="cyan")
                    table.add_column("Type", style="yellow")
                    table.add_column("Message", style="white")
                    
                    for r in results:
                        table.add_row(
                            str(r.line),
                            str(r.column),
                            r.check_path.split('.')[-1],
                            r.message
                        )
                    
                    console.print(table)
                else:
                    console.print("[green]✓ No issues found![/]")
                
            except KeyboardInterrupt:
                console.print("\n[yellow]Exiting...[/]")
                break
            except Exception as e:
                console.print(f"[red]Error: {e}[/]")


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__, '--version', '-v')
@click.option('--config', '-c', type=click.Path(exists=True, path_type=Path),
              help='Configuration file path')
@click.option('--output', '-o', type=click.Choice(['text', 'json', 'github', 'compact']),
              default='text', help='Output format')
@click.option('--mode', '-m', type=click.Choice(['fast', 'normal', 'thorough']),
              default='normal', help='Processing mode')
@click.option('--quiet', '-q', is_flag=True, help='Minimal output')
@click.option('--verbose', '-V', is_flag=True, help='Verbose output')
@click.option('--debug', is_flag=True, help='Debug mode')
@click.option('--no-cache', is_flag=True, help='Disable result caching')
@click.option('--clear-cache', is_flag=True, help='Clear result cache')
@click.option('--parallel/--no-parallel', default=True,
              help='Enable/disable parallel processing')
@click.option('--workers', '-w', type=int, default=None,
              help='Number of parallel workers')
@click.option('--interactive', '-i', is_flag=True, help='Interactive mode')
@click.option('--stats', is_flag=True, help='Show statistics')
@click.option('--list-checks', is_flag=True, help='List available checks')
@click.option('--enable-check', multiple=True, help='Enable specific check')
@click.option('--disable-check', multiple=True, help='Disable specific check')
@click.option('--max-errors', type=int, default=1000,
              help='Maximum number of errors to report')
@click.option('--timeout', type=int, default=10,
              help='Timeout per check in seconds')
@click.argument('paths', nargs=-1, type=click.Path(exists=True, path_type=Path))
def main(
    paths: tuple[Path, ...],
    config: Optional[Path],
    output: str,
    mode: str,
    quiet: bool,
    verbose: bool,
    debug: bool,
    no_cache: bool,
    clear_cache: bool,
    parallel: bool,
    workers: Optional[int],
    interactive: bool,
    stats: bool,
    list_checks: bool,
    enable_check: tuple[str, ...],
    disable_check: tuple[str, ...],
    max_errors: int,
    timeout: int
) -> None:
    """
    Proselint - A linter for prose.
    
    Rock-solid prose checking with comprehensive error handling.
    """
    # Setup logging
    log_level = "DEBUG" if debug else ("INFO" if verbose else "WARNING")
    setup_logging(level=log_level, verbose=verbose)
    
    # Handle special modes
    if interactive:
        interactive_mode = InteractiveMode()
        interactive_mode.run()
        return
    
    if clear_cache:
        cache = ResultCache()
        cache.clear()
        console.print("[green]✓ Cache cleared[/]")
        return
    
    # Load configuration
    config_data = load_from(config)
    
    # Initialize registry
    registry = CheckRegistry()
    registry.register_many(__register__)
    
    if list_checks:
        # List all available checks
        checks = registry.get_all_enabled(config_data["checks"])
        table = Table(title="Available Checks", show_header=True)
        table.add_column("Check", style="cyan")
        table.add_column("Enabled", style="green")
        
        for check in sorted(checks, key=lambda c: c.path):
            enabled = "✓" if check.path not in disable_check else "✗"
            table.add_row(check.path, enabled)
        
        console.print(table)
        return
    
    # Process files
    if not paths:
        # Read from stdin
        text = sys.stdin.read()
        process_text(
            text, "<stdin>", config_data, output, mode,
            parallel, workers, no_cache, enable_check,
            disable_check, max_errors, timeout, quiet, stats
        )
    else:
        # Process files
        all_files = list(extract_files(paths))
        
        if not quiet and len(all_files) > 1:
            console.print(f"[cyan]Processing {len(all_files)} files...[/]")
        
        total_errors = 0
        file_count = 0
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            console=console,
            disable=quiet or len(all_files) <= 1
        ) as progress:
            
            task = progress.add_task(
                "[cyan]Checking files...", total=len(all_files)
            )
            
            for filepath in all_files:
                progress.update(task, description=f"[cyan]Checking {filepath.name}...")
                
                try:
                    with SafeFileReader(filepath) as reader:
                        text = reader.read()
                    
                    errors = process_text(
                        text, str(filepath), config_data, output, mode,
                        parallel, workers, no_cache, enable_check,
                        disable_check, max_errors, timeout, quiet, stats
                    )
                    
                    total_errors += errors
                    file_count += 1
                    
                except Exception as e:
                    logger.error(f"Failed to process {filepath}: {e}")
                    if not quiet:
                        console.print(f"[red]✗ Error processing {filepath}: {e}[/]")
                
                progress.advance(task)
        
        # Summary
        if not quiet and file_count > 1:
            console.print(
                f"\n[bold]Summary:[/] Checked {file_count} files, "
                f"found {total_errors} issues"
            )
    
    # Exit with appropriate code
    sys.exit(1 if total_errors > 0 else 0)


def process_text(
    text: str,
    filename: str,
    config: dict,
    output_format: str,
    mode: str,
    parallel: bool,
    workers: Optional[int],
    no_cache: bool,
    enable_check: tuple[str, ...],
    disable_check: tuple[str, ...],
    max_errors: int,
    timeout: int,
    quiet: bool,
    show_stats: bool
) -> int:
    """Process a single text and return error count."""
    # Validate input
    try:
        text = validate_input(text)
    except Exception as e:
        logger.error(f"Invalid input: {e}")
        return 0
    
    # Create processing context
    processing_mode = ProcessingMode[mode.upper()]
    
    metadata = FileMetadata(
        path=Path(filename),
        size=len(text),
        hash="",
        file_type=FileType.PLAIN_TEXT,
        line_count=text.count('\n') + 1,
        word_count=len(text.split())
    )
    
    context = ProcessingContext(
        content=text,
        metadata=metadata,
        mode=processing_mode,
        max_errors=max_errors,
        checks_to_skip=set(disable_check),
        checks_to_run=set(enable_check) if enable_check else set()
    )
    
    # Initialize processor
    processor = ResilientProcessor(
        parallel=parallel,
        max_workers=workers,
        timeout_per_check=timeout,
        cache_results=not no_cache
    )
    
    # Get checks
    registry = CheckRegistry()
    checks = registry.get_all_enabled(config["checks"])
    
    # Process
    start_time = time.perf_counter()
    results = processor.process(text, checks, context)
    elapsed = time.perf_counter() - start_time
    
    # Format and output results
    formatter = OutputFormatter(output_format)
    output = formatter.format_results(results, filename)
    
    if output and not quiet:
        console.print(output)
    
    # Show statistics if requested
    if show_stats and not quiet:
        stats_table = Table(title="Processing Statistics", show_header=False)
        stats_table.add_column("Metric", style="cyan")
        stats_table.add_column("Value", style="white")
        
        stats_table.add_row("File", filename)
        stats_table.add_row("Size", f"{metadata.size:,} bytes")
        stats_table.add_row("Lines", f"{metadata.line_count:,}")
        stats_table.add_row("Words", f"{metadata.word_count:,}")
        stats_table.add_row("Issues found", str(len(results)))
        stats_table.add_row("Processing time", f"{elapsed:.3f}s")
        stats_table.add_row("Speed", f"{metadata.size / elapsed:.0f} bytes/s")
        
        console.print(stats_table)
    
    return len(results)


if __name__ == "__main__":
    main()