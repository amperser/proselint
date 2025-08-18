"""General-purpose tools shared across linting checks."""

import json
from io import FileIO
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
    input_file: Union[str,
    FileIO],
    config: Config = DEFAULT,
    *,
    debug: bool = False,
) -> list[LintResult]:
    """Run the linter on the input file."""
    text = input_file if isinstance(input_file, str) else input_file.read()

    checks = CheckRegistry().get_all_enabled(config["checks"])

    lint_results: list[LintResult] = []
    for check in checks:

        results = check.check_with_flags(text)

        for result in results:
            (line, column) = line_and_column(text, result.start_pos)
            if is_quoted(result.start_pos, text):
                continue
            lint_results.append(LintResult(
                check_path=result.check_path,
                message=result.message,
                line=line,
                column=column,
                start_pos=result.start_pos,
                end_pos=result.end_pos,
                severity="warning",
                replacements=result.replacements
            ))

        if len(lint_results) > config["max_errors"]:
            break

    # Sort the errors by line and column number.
    return sorted(lint_results, key=itemgetter(2, 3))



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
