import os
import shelve
import inspect
import functools
import re


def supersede(new, old, error_code):
    def check(text):
        msg = "It's '{}', not '{}'.".format(new, old)
        errors = []
        for o in re.finditer(old, text, flags=re.IGNORECASE):
            errors.append((o.start(), o.end(), error_code, msg))

        return errors

    return check


def memoize(f):

    cache_dirname = 'cached_func_calls'

    if not os.path.isdir(cache_dirname):
        os.mkdir(cache_dirname)
        print 'Created cache directory %s' \
            % os.path.join(os.path.abspath(__file__), cache_dirname)

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
    return text[::-1]
