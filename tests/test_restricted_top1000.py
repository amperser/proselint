"""Tests reverse existence for top1000 and check."""

from proselint.checks.restricted import top1000 as chk

from .check import Check


class TestCheck(Check):
    """The test class for restricted.top1000."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for restricted.top1000."""
        assert self.passes("""I am blonde.""")
        assert self.passes("""I'm gonna listen to music tonight.""")
        assert self.passes("""I will go to sleep because I have school.""")
        assert self.passes("""""")

        assert not self.passes("""I am tired.""")
        assert not self.passes("""I hate broccoli.""")
        assert not self.passes("""I am tired and hate broccoli.""")
