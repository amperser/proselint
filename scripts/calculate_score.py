#!/usr/bin/env python3
"""Calculate a lint score which we use to evaluate proselint's performance."""

from scripts.review_corpus import RESULT_PATH, read_corpus


def _score(positives: int, falses: int, k: float = 2.0) -> float:
    """
    T (T / (F + T)) k.

    T = True positives
    F = False positives
    k = Imprecision temperature (k > 0)
    """
    return positives / (falses + positives) * k


if __name__ == "__main__":
    detections = [
        d
        for entry in read_corpus(RESULT_PATH).values()
        for d in entry["detections"]
    ]

    positives = sum(d["marked"] for d in detections)

    print(
        _score(positives, len(detections) - positives)
        if detections
        else "No detections to score."
    )
