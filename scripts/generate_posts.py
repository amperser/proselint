import os
import ast
import datetime
import re


grandparent = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
checks_dir = os.path.join(grandparent, "proselint", "checks")
listing = os.listdir(checks_dir)


def is_check(fn):
    return fn[-3:] == ".py" and not fn == "__init__.py"

for fn in listing:
    if is_check(fn):
        M = ast.parse(''.join(open(os.path.join(checks_dir, fn))))
        docstring = ast.get_docstring(M)
        error_code = re.search("error_code: (.*)\n", docstring).group(1)
        head, sep, tail = docstring.partition("title: ")
        docstring = head + sep + "     " + error_code + "&#58;" + tail[4:]

        post_filename = os.path.join(
            os.path.join(grandparent, "site", "_posts"),
            str(datetime.date.today()) + "-" + docstring[0:6] + ".md")

        # Chop off the first two lines
        for i in xrange(2):
            docstring = '\n'.join(docstring.split('\n')[1:])

        # Create a new post in the blog.
        with open(post_filename, 'w') as f:
            f.write(docstring)
