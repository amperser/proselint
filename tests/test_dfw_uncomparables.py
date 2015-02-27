from check import Check
from proselint.checks.wallace import uncomparables as chk


class TestCheck(Check):

    __test__ = True

    @property
    def this_check(self):
        return chk

    def test_sample_phrases(self):
        assert not self.check("""This sentence is very unique.""")

    def test_linebreaks(self):
        assert not self.check("""This sentence is very\nunique.""")
