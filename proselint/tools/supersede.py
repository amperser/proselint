import re


def supersede(new, old, error_code):
    def check(text):
        msg = "It's '{}', not '{}'.".format(new, old)
        errors = []
        for o in re.finditer(old, text, flags=re.IGNORECASE):
            errors.append((o.start(), o.end(), error_code, msg))

        return errors

    return check
