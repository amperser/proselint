"""Checks that links are viable.

---
layout:     post
source:     SublimeLinter-annotations
source_url: http://bit.ly/16Q7H41
title:      broken links
date:       2014-06-10
categories: writing
---

Check that links are not broken.

"""
from __future__ import annotations

import asyncio
import re
import urllib.request as ulr
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from proselint.checks import ResultCheck

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "General url short www.github.com should work",
    "Url long insecure http://docs.python.org.",
    "Long secure Url like https://en.wikipedia.org",
]

examples_fail = [
    "You can't visit www.thiswebsitedoesreallynotexist.org now.",
    "You can't visit http://www.thiswebsitedoesreallynotexist.org now.",
    "You can't visit https://www.thiswebsitedoesreallynotexist.org now.",
]


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "links.broken"
    msg = "Broken link: {}"

    regex = re.compile(
        r"""(?i)\b((?:https?://|www\d{0,3}[.]
        |[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+
        |(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)
        |[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019\u21a9]))""",
        re.UNICODE | re.VERBOSE,
    )  # TODO: update regex?

    results: list[ResultCheck] = []
    for m in re.finditer(regex, text):
        url = m.group(0).strip()

        if "http://" not in url and "https://" not in url:
            url = "http://" + url

        if is_broken_link(url):
            results.append((m.start(), m.end(), err, msg.format(url), None))
            asyncio.sleep(0.1)

    return results


def is_broken_link(url: str) -> bool:
    """Determine whether the link returns a 404 error."""
    try:
        # TODO: update header?
        request = ulr.Request(url, headers={"User-Agent": "Mozilla/5.0"})  # noqa: S310
        ulr.urlopen(request).read()  # noqa: S310
        return False
    except ulr.URLError:
        return True
    except OSError:
        return True
