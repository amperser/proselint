"""Generate blog posts from check docstrings."""

from builtins import str
from builtins import range
import os
import ast
import datetime


grandparent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
checks_dir = os.path.join(grandparent, "proselint", "checks")
listing = os.walk(checks_dir)


def is_check(fn):
    """Check whether a file contains a check."""
    if not fn[-3:] == ".py":
        return False

    if fn[-11:] == "__init__.py":
        return False

    if "inprogress" in fn:
        return False

    return True

for root, subdirs, files in listing:
    for file in files:
        fn = os.path.join(root, file)
        if is_check(fn):
            M = ast.parse(''.join(open(os.path.join(checks_dir, fn))))
            docstring = ast.get_docstring(M)
            head, sep, tail = docstring.partition("title: ")
            docstring = head + sep + "     &#58;" + tail[4:]

            post_filename = os.path.join(
                os.path.join(grandparent, "site", "_posts"),
                str(datetime.date.today()) + "-" + docstring[0:6] + ".md")

            # Chop off the first two lines
            for i in range(2):
                docstring = '\n'.join(docstring.split('\n')[1:])

            # Create a new post in the blog.
            with open(post_filename, 'w') as f:
                f.write(docstring.encode('utf8'))
