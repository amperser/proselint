from check import Check
from proselint.checks import dfw_uncomparables


class TestCheck(Check):

    @property
    def this_check(self):
        return dfw_uncomparables

    def test_sample_phrases(self):
        assert not self.check(
            """This sentence is very unique."""
        )

    def test_linebreaks(self):
        assert not self.check(
            """This sentence is very\n unique."""
        )
