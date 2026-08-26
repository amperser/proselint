#!/usr/bin/env python3
"""Helper TUI to review the corpus."""

from dataclasses import dataclass
from json import dump, loads
from pathlib import Path
from typing import ClassVar, TypedDict, cast, final, override

from rich.text import Text
from textual import work
from textual.app import App, ComposeResult
from textual.binding import Binding, BindingType
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.reactive import reactive
from textual.widgets import (
    Label,
    ListItem,
    ListView,
    LoadingIndicator,
    Rule,
    Static,
)

import corpus.scripts.generate_readme_corpus as corpus
from proselint.checks import __register__
from proselint.registry import CheckRegistry
from proselint.registry.checks import CheckResult
from proselint.tools import LintFile, LintResult

CheckRegistry().register_many(__register__)

ROOT_DIR = Path(__file__).resolve().parents[1]
CORPUS_DIR = ROOT_DIR / "corpus" / "works"
RESULT_PATH = ROOT_DIR / "corpus.json"

CONTEXT_RADIUS = 1


class _Detection(TypedDict):
    highlight: tuple[int, int]
    pos: tuple[int, int]
    check: CheckResult
    context: str
    marked: bool


class _Entry(corpus.Metadata):
    detections: list[_Detection]


@dataclass
class _Statistics:
    total: int
    positives: int

    @property
    def remaining(self) -> int:
        return self.total - self.positives

    @staticmethod
    def from_entry(entry: _Entry) -> "_Statistics":
        detections = entry["detections"]

        return _Statistics(
            len(detections), sum(d["marked"] for d in detections)
        )


def _clamp(lower: int, value: int, upper: int) -> int:
    return max(lower, min(value, upper))


def _context(
    file: LintFile,
    line: int,
    span: tuple[int, int],
    radius: int = CONTEXT_RADIUS,
) -> tuple[str, tuple[int, int]]:
    """Extract a window of `radius` lines around `line`."""
    content = file.content
    bounds = file.line_bounds

    first_line_idx = max(0, line - 1 - radius)
    last_line_idx = min(len(bounds), line + radius)

    context_start = bounds[first_line_idx]
    context_end = (
        bounds[last_line_idx] if last_line_idx < len(bounds) else len(content)
    )

    context = content[context_start:context_end]

    # Translate `span` into offsets for `Text.stylize`.
    # span (source) -> absolute, 1-indexed
    # Text.stylize  -> relative to window, 0-indexed
    start, end = span
    highlight = (
        _clamp(0, start - context_start, len(context)),
        _clamp(0, end - context_start, len(context)),
    )

    return context, highlight


def _to_detections(key: str, content: str) -> list[_Detection]:
    file = LintFile(key, content=content)

    def to_detection(result: LintResult) -> _Detection:
        line, _ = result.pos
        context, highlight = _context(file, line, result.check_result.span)

        return _Detection(
            pos=result.pos,
            check=result.check_result,
            marked=False,
            context=context,
            highlight=highlight,
        )

    return list(map(to_detection, file.lint()))


def _decode_detection(raw: _Detection) -> _Detection:
    raw["check"] = CheckResult(*raw["check"])

    return raw


def _decode_entry(raw: _Entry) -> _Entry:
    raw["detections"] = list(map(_decode_detection, raw["detections"]))

    return raw


def read_corpus(path: Path) -> dict[str, _Entry]:
    """Read corpus file and decode it."""
    if not path.exists():
        return {}

    raw = cast("dict[str, _Entry]", loads(path.read_text(encoding="utf-8")))
    return {key: _decode_entry(value) for key, value in raw.items()}


def _write_corpus(path: Path, corpus_data: dict[str, _Entry]) -> None:
    with path.open("w", encoding="utf-8") as fp:
        dump(corpus_data, fp, indent="\t", sort_keys=True)


def _mark(*, done: bool) -> Text:
    return Text().append(
        "+ " if done else "", style="bold green" if done else "bold"
    )


class _ReviewItem(ListItem):
    key: str

    def __init__(self, key: str) -> None:
        self.key = key
        super().__init__(Label(self.render_label()))

    def render_label(self) -> Text:
        raise NotImplementedError

    def refresh_label(self) -> None:
        self.query_one(Label).update(self.render_label())


class _EntryItem(_ReviewItem):
    entry: _Entry

    def __init__(self, key: str, entry: _Entry) -> None:
        self.entry = entry
        super().__init__(key)

    @override
    def render_label(self) -> Text:
        stats = _Statistics.from_entry(self.entry)
        done = stats.total > 0 and not stats.remaining

        return (
            _mark(done=done)
            .append(self.entry["work"]["name"], style="bold cyan")
            .append(f" ({stats.positives}/{stats.total})")
        )


