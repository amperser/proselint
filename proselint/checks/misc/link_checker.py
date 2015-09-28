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

Check that links are not not broken.

"""
from tools import memoize
from future import standard_library
import re
try:
    import urllib.request as urllib_request  # for Python 3
except ImportError:
    import urllib2 as urllib_request         # for Python 2
from socket import error as SocketError
standard_library.install_aliases()


@memoize
def check(text):
    """Check the text."""
    err = "misc.link_checker"
    msg = u"Broken link: {}"

    regex = re.compile(
        r"""(?i)\b((?:https?://|www\d{0,3}[.]
        |[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+
        |(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)
        |[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019\u21a9]))""",
        re.U)

    errors = []
    for m in re.finditer(regex, text):
        url = m.group(0).strip()

        if "http://" not in url and "https://" not in url:
            url = "http://" + url

        if is_broken_link(url):
            errors.append((m.start(), m.end(), err, msg.format(url)))

    return errors


@memoize
def is_broken_link(url):
    """Determine whether the link returns a 404 error."""
    try:
        request = urllib_request.Request(
            url, headers={'User-Agent': 'Mozilla/5.0'})
        urllib_request.urlopen(request).read()
        return False
    except urllib_request.URLError:
        return True
    except SocketError:
        return True
