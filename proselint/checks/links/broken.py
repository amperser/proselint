# -*- coding: utf-8 -*-
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
from proselint.tools import memoize
import re
from urllib import error, request
from socket import error as SocketError


@memoize
def check(text):
    """Check the text."""
    err = "links.broken"
    msg = u"Broken link: {}"

    regex = re.compile(
        r"""(?i)\b((?:https?://|www\d{0,3}[.]
        |[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+
        |(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)
        |[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019\u21a9]))""",
        re.U | re.X)

    errors = []
    for m in re.finditer(regex, text):
        url = m.group(0).strip()

        if "http://" not in url and "https://" not in url:
            url = "http://" + url

        if is_broken_link(url):
            errors.append((m.start(), m.end(), err, msg.format(url), None))

    return errors


def is_broken_link(url):
    """Determine whether the link returns a 404 error."""
    try:
        req = request.Request(
            url, headers={'User-Agent': 'Mozilla/5.0'})
        request.urlopen(req).read()
        return False
    except (error.URLError, SocketError):
        return True
