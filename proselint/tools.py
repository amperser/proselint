"""General-purpose tools shared across linting checks."""

import json
from collections.abc import Callable
from itertools import accumulate, chain, islice
from operator import itemgetter
from pathlib import Path
from re import Pattern, finditer
from re import compile as rcompile
from sys import stdin
from typing import Union, cast, overload

from proselint.config import DEFAULT, Config
from proselint.registry import CheckRegistry
from proselint.registry.checks import LintResult

ACCEPTED_EXTENSIONS = [".md", ".txt", ".rtf", ".html", ".tex", ".markdown"]


def extract_files(paths: list[Path]) -> list[Path]:
    """Expand `paths` to include all text files accepted by the linter."""
    return list(chain.from_iterable(
        (
            file
            for root, _, files in path.walk()
            for file in map(root.__truediv__, files)
            if file.suffix in ACCEPTED_EXTENSIONS
        ) if path.is_dir() else (path,)
        for path in paths
    ))


def find_spans(
    text: str,
    pattern: Pattern[str],
    predicate: Callable[[tuple[str, str]], tuple[tuple[int, int], bool]],
) -> list[tuple[int, int]]:
    """Find spans of matching characters (e.g. quotes)."""
    active = tuple((m.group(0), m.start()) for m in finditer(pattern, text))
    prev: list[tuple[str, int]] = []
    spans: list[tuple[int, int]] = []
    for char, span_end in active:
        for potential, span_start in reversed(prev):
            offset, match = predicate((potential, char))
            if match:
                _ = prev.pop()
                spans.append((span_start + offset[0], span_end + offset[1]))
                break
        else:
            prev.append((char, span_end))
    return spans


STRAIGHT_QUOTES = {'"', "'"}
CURLY_QUOTES = {"“", "”"}
CURLY_SINGLE_QUOTES = {"‘", "’"}  # noqa: RUF001


def check_matching_quotes(
    chars: tuple[str, str],
) -> tuple[tuple[int, int], bool]:
    """Check if a pair of quotes match."""
    end_offset = 1 if chars[1][0] in ",.!?" else 0
    chars = (chars[0], chars[1].lstrip(",.!?"))
    return (
        (0, end_offset),
        (
            (chars[0] in STRAIGHT_QUOTES and chars[0] == chars[1])
            or set(chars) in (CURLY_QUOTES, CURLY_SINGLE_QUOTES)
        ),
    )


QUOTES = "".join(STRAIGHT_QUOTES | CURLY_QUOTES | CURLY_SINGLE_QUOTES)
QUOTE_PATTERN = rcompile(rf"(?:\B[{QUOTES}]\b|\b[,.!?]?[{QUOTES}]\B)")


def find_quoted_ranges(text: str) -> list[tuple[int, int]]:
    """Find the ranges of quote pairs in text."""
    return find_spans(text, QUOTE_PATTERN, check_matching_quotes)


def errors_to_json(errors: list[LintResult]) -> str:
    """Convert the errors to JSON."""
    return json.dumps(
        {
            "status": "success",
            "data": {"errors": [err._asdict() for err in errors]},
        },
        sort_keys=True,
    )


class LintFile:
    """A prepared file with span information for linting against."""

    source: Union[str, Path]
    content: str
    line_bounds: tuple[int, ...]
    quote_spans: tuple[tuple[int, int], ...]

    @overload
    def __init__(
        self, source: Path, content: Union[str, None] = None
    ) -> None: ...

    @overload
    def __init__(self, source: str, content: str) -> None: ...
    def __init__(
        self, source: Union[str, Path], content: Union[str, None] = None
    ) -> None:
        """Initialise a file for the linter from a given `source`."""
        if isinstance(source, str) and content is None:
            raise ValueError("Content must be given if the file path is not.")

        self.source = source

        # NOTE: necessary to prevent edge cases for padding and line boundaries
        content = content or cast("Path", source).read_text()
        self.content = f"\n{content}\n"

        self.line_bounds = self._line_bounds()
        self.quote_spans = tuple(find_quoted_ranges(self.content))

    @classmethod
    def from_stdin(cls) -> "LintFile":
        """Return a new `LintFile` with content from standard input."""
        return cls("<stdin>", stdin.read())

    @property
    def source_name(self) -> str:
        """Return the source name (filename or otherwise) of the `LintFile`."""
        return self.source if isinstance(self.source, str) else self.source.name

    def _line_bounds(self) -> tuple[int, ...]:
        """Return the starting positions of each line in the text."""
        return tuple(
            map(
                (1).__rsub__,
                accumulate(map(len, self.content.splitlines(keepends=True))),
            )
        )

    def line_col_of(self, position: int) -> tuple[int, int]:
        """Return the line and column numbers of a position in the content."""
        line_delta, bound = next(
            filter(
                lambda x: position > x[1], enumerate(reversed(self.line_bounds))
            )
        )
        return (len(self.line_bounds) - line_delta, position - bound)

    def is_quoted_pos(self, position: int) -> bool:
        """Determine if the content position falls within quotes."""
        return any(start <= position < end for start, end in self.quote_spans)

    def lint(self, config: Config = DEFAULT) -> list[LintResult]:
        """Run the linter against the file."""
        registry = CheckRegistry()
        return sorted(
            islice(
                (
                    LintResult(
                        result.check_path,
                        result.message,
                        *self.line_col_of(result.start_pos),
                        start_pos=result.start_pos,
                        end_pos=result.end_pos,
                        severity="warning",
                        replacements=result.replacements,
                    )
                    for check in registry.get_all_enabled(config["checks"])
                    for result in check.check_with_flags(self.content)
                    if not self.is_quoted_pos(result.start_pos)
                ),
                config["max_errors"],
            ),
            key=itemgetter(2, 3),  # sort by line and column
        )

    def output_errors(
        self,
        results: list[LintResult],
        *,
        output_json: bool = False,
        compact: bool = False,
    ) -> None:
        """Log lint results from the LintFile."""
        if output_json:
            print(errors_to_json(results))
            return

        name = "-" if compact else self.source_name

        for result in results:
            print(f"{name}{result}")
