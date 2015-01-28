from memoize import memoize


@memoize
def reverse(text):
    return text[::-1]
