from proselint.checks import dfw_uncomparables


class TestCheck(object):

    @property
    def this_check(self):
        return dfw_uncomparables

    def check(self, lst):
        if isinstance(lst, basestring):
            lst = [lst]

        errors = []
        for text in lst:
            errors.append(self.this_check.check(text))

        return len(errors) == 0

    def test_sample_phrases(self):
        assert not self.check(
            """This sentence is very unique."""
        )

    def test_linebreaks(self):
        assert not self.check(
            """This sentence is very\n unique."""
        )
