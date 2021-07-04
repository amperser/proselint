# -*- coding: utf-8 -*-

"""General-purpose tools shared across linting checks."""

from __future__ import print_function
from __future__ import unicode_literals
import sys
import traceback
import os
import shelve
import inspect
import functools
import re
import hashlib
import json
import importlib
import copy

import dbm
_cache_shelves = dict()
proselint_path = os.path.dirname(os.path.realpath(__file__))
home_dir = os.path.expanduser("~")
cwd = os.getcwd()


def close_cache_shelves():
    """Close previously opened cache shelves."""
    for pth, cache in _cache_shelves.items():
        cache.close()
    _cache_shelves.clear()


def close_cache_shelves_after(f):
    """Decorate a function to ensure cache shelves are closed after call."""
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        f(*args, **kwargs)
        close_cache_shelves()
    return wrapped


def _get_xdg_path(variable_name, default_path):
    path = os.environ.get(variable_name)
    if path is None or path == '':
        return default_path
    else:
        return path


def _get_xdg_config_home():
    return _get_xdg_path('XDG_CONFIG_HOME', os.path.join(home_dir, '.config'))


def _get_xdg_cache_home():
    return _get_xdg_path('XDG_CACHE_HOME', os.path.join(home_dir, '.cache'))


def _get_cache(cachepath):
    if cachepath in _cache_shelves:
        return _cache_shelves[cachepath]

    try:
        cache = shelve.open(cachepath, protocol=2)
    except dbm.error:
        # dbm error on open - delete and retry
        print('Error (%s) opening %s - will attempt to delete and re-open.' %
              (sys.exc_info()[1], cachepath))
        try:
            os.remove(cachepath)
            cache = shelve.open(cachepath, protocol=2)
        except Exception:
            print('Error on re-open: %s' % sys.exc_info()[1])
            cache = None
    except Exception:
        # unknown error
        print('Could not open cache file %s, maybe name collision. '
              'Error: %s' % (cachepath, traceback.format_exc()))
        cache = None

    # Don't fail on bad caches
    if cache is None:
        print('Using in-memory shelf for cache file %s' % cachepath)
        cache = shelve.Shelf(dict())

    _cache_shelves[cachepath] = cache
    return cache


def memoize(f):
    """Cache results of computations on disk."""
    # Determine the location of the cache.
    cache_dirname = os.path.join(_get_xdg_cache_home(), 'proselint')
    legacy_cache_dirname = os.path.join(home_dir, ".proselint")

    if not os.path.isdir(cache_dirname):
        # Migrate the cache from the legacy path to XDG compliant location.
        if os.path.isdir(legacy_cache_dirname):
            os.rename(legacy_cache_dirname, cache_dirname)
        # Create the cache if it does not already exist.
        else:
            os.makedirs(cache_dirname)

    cache_filename = f.__module__ + "." + f.__name__
    cachepath = os.path.join(cache_dirname, cache_filename)

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
        cache = _get_cache(cachepath)

        try:
            return cache[key]
        except KeyError:
            value = f(*args, **kwargs)
            cache[key] = value
            cache.sync()
            return value
        except TypeError:
            call_to = f.__module__ + '.' + f.__name__
            print('Warning: could not disk cache call to %s;'
                  'it probably has unhashable args. Error: %s' %
                  (call_to, traceback.format_exc()))
            return f(*args, **kwargs)

    return wrapped


def get_checks(options):
    """Extract the checks."""
    sys.path.append(proselint_path)
    checks = []
    check_names = [key for (key, val)
                   in list(options["checks"].items()) if val]

    for check_name in check_names:
        module = importlib.import_module("checks." + check_name)
        for d in dir(module):
            if re.match("check", d):
                checks.append(getattr(module, d))

    return checks


def deepmerge_dicts(dict1, dict2):
    """Deep merge dictionaries, second dict will take priority."""
    result = copy.deepcopy(dict1)

    for key, value in dict2.items():
        if isinstance(value, dict):
            result[key] = deepmerge_dicts(result[key] or {}, value)
        else:
            result[key] = value

    return result


def load_options(config_file_path=None):
    """Read various proselintrc files, allowing user overrides."""
    system_config_paths = (
        '/etc/proselintrc',
        os.path.join(proselint_path, '.proselintrc'),
    )

    system_options = {}
    for path in system_config_paths:
        if os.path.isfile(path):
            system_options = json.load(open(path))
            break

    user_config_paths = [
        os.path.join(cwd, '.proselintrc'),
        os.path.join(_get_xdg_config_home(), 'proselint', 'config'),
        os.path.join(home_dir, '.proselintrc')
    ]
    if config_file_path:
        if not os.path.isfile(config_file_path):
            raise FileNotFoundError(
                f"Config file {config_file_path} does not exist")
        user_config_paths.insert(0, config_file_path)

    user_options = {}
    for path in user_config_paths:
        if os.path.isfile(path):
            user_options = json.load(open(path))
            break

    options = deepmerge_dicts(system_options, user_options)

    return options


