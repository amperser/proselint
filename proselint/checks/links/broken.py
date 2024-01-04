"""Checks that links are viable.

---
layout:     post
source:     SublimeLinter-annotations
source_url: http://bit.ly/16Q7H41
title:      broken links
date:       2014-06-10 12:31:19
categories: writing
---

Check that links are not broken.

"""
from __future__ import annotations

import re
import urllib.request as urllib_request  # for Python 3
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from proselint.checks import ResultCheck


def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "links.valid"
    msg = "Broken link: {}"

    regex = re.compile(
        r"""(?i)\b((?:https?://|www\d{0,3}[.]
        |[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+
        |(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)
        |[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019\u21a9]))""",
        re.U | re.X,
    )

    results: list[ResultCheck] = []
    for m in re.finditer(regex, text):
        url = m.group(0).strip()

        if "http://" not in url and "https://" not in url:
            url = "http://" + url

        if is_broken_link(url):
            results.append((m.start(), m.end(), err, msg.format(url), None))
        # TODO: this should probably be rate limited (10/s)?

    return results


def is_broken_link(url: str) -> bool:
    """Determine whether the link returns a 404 error."""
    try:
        request = urllib_request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        urllib_request.urlopen(request).read()
        return False
    except urllib_request.URLError:
        return True
    except OSError:
        return True
