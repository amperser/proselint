# -*- coding: utf-8 -*-
"""MSC404: Checks that links are viable.

---
layout:     post
error_code: MSC404
source:     SublimeLinter-annotations
source_url: http://bit.ly/16Q7H41
title:      broken links
date:       2014-06-10 12:31:19
categories: writing
---

Check that links are not not broken.

"""
from proselint.tools import memoize
import re
import urllib
from socket import error as SocketError


@memoize
def check(blob):
    """Check the text."""
    err = "ANN100"
    msg = u"Broken link: {}"

    regex = re.compile(
        r"""(?i)\b((?:https?://|www\d{0,3}[.]
        |[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+
        |(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)
        |[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019\u21a9]))""",
        re.U)

    errors = []
    for m in re.finditer(regex, blob.raw):
        url = m.group(0).strip()

        if "http://" not in url and "https://" not in url:
            url = "http://" + url

        if is_broken_link(url):
            errors.append((m.start(), m.end(), err, msg.format(url)))

    return errors


@memoize
def is_broken_link(url):
    """Check if the link return a 404 error."""
    try:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlopen(request).read()
        return False
    except urllib.error.URLError:
        return True
    except SocketError:
        return True
