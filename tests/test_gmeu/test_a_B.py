#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Test GMEU entry 'a', part B."""

from proselint.tools import assert_error
from nose import SkipTest


def test_a_distributive():
    """Use a over per in the distributive sense."""
    raise SkipTest

    sentences = [
        "An apple per day keeps the doctor away.",
        "I sleep eight hours per night.",
        "Their policy allows one golf cart a couple.",
        "The company donated five books a student.",
        "Our a-unit cost is less than $1000.",
        "The $50-a-parent fee seems unreasonably high."
    ]

    error_check_name = "misc.a_distributive"

    for sentence in sentences:
        yield assert_error, sentence, error_check_name
