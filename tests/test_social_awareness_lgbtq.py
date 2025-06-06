"""Tests for social_awareness.lgbtq check."""

from proselint.checks.social_awareness import lgbtq as chk

from .check import Check


class TestCheck(Check):
    """The test class for social_awareness.lgbtq."""

    __test__ = True

    @property
    def this_check(self):
        """Boilerplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for social_awareness.lgbtq."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert self.passes("""They were a gay couple.""")
        assert not self.passes("""He was a homosexual man.""")
        assert self.passes("""I once met a gay man.""")
        assert not self.passes("""I once met a fag.""")

    def test_homosexual_term(self):
        """Check that the term homosexual does not get caught."""
        assert self.passes("""Homosexual.""")

    def test_sexual_prefence(self):
        """Check that sexual preference is flagged."""
        assert not self.passes("""My sexual preference is for women.""")
