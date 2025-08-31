#!/usr/bin/env python3
"""Benchmark proselint performance."""

import time
import cProfile
import pstats
from pathlib import Path
import tempfile

# Generate test content
def generate_test_content(size_kb=100):
    """Generate test content with known issues."""
    base = """The reason is because this is very unique. It's literally perfect.
At this point in time, we should utilize better tools. The reason is because
of various issues. This will allow you to do things. Very important matters
need attention. We must utilize all resources. The point in time is now.
"""
    return (base * (size_kb * 10))[:size_kb * 1024]

# Create test files
test_sizes = [10, 50, 100, 500]  # KB
test_files = []

print("Creating test files...")
for size in test_sizes:
    content = generate_test_content(size)
    f = tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False)
    f.write(content)
    f.close()
    test_files.append((size, f.name))
    print(f"  Created {size}KB test file: {f.name}")

print("\nBenchmarking proselint...")

# Profile the main bottleneck
print("\nProfiling 100KB file...")
from proselint.tools import LintFile
from proselint.command_line import CheckRegistry, __register__

profiler = cProfile.Profile()
profiler.enable()

# Initialize registry once
CheckRegistry().register_many(__register__)
lint_file = LintFile(Path(test_files[2][1]))
results = lint_file.lint()

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
print("\nTop 20 time-consuming functions:")
stats.print_stats(20)

# Benchmark different file sizes
print("\n" + "="*60)
print("Performance by file size:")
print("="*60)

for size, filepath in test_files:
    start = time.perf_counter()
    
    lint_file = LintFile(Path(filepath))
    results = lint_file.lint()
    
    elapsed = time.perf_counter() - start
    errors_found = len(results)
    
    print(f"{size:4}KB: {elapsed:6.3f}s ({errors_found:4} errors, {size/elapsed:6.1f} KB/s)")

# Clean up
for _, f in test_files:
    Path(f).unlink()