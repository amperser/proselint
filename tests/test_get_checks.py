"""Tests for annotations.misc check."""
from __future__ import absolute_import

from .check import Check

from proselint.tools import get_checks


class TestCheck(Check):
    """The test class for annotations.misc."""

    __test__ = True

    def test_exclude(self):
        full_checks = get_checks({
            'checks': {
                'typography.symbols': True,
            }
        })

        skip_ellipsis = get_checks({
            'checks': {
                'typography.symbols': True,
                'typography.symbols.ellipsis': False,
            }
        })

        assert len(full_checks) - 1 == len(skip_ellipsis)

    def test_only(self):
        checks = get_checks({
            'checks': {
                'typography.symbols': False,
                'typography.symbols.ellipsis': True,
            }
        })

        assert len(checks) == 1

    def test_implicit_only(self):
        checks = get_checks({
            'checks': {
                'typography.symbols.ellipsis': True,
            }
        })

        assert len(checks) == 1
