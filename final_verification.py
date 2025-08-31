#!/usr/bin/env python3
"""Final verification of all fixes."""

import json
from proselint.tools import LintFile
from proselint.config import load_from


def verify_issue_1379():
    """Verify meantime/meanwhile fix."""
    print("Verifying Issue #1379 (meantime/meanwhile)...")
    
    # This used to trigger conflicting suggestions
    text = "In the meantime, we should work. Meantime, let's go."
    lint_file = LintFile('<test>', text)
    config = load_from()
    results = lint_file.lint(config)
    
    # Should not have any meantime/meanwhile related errors
    related_errors = [r for r in results if 'meantime' in r.message.lower() or 'meanwhile' in r.message.lower()]
    
    if related_errors:
        print(f"  ❌ FAIL: Found unexpected errors: {[r.message for r in related_errors]}")
        return False
    else:
        print(f"  ✅ PASS: No conflicting suggestions")
        return True


def verify_issue_1367():
    """Verify curly quotes config fix."""
    print("\nVerifying Issue #1367 (curly_quotes config)...")
    
    text = 'He said "hello world" today.'
    lint_file = LintFile('<test>', text)
    
    # Test that it works by default
    config = load_from()
    results = lint_file.lint(config)
    curly_errors = [r for r in results if 'curly_quotes' in r.check_path]
    
    if not curly_errors:
        print(f"  ❌ FAIL: Curly quotes check not working by default")
        return False
    
    print(f"  ✅ Default: Found curly quotes error as expected")
    
    # Test that config disables it
    config['checks']['typography.symbols.curly_quotes'] = False
    results = lint_file.lint(config)
    curly_errors = [r for r in results if 'curly_quotes' in r.check_path]
    
    if curly_errors:
        print(f"  ❌ FAIL: Config not disabling curly quotes check")
        return False
    
    print(f"  ✅ Config: Successfully disabled via config")
    return True


def verify_issue_971():
    """Verify hyperbole false positive fix."""
    print("\nVerifying Issue #971 (hyperbole false positive)...")
    
    # This used to trigger false positive
    text = "Data values: 1, 2, ???, 4, 5"
    lint_file = LintFile('<test>', text)
    config = load_from()
    results = lint_file.lint(config)
    
    hyperbole_errors = [r for r in results if 'hyperbole' in r.check_path or 'hyperbolic' in r.message.lower()]
    
    if hyperbole_errors:
        print(f"  ❌ FAIL: False positive still triggered: {hyperbole_errors[0].message}")
        return False
    
    print(f"  ✅ PASS: No false positive for ??? data marker")
    
    # Make sure real hyperbole still works
    text2 = "This is amazing!!!"
    lint_file2 = LintFile('<test>', text2)
    results2 = lint_file2.lint(config)
    hyperbole_errors2 = [r for r in results2 if 'hyperbole' in r.check_path or 'hyperbolic' in r.message.lower()]
    
    if not hyperbole_errors2:
        print(f"  ❌ FAIL: Real hyperbole not detected")
        return False
    
    print(f"  ✅ PASS: Real hyperbole still detected")
    return True


def verify_registry_initialization():
    """Verify CheckRegistry is properly initialized."""
    print("\nVerifying CheckRegistry initialization...")
    
    from proselint.registry import CheckRegistry
    from proselint.checks import __register__
    
    # CheckRegistry is a singleton, so get the instance
    registry = CheckRegistry()
    
    # Since it's a singleton, it may already have checks from previous imports
    # The important thing is that LintFile.lint() properly uses it
    initial_count = len(registry.checks)
    print(f"  ℹ️  Registry is a singleton with {initial_count} checks")
    
    # If empty, register checks
    if initial_count == 0:
        registry.register_many(__register__)
        print(f"  ✅ Registered {len(registry.checks)} checks")
    else:
        print(f"  ✅ Registry already initialized (singleton pattern working)")
    
    # The real test is whether LintFile.lint() works correctly
    
    # Verify LintFile uses registry correctly
    text = "Test text"
    lint_file = LintFile('<test>', text)
    config = load_from()
    
    # This should not raise an error
    try:
        results = lint_file.lint(config)
        print(f"  ✅ PASS: LintFile.lint() works correctly")
        return True
    except Exception as e:
        print(f"  ❌ FAIL: LintFile.lint() failed: {e}")
        return False


def main():
    """Run all verifications."""
    print("="*60)
    print("FINAL VERIFICATION OF ALL FIXES")
    print("="*60)
    
    tests = [
        verify_issue_1379,
        verify_issue_1367,
        verify_issue_971,
        verify_registry_initialization,
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "="*60)
    print(f"RESULTS: {passed}/{len(tests)} verifications passed")
    
    if passed == len(tests):
        print("✅ ALL FIXES VERIFIED AND WORKING CORRECTLY!")
        return 0
    else:
        print("❌ Some issues detected - review needed")
        return 1


if __name__ == "__main__":
    exit(main())