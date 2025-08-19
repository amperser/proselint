"""General-purpose tools shared across linting checks."""

import json
from io import FileIO
from itertools import islice
from operator import itemgetter
from typing import NamedTuple, Union

from proselint.config import DEFAULT, Config
from proselint.registry import CheckRegistry
from proselint.registry.checks import LintResult


def errors_to_json(errors: list[LintResult]) -> str:
    """Convert the errors to JSON."""
    return json.dumps({
        "status": "success",
        "data": {"errors": list(map(NamedTuple._asdict, errors))}
    }, sort_keys=True)


def line_and_column(text, position):
    """Return the line number and column of a position in a string."""
    position_counter = 0
    line_no = 0
    for line in text.splitlines(True):
        if (position_counter + len(line.rstrip())) >= position:
            break
        position_counter += len(line)
        line_no += 1
    return (line_no, position - position_counter)


def lint(
    source: Union[str, FileIO],
    config: Config = DEFAULT,
) -> list[LintResult]:
    """Run the linter on the input."""
    content = source if isinstance(source, str) else str(source.read())

    return sorted(
        islice(
            (
                LintResult(
                    result.check_path,
                    result.message,
                    *line_and_column(content, result.start_pos),
                    start_pos=result.start_pos,
                    end_pos=result.end_pos,
                    severity="warning",
                    replacements=result.replacements,
                )
                for check in CheckRegistry().get_all_enabled(config["checks"])
                for result in check.check_with_flags(content)
                if not is_quoted(result.start_pos, content)
            ),
            config["max_errors"],
        ),
        key=itemgetter(2, 3),  # sort by line and column
    )


def assert_error(text, check, n=1):
    """Assert that text has n errors of type check."""
    assert_error.description = f"No {check} error for '{text}'"
    assert len([error[0] for error in lint(text) if error[0] == check]) == n


def is_quoted(position, text):
    """Determine if the position in the text falls within a quote."""
    def matching(quotemark1, quotemark2):
        straight = '\"\''
        curly = '“”'
        if quotemark1 in straight and quotemark2 in straight:
            return True
        if quotemark1 in curly and quotemark2 in curly:
            return True
        else:
            return False

    def find_ranges(text):
        s = 0
        q = pc = ''
        start = None
        ranges = []
        seps = " .,:;-\r\n"
        quotes = ['\"', '“', '”', "'"]
        for i, c in enumerate(text + "\n"):
            if s == 0 and c in quotes and pc in seps:
                start = i
                s = 1
                q = c
            elif s == 1 and matching(c, q):
                s = 2
            elif s == 2:
                if c in seps:
                    ranges.append((start+1, i-1))
                    start = None
                    s = 0
                else:
                    s = 1
            pc = c
        return ranges

    def position_in_ranges(ranges, position):
        for start, end in ranges:
            if start <= position < end:
                return True
        return False

    return position_in_ranges(find_ranges(text), position)


def context(text, position, level="paragraph"):
    """Get sentence or paragraph that surrounds the given position."""
    if level == "sentence":
        pass
    elif level == "paragraph":
        pass

    return ""
