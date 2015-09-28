#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Compute the lintscore on the corpus."""

from __future__ import print_function
from builtins import input
from builtins import int

import os
import subprocess
import re

proselint_path = os.path.dirname(os.path.realpath(__file__))


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
    large value of k, one that strongly discourages the creatiion of rules that
    can't be trusted. Suppose that k = 2. Then if the linter detects 100
    errors, of which 10 are false positives, the score is 81.
    """
    tp = 0
    fp = 0

    parent_directory = os.path.dirname(proselint_path)
    path_to_corpus = os.path.join(parent_directory, "corpora", "0.1.0")
    for root, _, files in os.walk(path_to_corpus):
        files = [f for f in files if f.endswith(".md")]
        for f in files:
            fullpath = os.path.join(root, f)

            # Run the linter.
            print("Linting {}".format(f))
            out = subprocess.check_output(
                "proselint {}".format(fullpath), shell=True)

            # Determine the number of errors.
            regex = r".+?:(?P<line>\d+):(?P<col>\d+): (?P<message>.+)"
            num_errors = len(tuple(re.finditer(regex, out)))
            print("Found {} errors.".format(num_errors))

            # Open the document.
            subprocess.call("{} {}".format("open", fullpath), shell=True)

            # Ask the scorer how many of the errors were false alarms?
            input_val = None
            while not isinstance(input_val, int):
                try:
                    input_val = input("# of false alarms? ")
                    if input_val == "exit":
                        return
                    else:
                        input_val = int(input_val)
                        fp += input_val
                        tp += (num_errors - input_val)
                except:
                    pass

            print("Currently {} hits and {} false alarms\n---".format(tp, fp))

    if (tp + fp) > 0:
        return tp * (1.0 * tp / (tp + fp)) ** 2
    else:
        return 0
