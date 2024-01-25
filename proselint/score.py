"""Compute the lintscore on the corpus.
NOTE: relic, probably broken
"""


import os
import re
import subprocess  # noqa: S404
from pathlib import Path

from .config_paths import proselint_path
from .logger import log


def score(check=None):
    """Compute the linter's score on the corpus.

    Proselint's score reflects the desire to have a linter that catches many
    errors, but which takes false alarms seriously. It is better not to say
    something than to say the wrong thing, and the harm from saying the wrong
    thing is greater than the benefit of saying the right thing. Thus our score
    metric is defined as:

        TP * (TP / (FP + TP)) ^ k,

    where TP is the number of true positives (hits), FP is the number of
    false positives (false alarms), and k > 0 is a temperature parameter that
    determines the penalty for imprecision. In general, we should choose a
    large value of k, one that strongly discourages the creation of rules that
    can't be trusted. Suppose that k = 2. Then if the linter detects 100
    errors, of which 10 are false positives, the score is 81.
    """
    tp = 0
    fp = 0
    # corpus was removed in https://github.com/amperser/proselint/pull/186
    path_to_corpus = proselint_path.parent / "corpora" / "0.1.0"
    for root, _, files in os.walk(path_to_corpus):
        files_md = [f for f in files if f.endswith(".md")]
        root_path = Path(root)
        for file_md in files_md:
            fullpath = root_path / file_md

            # Run the linter.
            log.debug("Linting %s", file_md)
            out = subprocess.check_output(["proselint", fullpath])  # noqa: S603, S607
            # TODO: this can just call lint() ?!?

            # Determine the number of errors.
            regex = r".+?:(?P<line>\d+):(?P<col>\d+): (?P<message>.+)"
            num_errors = len(tuple(re.finditer(regex, out)))
            log.debug(" -> found %d errors.", num_errors)

            # Open the document.
            subprocess.call(["open", fullpath])  # noqa: S603, S607

            # Ask the scorer how many of the errors were false alarms?
            # TODO: this should not be manual - data can be stored in corpus
            input_val = None
            while not isinstance(input_val, int):
                try:
                    input_val = input("# of false alarms? ")
                    if input_val == "exit":
                        return None
                    input_val = int(input_val)
                    fp += input_val
                    tp += num_errors - input_val
                except ValueError:  # noqa: PERF203
                    pass

            log.debug(" -> currently %d hits and %d false alarms", tp, fp)

    if (tp + fp) > 0:
        return tp * (1.0 * tp / (tp + fp)) ** 2

    return 0