class _DetectionItem(_ReviewItem):
    detection: _Detection

    def __init__(self, key: str, detection: _Detection) -> None:
        self.detection = detection
        super().__init__(key)

    @override
    def render_label(self) -> Text:
        return (
            _mark(done=self.detection["marked"])
            .append(self.detection["check"].check_path, style="bold cyan")
            .append(f" {self.detection['check'].message}")
        )


@final
class _Corpus(App[None]):
    TITLE = "Review Corpus"
    ENABLE_COMMAND_PALETTE = False

    BINDINGS: ClassVar[list[BindingType]] = [
        Binding("r", "toggle_marked", "Toggle marked"),
    ]

    _loading = reactive(default=True)

    def __init__(self) -> None:
        super().__init__()

        self._corpus: dict[str, _Entry] = {}
        self._items: dict[str, _EntryItem] = {}

    @override
    def compose(self) -> ComposeResult:
        with Horizontal(id="body"):
            yield LoadingIndicator(id="loading")

            with Vertical(id="works"):
                yield Label(Text("Works", style="bold"))
                yield ListView(id="works-li")

            yield Rule(orientation="vertical")

            with Vertical(id="detections"):
                yield Label(Text("Detections", style="bold"))
                yield ListView(id="detections-li")

            yield Rule(orientation="vertical")

            with Vertical(id="detail"):
                yield Label(Text("Detail", style="bold"))
                with VerticalScroll(id="detail-body-scroll", can_focus=False):
                    yield Static(id="detail-body")

    def on_mount(self) -> None:
        self.theme = "ansi-dark"
        _ = self._ensure_corpus()

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        item = event.item

        if event.list_view.id == "works-li" and isinstance(item, _EntryItem):
            _ = self._show_detections(item)
        elif event.list_view.id == "detections-li" and isinstance(
            item, _DetectionItem
        ):
            self._show_detail(item.detection)

    def action_toggle_marked(self) -> None:
        detections = self.query_one("#detections-li", ListView)
        item = detections.highlighted_child

        if not isinstance(item, _DetectionItem):
            return

        print(item.detection["marked"])
        item.detection["marked"] = not item.detection["marked"]

        item.refresh_label()
        self._show_detail(item.detection)

        if entry_item := self._items.get(item.key):
            entry_item.refresh_label()

        _write_corpus(RESULT_PATH, self._corpus)

    @work(exclusive=True)
    async def _show_detections(self, item: _EntryItem) -> None:
        detections = self.query_one("#detections-li", ListView)
        await detections.clear()

        items = [
            _DetectionItem(item.key, detection)
            for detection in item.entry["detections"]
        ]

        if not items:
            self.query_one("#detail-body", Static).update("")
            return

        await detections.mount(*items)
        detections.index = 0

        self._show_detail(item.entry["detections"][0])

    def _show_detail(self, detection: _Detection) -> None:
        line, col = detection["pos"]
        marked = detection["marked"]

        text = (
            Text()
            .append(detection["check"].check_path, style="bold cyan")
            .append(f" {line}:{col}\n\n", style="dim")
            .append(detection["check"].message)
            .append("\n")
        )

        start, end = detection["highlight"]

        context = Text().append(detection["context"])
        context.stylize("reverse bold", start, end)

        _ = (
            text.append(context)
            .append("\n\n")
            .append(
                "Positive" if marked else "False-positive",
                style="bold green" if marked else "bold red",
            )
            .append("\nPress ", style="dim")
            .append("R", style="bold dim")
            .append(" to mark", style="dim")
        )

        self.query_one("#detail-body", Static).update(text)

    @work(thread=True)
    def _ensure_corpus(self) -> None:
        data = (
            read_corpus(RESULT_PATH)
            if RESULT_PATH.exists()
            else self._generate()
        )

        self.call_from_thread(self._finish_loading, data)

    def _finish_loading(self, data: dict[str, _Entry]) -> None:
        self._corpus = data
        self._loading = False

        _ = self.query_one("#loading").remove()

        works = self.query_one("#works-li", ListView)
        entries = sorted(data.items(), key=lambda item: item[1]["work"]["name"])

        for key, entry in entries:
            item = _EntryItem(key, entry)

            self._items[key] = item
            _ = works.append(item)

        if entries:
            _ = works.focus()
            works.index = 0

            _ = self._show_detections(works.query_one(_EntryItem))

    @staticmethod
    def _generate() -> dict[str, _Entry]:
        entries: dict[str, _Entry] = {}

        for path in CORPUS_DIR.glob("*"):
            parsed = corpus.parse_entry(path)
            content = parsed["content"]
            key = str(parsed["path"].relative_to(ROOT_DIR))

            entry = _Entry(
                **parsed["meta"], detections=_to_detections(key, content)
            )

            _ = entry.pop("content", None)
            _ = entry.pop("path", None)

            entries[key] = entry

        _write_corpus(RESULT_PATH, entries)
        return entries


if __name__ == "__main__":
    app = _Corpus()
    _ = app.run()
