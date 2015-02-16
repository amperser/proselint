"""General-purpose tools shared across linting checks."""
import os
import shelve
import inspect
import functools
import re


def memoize(f):
    """Cache results of computations on disk."""
    path_of_this_file = os.path.dirname(os.path.realpath(__file__))
    cache_dirname = os.path.join(path_of_this_file, "cache")

    if not os.path.isdir(cache_dirname):
        os.mkdir(cache_dirname)

    cache_filename = f.__module__ + "." + f.__name__
    cachepath = os.path.join(cache_dirname, cache_filename)

    try:
        cache = shelve.open(cachepath, protocol=2)
    except:
        print 'Could not open cache file %s, maybe name collision' % cachepath
        cache = None

    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        argdict = {}

        # handle instance methods
        if hasattr(f, '__self__'):
            args = args[1:]

        tempargdict = inspect.getcallargs(f, *args, **kwargs)

        for k, v in tempargdict.iteritems():
            argdict[k] = v

        key = str(hash(frozenset(argdict.items())))

        try:
            return cache[key]
        except KeyError:
            value = f(*args, **kwargs)
            cache[key] = value
            cache.sync()
            return value
        except TypeError:
            call_to = f.__module__ + '.' + f.__name__
            print ['Warning: could not disk cache call to ',
                   '%s; it probably has unhashable args'] % (call_to)
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


def consistency_check(text, word_pairs, err, msg):
    """Build a consistency checker for the given word_pairs."""
    errors = []
    for w in word_pairs:
        match1 = [m for m in re.finditer(w[0], text)]
        match2 = [m for m in re.finditer(w[1], text)]

        if len(match1) > 0 and len(match2) > 0:

            if len(match1) > len(match2):
                for m in match2:
                    errors.append((m.start(), m.end(), err,
                                  msg.format(m.group(0), w[0])))
            else:
                for m in match1:
                    errors.append((m.start(), m.end(), err,
                                  msg.format(m.group(0), w[1])))

    return errors


def preferred_forms_check(text, list, err, msg):
    """Build a checker that suggests the preferred form."""
    errors = []
    for p in list:
        for r in p[1]:
            for m in re.finditer(u"\s{}\s".format(r), text, flags=re.I):
                txt = m.group(0).strip()
                errors.append((m.start(), m.end(), err, msg.format(p[0], txt)))

    return errors


def existence_check(text, list, err, msg, ignore_case=True, unicode=False):
    """Build a checker that blacklists certain words."""
    flags = 0

    if ignore_case and unicode:
        flags = re.IGNORECASE | re.UNICODE
    elif ignore_case:
        flags = re.IGNORECASE
    elif unicode:
        flags = re.UNICODE
    else:
        flags = 0

    errors = []
    for w in list:
        for m in re.finditer(u"\s{}\s".format(w), text, flags=flags):
            txt = m.group(0).strip()
            errors.append((m.start(), m.end(), err, msg.format(txt)))

    return errors
