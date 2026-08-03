#!/usr/bin/env python3
"""Calculate a lint score which we use to evaluate proselint's performance."""

from dataclasses import asdict, dataclass
from json import dumps, loads
from os.path import curdir
from pathlib import Path

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Footer, Header, Label, ListItem, ListView

import corpus.scripts.generate_readme_corpus as corpus
from proselint.checks import __register__
from proselint.registry import CheckRegistry
from proselint.tools import LintFile, LintResult

CheckRegistry().register_many(__register__)


ROOT_DIR = Path(curdir).resolve()
CORPUS_DIR = Path(ROOT_DIR) / "corpus" / "works"
RESULT_PATH = Path(ROOT_DIR) / "corpus.json"
CONFIRM_PHRASE = "REGENERATE"


@dataclass
class _Detection:
    check_name: str
    message: str
    context: str
    span: tuple[int, int]
    pos: tuple[int, int]

    explanation: str = ""
    reviewed: bool = False

    @classmethod
    def from_proselint(
            cls,
            result: LintResult,
            source: str,
            padding: int = 10,
            ) -> "_Detection":
        start, end = result.check_result.span
        context = source[
                max(0, start - padding) : min(len(source), end + padding)
                ]

        return cls(
            pos=result.pos,
            span=result.check_result.span,
            message=result.check_result.message,
            check_name=result.check_result.check_path,
            context=context
        )


@dataclass
class _Work(corpus.Metadata):
    positives: list[_Detection]


@dataclass
class _Stats:
    total: int
    reviewed: int

    @property
    def remaining(self) -> int:
        return self.total - self.reviewed


def score(positives: int, falses: int, k: float = 2.0) -> float:
    """
    T (T / (F + T)) k.

    T = True positives
    F = False positives
    k = Imprecision temperature (k > 0)
    """
    return positives / (falses + positives) * k


def _load_corpus(path: Path) -> dict[str, _Work]:
    if not path.exists():
        return {}

    raw = loads(path.read_text(encoding="utf-8"))
    data = {}

    for key, value in raw.items():
        data[key] = _Work(
            work=corpus.Work(**value["work"]),
            author=corpus.Author(**value["author"]),
            source=corpus.Source(**value["source"]),
            positives=[_Detection(**d) for d in value["positives"]],
        )

    return data


class _WorkItem(ListItem):
    def __init__(self, key: str, work: _Work) -> None:
        stats = self.stats(work)

        marker = "+" if stats.remaining == 0 and stats.total else " "

        label = Label(
            f"{marker} {work.work.name} ({stats.reviewed}/{stats.total})"
        )

        self.key = key
        self.work = work

        super().__init__(label)

    @staticmethod
    def stats(work: _Work) -> _Stats:
        reviewed = sum(d.reviewed for d in work.positives)
        return _Stats(
            total=len(work.positives),
            reviewed=reviewed,
        )


class _Corpus(App):
    TITLE = "Review Corpus"

    def __init__(self) -> None:
        super().__init__()

        self.corpus = _load_corpus(RESULT_PATH)

    def compose(self) -> ComposeResult:  # noqa: PLR6301
        yield Header()

        with Horizontal(id="body"):
            with Vertical(id="works"):
                yield Label("Works")
                yield ListView(id="works-li")

            with Vertical(id="detections"):
                yield Label("Detections")
                yield ListView(id="detections-li")

        yield Footer()

    def on_mount(self) -> None:
        works = self.query_one("#works-li", ListView)

        for key, work in sorted(
            self.corpus.items(),
            key=lambda item: item[1].work.name,
        ):
            works.append(_WorkItem(key, work))


if __name__ == "__main__":
    app = _Corpus()
    app.run()
    pass

    result = (
        loads(RESULT_PATH.read_text(encoding="utf-8"))
        if RESULT_PATH.exists()
        else {}
    )

    for entry in CORPUS_DIR.glob("*"):
        metadata = corpus.parse_entry(entry)
        source = metadata.content

        key = str(metadata.path.relative_to(ROOT_DIR))
        results = LintFile(key, source).lint()
        detections = [
                _Detection.from_proselint(result, source)
                for result in results
                ]

        work = _Work(
            work=metadata.meta.work,
            author=metadata.meta.author,
            source=metadata.meta.source,
            positives=detections,
        )

        if key not in result:
            value = asdict(work)

            value.pop("content", None)
            value.pop("path", None)

            result[key] = value

    RESULT_PATH.write_text(
            dumps(result, indent=2, default=str),
            encoding="utf-8"
            )
