"""General-purpose tools shared across linting checks."""

import json
import stat
from bisect import bisect_left
from collections.abc import Callable
from itertools import accumulate, chain, islice
from operator import itemgetter
from os import walk
from pathlib import Path
from re import Pattern, finditer
from re import compile as rcompile
from sys import stdin
from typing import NamedTuple, cast, overload

from proselint.config import DEFAULT, Config
from proselint.registry import CheckRegistry
from proselint.registry.checks import CheckResult

ACCEPTED_EXTENSIONS = {".md", ".txt", ".rtf", ".html", ".tex", ".markdown"}


def verify_path(
    path: Path,
    *,
    resolve: bool = False,
    reject_file: bool = False,
    reject_dir: bool = False,
    must_exist: bool = False,
) -> Path:
    """Check a path for specified conditions."""
    if resolve:
        path = path.resolve()

    try:
        stat_res = path.stat()
    except FileNotFoundError as err:
        if must_exist:
            raise err
        return path

    if reject_file and stat.S_ISREG(stat_res.st_mode):
        raise OSError("Files not permitted - found file %s", path)
    if reject_dir and stat.S_ISDIR(stat_res.st_mode):
        raise OSError("Directories not permitted - found directory %s", path)

    return path


def extract_files(paths: list[Path]) -> list[Path]:
    """Expand `paths` to include all text files accepted by the linter."""
    return list(
        chain.from_iterable(
            (
                file
                for root, _, files in walk(path)
                for file in map(Path(root).__truediv__, files)
                if file.suffix in ACCEPTED_EXTENSIONS
            )
            if path.is_dir()
            else (path,)
            for path in (
                verify_path(path_unchecked, resolve=True)
                for path_unchecked in paths
            )
        )
    )


SEPARATORS = " ,.!?:;-\r\n"
STRAIGHT_QUOTES = {'"', "'"}
CURLY_QUOTES = {"“", "”"}
CURLY_SINGLE_QUOTES = {"‘", "’"}  # noqa: RUF001
QUOTES = "".join(STRAIGHT_QUOTES | CURLY_QUOTES | CURLY_SINGLE_QUOTES)
QUOTE_PATTERN = rcompile(rf"(?:\B[{QUOTES}]|[{QUOTES}]\B)")


def check_matching_quotes(chars: tuple[str, str]) -> bool:
    """Check if a pair of quotes match."""
    # fmt: off
    return (
        (chars[0] in STRAIGHT_QUOTES and chars[0] == chars[1])
        or set(chars) in (CURLY_QUOTES, CURLY_SINGLE_QUOTES)
    )


def find_spans(
    text: str,
    pattern: Pattern[str],
    predicate: Callable[[tuple[str, str]], bool],
) -> list[tuple[int, int]]:
    """
    Find spans of matching characters (e.g. quotes).

    Note that this ignores nested spans, and currently requires a separator
    around the matched items. Its only function within proselint is to find
    quotes, but either of these behaviours may change in the future.
    """
    prev: tuple[str, int] | None = None
    spans: list[tuple[int, int]] = []
    for match in finditer(pattern, text):
        char, span_end = (match.group(0), match.start())
        if not prev:
            if text[span_end - 1] in SEPARATORS:
                prev = (char, span_end)
            continue
        if predicate((prev[0], char)) and text[span_end + 1] in SEPARATORS:
            spans.append((prev[1], span_end))
            prev = None
    return spans


class LintResult(NamedTuple):
    """Carry lint result information."""

    check_result: CheckResult
    pos: tuple[int, int]

    @property
    def extent(self) -> int:
        """The extent (span width) of the result."""
        return self.check_result.span[1] - self.check_result.span[0]

    def into_dict(self) -> dict[str, object]:
        """Convert the `LintResult` into a flattened dictionary."""
        result = self._asdict() | self.check_result._asdict()
        del result["check_result"]
        return result


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

    source: str | Path
    content: str
    line_bounds: tuple[int, ...]
    quote_bounds: tuple[int, ...]
    """A flat sequence of positions guaranteed to come in pairs."""

    @overload
    def __init__(self, source: Path, content: str | None = None) -> None: ...

    @overload
    def __init__(self, source: str, content: str) -> None: ...
    def __init__(self, source: str | Path, content: str | None = None) -> None:
        """Initialise a file for the linter from a given `source`."""
        if isinstance(source, str) and content is None:
            raise ValueError("Content must be given if the file path is not.")

        self.source = source

        if content:
            self.content = f"\n{content}\n"
            self._compute_bounds()
            return
        self.content, self.line_bounds, self.quote_bounds = ("", (), ())

    @classmethod
    def from_stdin(cls) -> "LintFile":
        """Return a new `LintFile` with content from standard input."""
        return cls("<stdin>", stdin.read())

    @property
    def source_name(self) -> str:
        """Return the source name (filename or otherwise) of the `LintFile`."""
        return self.source if isinstance(self.source, str) else self.source.name

    def _compute_bounds(self) -> None:
        if not self.content:
            raise ValueError("Content must be available to compute boundaries.")

        self.line_bounds = self._line_bounds()
        self.quote_bounds = tuple(
            chain.from_iterable(
                find_spans(self.content, QUOTE_PATTERN, check_matching_quotes)
            )
        )

    def _read(self) -> None:
        """Read the source contents and compute boundaries."""
        if self.content:
            return

        # NOTE: necessary to prevent edge cases for padding and line boundaries
        content = cast("Path", self.source).read_text()
        self.content = f"\n{content}\n"

        self._compute_bounds()

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
        bound_idx = bisect_left(self.line_bounds, position)
        return (bound_idx, position - self.line_bounds[bound_idx - 1])

    def is_quoted_pos(self, position: int) -> bool:
        """Determine if the content position falls within quotes."""
        # NOTE: since bounds are paired, odd insertions are always within a span
        return bisect_left(self.quote_bounds, position) % 2 == 1

    def lint(self, config: Config = DEFAULT) -> list[LintResult]:
        """Run the linter against the file."""
        self._read()
        registry = CheckRegistry()
        return sorted(
            islice(
                (
                    LintResult(result, self.line_col_of(result.span[0]))
                    for check in registry.get_all_enabled(config["checks"])
                    for result in check.check_with_flags(self.content)
                    if (
                        check.flags.allow_quotes
                        or not self.is_quoted_pos(result.span[0])
                    )
                ),
                config["max_errors"],
            ),
            key=itemgetter(1),  # sort by line and column
        )
