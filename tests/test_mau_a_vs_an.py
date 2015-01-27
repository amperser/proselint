from check import Check
from proselint.checks import mau_a_vs_an as chk


class TestCheck(Check):

    __test__ = True

    @property
    def this_check(self):
        return chk

    def test_clean(self):
        assert self.check(
            """An apple a day keeps the doctor away."""
        )

    def test_a_apple(self):
        assert not self.check(
            """A apple a day keeps the doctor away."""
        )

    def test_an_day(self):
        assert not self.check(
            """An apple an day keeps the doctor away."""
        )

    def test_linebreak(self):
        assert not self.check(
            """An apple an\nday keeps the doctor away."""
        )

    def test_mid_word(self):
        assert self.check(
            """The Epicurean garden."""
        )
