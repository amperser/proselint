"""Unit tests for MAU101."""

from check import Check
from proselint.checks.garner import a_vs_an as chk


class TestCheck(Check):

    __test__ = True

    @property
    def this_check(self):
        return chk

    def test(self):
        assert self.check("""An apple a day keeps the doctor away.""")
        assert self.check("""The Epicurean garden.""")
        assert not self.check("""A apple a day keeps the doctor away.""")
        assert not self.check("""An apple an day keeps the doctor away.""")
        assert not self.check("""An apple an\nday keeps the doctor away.""")
