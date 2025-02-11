"""General-purpose tools shared across linting checks."""

import copy
import functools
import importlib
import json
import os
import re
import sys
from warnings import showwarning as warn

from . import config

proselint_path = os.path.dirname(os.path.realpath(__file__))
home_dir = os.path.expanduser("~")
cwd = os.getcwd()


def _get_xdg_path(variable_name, default_path):
    path = os.environ.get(variable_name)
    if path is None or path == '':
        return default_path
    else:
        return path


def _get_xdg_config_home():
    return _get_xdg_path('XDG_CONFIG_HOME', os.path.join(home_dir, '.config'))


def get_checks(options):
    """Extract the checks."""
    sys.path.append(proselint_path)
    checks = []
    check_names = [key for (key, val) in options["checks"].items() if val]

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


def load_options(config_file_path=None, conf_default=None):
    """Read various proselintrc files, allowing user overrides."""
    conf_default = conf_default or {}
    if os.path.isfile("/etc/proselintrc"):
        conf_default = json.load(open("/etc/proselintrc"))

    user_config_paths = [
        os.path.join(cwd, '.proselintrc.json'),
        os.path.join(_get_xdg_config_home(), 'proselint', 'config.json'),
        os.path.join(home_dir, '.proselintrc.json')
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
        oldpath = path.replace(".json", "")
        if os.path.isfile(oldpath):
            warn(f"{oldpath} was found instead of a JSON file."
                 f" Rename to {path}.", DeprecationWarning, "", 0)
            user_options = json.load(open(oldpath))
            break

    return deepmerge_dicts(conf_default, user_options)


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
        {"status": "success", "data": {"errors": out}}, sort_keys=True)


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


def lint(input_file, debug=False, config=config.default):
    """Run the linter on the input file."""
    if isinstance(input_file, str):
        text = input_file
    else:
        text = input_file.read()

    # Get the checks.
    checks = get_checks(config)

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

        if len(errors) > config["max_errors"]:
            break

    # Sort the errors by line and column number.
    errors = sorted(errors[:config["max_errors"]], key=lambda e: (e[2], e[3]))

    return errors


def assert_error(text, check, n=1):
    """Assert that text has n errors of type check."""
    assert_error.description = f"No {check} error for '{text}'"
    assert len([error[0] for error in lint(text) if error[0] == check]) == n


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


def preferred_forms_check(text, list, err, msg, ignore_case=True, offset=0):
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

    return errors


def existence_check(
    text,
    list,
    err,
    msg,
    ignore_case=True,
    str=False,
    offset=0,
    require_padding=True,
    dotall=False,
    exceptions=(),
    join=False,
):
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

    return errors


def _allowed_word(permitted, match: re.Match, /, ignore_case=True):
    """Determine if a match object result is in a set of strings."""
    matched = match.string[match.start():match.end()]
    if ignore_case:
        return matched.lower() in permitted
    return matched in permitted


def reverse_existence_check(
    text, list, err, msg, ignore_case=True, offset=0
):
    """Find all words in ``text`` that aren't on the ``list``."""
    permitted = set([word.lower() for word in list] if ignore_case else list)
    allowed_word = functools.partial(
        _allowed_word, permitted, ignore_case=ignore_case)

    # Match all 3+ character words that contain a hyphen or apostrophe
    # only in the middle (not as the first or last character)
    tokenizer = re.compile(r"\w[\w'-]+\w")

    # Ignore any that contain numerals
    exclusions = re.compile(r'\d')

    errors = [
        (
            m.start() + 1 + offset,
            m.end() + offset,
            err,
            msg.format(m.string[m.start():m.end()]),
            None
        )
        for m in tokenizer.finditer(text)
        if (
            not exclusions.search(m.string[m.start():m.end()])
            and not allowed_word(m)
        )
    ]
    return errors


def max_errors(limit):
    """Decorate a check to truncate error output to a specified limit."""
    def wrapper(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            return truncate_errors(f(*args, **kwargs), limit)
        return wrapped
    return wrapper


def truncate_errors(errors, limit=float("inf")):
    """If limit was specified, truncate the list of errors.

    Give the total number of times that the error was found elsewhere.
    """
    if len(errors) > limit:
        start1, end1, err1, msg1, replacements = errors[0]

        if len(errors) == limit + 1:
            msg1 += " Found once elsewhere."
        else:
            msg1 += f" Found {len(errors)} times elsewhere."

        errors = [(start1, end1, err1, msg1, replacements)] + errors[1:limit]

    return errors


def ppm_threshold(threshold):
    """Decorate a check to error if the PPM threshold is surpassed."""
    def wrapped(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            return threshold_check(f(*args, **kwargs), threshold, len(args[0]))
        return wrapper
    return wrapped


def threshold_check(errors, threshold, length):
    """Check that returns an error if the PPM threshold is surpassed."""
    if length > 0:
        errcount = len(errors)
        ppm = (errcount / length) * 1e6

        if ppm >= threshold and errcount >= 1:
            return [errors[0]]
    return []


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


def context(text, position, level="paragraph"):
    """Get sentence or paragraph that surrounds the given position."""
    if level == "sentence":
        pass
    elif level == "paragraph":
        pass

    return ""
