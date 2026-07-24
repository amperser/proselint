#!/usr/bin/env python3
"""Calculate a lint score which we use to evaluate proselint's performance."""

from os.path import curdir
from pathlib import Path

from proselint.checks import __register__
from proselint.registry import CheckRegistry

CheckRegistry().register_many(__register__)

ROOT_DIR = Path(curdir).resolve()
CORPUS_DIR = Path(ROOT_DIR) / "corpora"


def score(positives: int, falses: int, k: float = 2.0) -> float:
    """
    T (T / (F + T)) k.

    T = True positives
    F = False positives
    k = Imprecision temperature (k > 0)
    """
    return positives / (falses + positives) * k


if __name__ == "__main__":
    pass
