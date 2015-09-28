#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""General-purpose tools shared across linting checks."""
from __future__ import print_function
from __future__ import unicode_literals
import os
import shelve
import inspect
import functools
import re
import hashlib


def memoize(f):
    """Cache results of computations on disk."""
    path_of_this_file = os.path.dirname(os.path.realpath(__file__))

    # Determine the location of the cache.
    cache_dirname = os.path.join(path_of_this_file, "cache")

    # Create the cache if it does not already exist.
    if not os.path.isdir(cache_dirname):
        os.mkdir(cache_dirname)

    cache_filename = f.__module__ + "." + f.__name__
    cachepath = os.path.join(cache_dirname, cache_filename)

    try:
        cache = shelve.open(cachepath, protocol=2)
    except:
        print('Could not open cache file %s, maybe name collision' % cachepath)
        cache = None

    @functools.wraps(f)
    def wrapped(*args, **kwargs):

        # handle instance methods
        if hasattr(f, '__self__'):
            args = args[1:]

        signature = (f.__module__ + '.' + f.__name__).encode("utf-8")

        tempargdict = inspect.getcallargs(f, *args, **kwargs)

        for item in list(tempargdict.items()):
            signature += item[1].encode("utf-8")

        key = hashlib.sha256(signature).hexdigest()

        try:
            return cache[key]
        except KeyError:
            value = f(*args, **kwargs)
            cache[key] = value
            cache.sync()
            return value
        except TypeError:
            call_to = f.__module__ + '.' + f.__name__
            print(['Warning: could not disk cache call to ',
                   '%s; it probably has unhashable args'] % (call_to))
            return f(*args, **kwargs)

    return wrapped


def reverse(text):
    """Reverse a string. This is here as a demo of memoization."""
    return text[::-1]


def line_and_column(text, position):
    """Return the line number and column of a position in a string."""
    position_counter = 0
    for idx_line, line in enumerate(text.splitlines(True)):
        if (position_counter + len(line.rstrip())) > position:
            return (idx_line, position - position_counter)
        else:
            position_counter += len(line)


def consistency_check(text, word_pairs, err, msg, offset=0):
    """Build a consistency checker for the given word_pairs."""
    errors = []
    for w in word_pairs:
        match1 = [m for m in re.finditer(w[0], text)]
        match2 = [m for m in re.finditer(w[1], text)]

        if len(match1) > 0 and len(match2) > 0:

            if len(match1) > len(match2):
                for m in match2:
                    errors.append((
                        m.start() + offset,
                        m.end() + offset,
                        err,
                        msg.format(m.group(0), w[0])))
            else:
                for m in match1:
                    errors.append((
                        m.start() + offset,
                        m.end() + offset,
                        err,
                        msg.format(m.group(0), w[1])))

    return errors


def preferred_forms_check(text, list, err, msg, ignore_case=True, offset=0):
    """Build a checker that suggests the preferred form."""
    if ignore_case:
        flags = re.IGNORECASE
    else:
        flags = 0

    errors = []
    regex = u"[\W^]{}[\W$]"
    for p in list:
        for r in p[1]:
            for m in re.finditer(regex.format(r), text, flags=flags):
                txt = m.group(0).strip()
                errors.append((
                    m.start() + 1 + offset,
                    m.end() + offset,
                    err,
                    msg.format(p[0], txt)))

    return errors


def existence_check(text, list, err, msg, ignore_case=True,
                    str=False, max_errors=float("inf"), offset=0,
                    require_padding=True, dotall=False,
                    excluded_topics=None, join=False):
    """Build a checker that blacklists certain words."""
    flags = 0

    if ignore_case:
        flags = flags | re.IGNORECASE

    if str:
        flags = flags | re.UNICODE

    if dotall:
        flags = flags | re.DOTALL

    if require_padding:
        regex = u"(?:^|\W){}[\W$]"
    else:
        regex = u"{}"

    errors = []

    # If the topic of the text is in the excluded list, return immediately.
    if excluded_topics:
        tps = topics(text)
        if any([t in excluded_topics for t in tps]):
            return errors

    rx = "|".join(regex.format(w) for w in list)
    for m in re.finditer(rx, text, flags=flags):
        txt = m.group(0).strip()
        errors.append((
            m.start() + 1 + offset,
            m.end() + offset,
            err,
            msg.format(txt)))

    # If max_errors was specified, truncate the list of errors and let the
    # user know the total number of times that the error was found elsewhere.
    if len(errors) > max_errors:
        start1, end1, err1, msg1 = errors[0]

        if len(errors) == (max_errors + 1):
            msg1 += " Found once elsewhere."
        else:
            msg1 += " Found {} times elsewhere.".format(len(errors))

        errors = errors[1:max_errors]
        errors = [(start1, end1, err1, msg1)] + errors

    return errors


def is_quoted(position, text):
    """Determine if the position in the text falls within a quote."""
    def matching(quotemark1, quotemark2):
        straight = '\"\''
        curly = '“”'
        if quotemark1 in straight and quotemark2 in straight:
            return True
        if quotemark1 in curly and quotemark2 in curly:
            return True
        else:
            return False

    def find_ranges(text):
        s = 0
        q = pc = ''
        start = None
        ranges = []
        seps = " .,:;-\r\n"
        quotes = ['\"', '“', '”', "'"]
        for i, c in enumerate(text + "\n"):
            if s == 0 and c in quotes and pc in seps:
                start = i
                s = 1
                q = c
            elif s == 1 and matching(c, q):
                s = 2
            elif s == 2:
                if c in seps:
                    ranges.append((start+1, i-1))
                    start = None
                    s = 0
                else:
                    s = 1
            pc = c
        return ranges

    def position_in_ranges(ranges, position):
        for start, end in ranges:
            if start <= position < end:
                return True
        return False

    return position_in_ranges(find_ranges(text), position)


def detector_50_Cent(text):
    """Determine whether 50 Cent is a topic."""
    keywords = [
        "50 Cent",
        "rap",
        "hip hop",
        "Curtis James Jackson III",
        "Curtis Jackson",
        "Eminem",
        "Dre",
        "Get Rich or Die Tryin'",
        "G-Unit",
        "Street King Immortal",
        "In da Club",
        "Interscope",
    ]
    num_keywords = sum(word in text for word in keywords)
    return ("50 Cent", float(num_keywords > 2))


def topics(text):
    """Return a list of topics."""
    detectors = [
        detector_50_Cent
    ]
    ts = []
    for detector in detectors:
        ts.append(detector(text))

    return [t[0] for t in ts if t[1] > 0.95]


def context(text, position, level="paragraph"):
    """Get sentence or paragraph that surrounds the given position."""
    if level == "sentence":
        pass
    elif level == "paragraph":
        pass

    return ""
