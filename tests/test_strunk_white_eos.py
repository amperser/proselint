from check import Check
from proselint.checks import strunk_white_eos as chk


class TestCheck(Check):

    __test__ = True

    @property
    def this_check(self):
        return chk

    def test_with_utilized(self):
        assert self.check(
            """I use a hammer to drive nails into wood.."""
        )

    def test_no_utilized(self):
        assert not self.check(
            """I utilize a hammer to drive nails into wood."""
        )
