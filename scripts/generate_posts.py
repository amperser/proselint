"""Generate blog posts from check docstrings."""

import ast
import datetime
import os
from pathlib import Path

project_path = Path(__file__).parent.parent
checks_path = project_path / "proselint" / "checks"
listing = os.walk(checks_path)


def is_check(file_path: Path) -> bool:
    """Check whether a file contains a check."""
    if file_path.suffix != ".py":
        return False

    if file_path.name == "__init__.py":
        return False

    if "inprogress" in file_path.name:
        return False

    return True


for root, _, files in listing:
    root_path = Path(root)
    for file in files:
        file_path = root_path / file
        if is_check(file_path):
            M = ast.parse("".join(file_path.open()))
            docstring = ast.get_docstring(M)
            head, sep, tail = docstring.partition("title: ")
            docstring = head + sep + "     &#58;" + tail[4:]

            post_filename = (
                project_path
                / f"site/_posts/{datetime.date.today()}-{docstring[0:6]}.md"
            )

            # Chop off the first two lines
            for _ in range(2):
                docstring = "\n".join(docstring.split("\n")[1:])

            # Create a new post in the blog.
            with post_filename.open("xb") as f:  # TODO: maybe add b, so xb
                f.write(docstring.encode("utf8"))
