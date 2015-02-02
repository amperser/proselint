"""General-purpose tools shared across linting checks."""
import os
import shelve
import inspect
import functools


def memoize(f):
    """Cache results of computations on disk."""
    path_of_this_file = os.path.dirname(os.path.realpath(__file__))
    cache_dirname = os.path.join(path_of_this_file, "cache")

    if not os.path.isdir(cache_dirname):
        os.mkdir(cache_dirname)

    cache_filename = f.__module__ + f.__name__
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


@memoize
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