def errors_to_json(errors):
    """Convert the errors to JSON."""
    out = []
    for e in errors:
        out.append({
            "check": e[0],
            "message": e[1],
            "line": 1 + e[2],
            "column": 1 + e[3],
            "start": 1 + e[4],
            "end": 1 + e[5],
            "extent": e[6],
            "severity": e[7],
            "replacements": e[8],
        })

    return json.dumps(
        dict(status="success", data={"errors": out}), sort_keys=True)


def line_and_column(text, position):
    """Return the line number and column of a position in a string."""
    position_counter = 0
    line_no = 0
    for line in text.splitlines(True):
        if (position_counter + len(line.rstrip())) >= position:
            break
        position_counter += len(line)
        line_no += 1
    return (line_no, position - position_counter)


def lint(input_file, debug=False, config_file_path=None):
    """Run the linter on the input file."""
    options = load_options(config_file_path)

    if isinstance(input_file, str):
        text = input_file
    else:
        text = input_file.read()

    # Get the checks.
    checks = get_checks(options)

    # Apply all the checks.
    errors = []
    for check in checks:

        result = check(text)

        for error in result:
            (start, end, check, message, replacements) = error
            (line, column) = line_and_column(text, start)
            if not is_quoted(start, text):
                errors += [(check, message, line, column, start, end,
                            end - start, "warning", replacements)]

        if len(errors) > options["max_errors"]:
            break

    # Sort the errors by line and column number.
    errors = sorted(errors[:options["max_errors"]], key=lambda e: (e[2], e[3]))

    return errors


def assert_error(text, check, n=1):
    """Assert that text has n errors of type check."""
    assert_error.description = "No {} error for '{}'".format(check, text)
    assert(check in [error[0] for error in lint(text)])


def consistency_check(text, word_pairs, err, msg, offset=0):
    """Build a consistency checker for the given word_pairs."""
    errors = []

    msg = " ".join(msg.split())

    for w in word_pairs:
        matches = [
            [m for m in re.finditer(w[0], text)],
            [m for m in re.finditer(w[1], text)]
        ]

        if len(matches[0]) > 0 and len(matches[1]) > 0:

            idx_minority = len(matches[0]) > len(matches[1])

            for m in matches[idx_minority]:
                errors.append((
                    m.start() + offset,
                    m.end() + offset,
                    err,
                    msg.format(w[~idx_minority], m.group(0)),
                    w[~idx_minority]))

    return errors


def preferred_forms_check(text, list, err, msg, ignore_case=True, offset=0,
                          max_errors=float("inf")):
    """Build a checker that suggests the preferred form."""
    if ignore_case:
        flags = re.IGNORECASE
    else:
        flags = 0

    msg = " ".join(msg.split())

    errors = []
    regex = r"[\W^]{}[\W$]"
    for p in list:
        for r in p[1]:
            for m in re.finditer(regex.format(r), text, flags=flags):
                txt = m.group(0).strip()
                errors.append((
                    m.start() + 1 + offset,
                    m.end() + offset,
                    err,
                    msg.format(p[0], txt),
                    p[0]))

    errors = truncate_to_max(errors, max_errors)

    return errors


def existence_check(text, list, err, msg, ignore_case=True,
                    str=False, max_errors=float("inf"), offset=0,
                    require_padding=True, dotall=False,
                    excluded_topics=None, exceptions=[], join=False):
    """Build a checker that prohibits certain words or phrases."""
    flags = 0

    msg = " ".join(msg.split())

    if ignore_case:
        flags = flags | re.IGNORECASE

    if str:
        flags = flags | re.UNICODE

    if dotall:
        flags = flags | re.DOTALL

    if require_padding:
        regex = r"(?:^|\W){}[\W$]"
    else:
        regex = r"{}"

    errors = []

    # If the topic of the text is in the excluded list, return immediately.
    if excluded_topics:
        tps = topics(text)
        if any([t in excluded_topics for t in tps]):
            return errors

    rx = "|".join(regex.format(w) for w in list)
    for m in re.finditer(rx, text, flags=flags):
        txt = m.group(0).strip()
        if any([re.search(exception, txt) for exception in exceptions]):
            continue
        errors.append((
            m.start() + 1 + offset,
            m.end() + offset,
            err,
            msg.format(txt),
            None))

    errors = truncate_to_max(errors, max_errors)

    return errors


def truncate_to_max(errors, max_errors):
    """If max_errors was specified, truncate the list of errors.

    Give the total number of times that the error was found elsewhere.
    """
    if len(errors) > max_errors:
        start1, end1, err1, msg1, replacements = errors[0]

        if len(errors) == (max_errors + 1):
            msg1 += " Found once elsewhere."
        else:
            msg1 += " Found {} times elsewhere.".format(len(errors))

        errors = errors[1:max_errors]
        errors = [(start1, end1, err1, msg1, replacements)] + errors

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
