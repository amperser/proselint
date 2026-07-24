#!/usr/bin/env python3
"""Calculate a lint score which we use to evaluate proselint's performance."""

from dataclasses import asdict, dataclass
from json import dumps, loads
from os.path import curdir
from pathlib import Path

from proselint.checks import __register__
from proselint.registry import CheckRegistry

import corpus.scripts.generate_readme_corpus as corpus

CheckRegistry().register_many(__register__)

ROOT_DIR = Path(curdir).resolve()
CORPUS_DIR = Path(ROOT_DIR) / "corpus" / "works"
RESULT_PATH = Path(ROOT_DIR) / "corpus.json"


@dataclass
class Detection:
    at: int 
    line: int
    column: int
    checkName: str

@dataclass 
class Work(corpus.Metadata):
    positives: list[Detection]

@dataclass
class Result:
    detections: dict[str, Work]


def score(positives: int, falses: int, k: float = 2.0) -> float:
    """
    T (T / (F + T)) k.

    T = True positives
    F = False positives
    k = Imprecision temperature (k > 0)
    """
    return positives / (falses + positives) * k


def detect():
    """
    TODO: Run proselint
    """
    pass


if __name__ == "__main__":
    result = (
        loads(RESULT_PATH.read_text(encoding="utf-8")) if RESULT_PATH.exists() else {}
    )

    for entry in CORPUS_DIR.glob("*"):
        metadata = corpus.parse_entry(entry)
        data = Work(
            work=metadata.meta.work,
            author=metadata.meta.author,
            source=metadata.meta.source,
            positives=[],
        )

        key = str(metadata.path.relative_to(ROOT_DIR))

        if key not in result:
            value = asdict(data)

            value.pop("content", None)
            value.pop("path", None)

            result[key] = value

    RESULT_PATH.write_text(dumps(result, indent=2, default=str), encoding="utf-8")
