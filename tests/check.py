class Check(object):

    @property
    def this_check(self):
        raise NotImplementedError

    def check(self, lst):
        if isinstance(lst, basestring):
            lst = [lst]

        errors = []
        for text in lst:
            errors.append(self.this_check.check(text))

        return len(errors) == 0

    def test_whatwhat(self):
        return False
