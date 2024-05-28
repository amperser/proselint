"""
learnings
- fast-string is the fastest, but not usable for proselint
  -> execution is tied to creation
- %-Op (ancient) seems like the fastest option

Consider to precalc the complete regex, as the existence_check
still does a lot of formatting and joining each time. fixing the slowest
contenders to speed up multi-file lints. best would be constant expressions
functions known from c++


class constant(object):
    __slots__ = ()
    val = 457

Const = namedtuple("c", ["val"])
const = Const(val=457)

-> both seem to make val constant!, same as a named
TODO: explore further
"""
from string import Template
from timeit import timeit

print("\n################### formatting")


msg1 = "[fmt]"
msg2 = "pad me"
tmp = Template(" $m1: $m2 ")

contenders = {
    "str.concat": "_e = ' ' + msg1 + ': ' + msg2 + ' '",
    "str.format()": "_e = ' {}: {} '.format(msg1, msg2)",
    "%-operation": "_e = ' %s: %s ' % (msg1, msg2)",
    "fast-sting": "_e = f' {msg1}: {msg2} '",
    "template-str": "_e = tmp.substitute(m1=msg1, m2=msg2)",
}

for _name, _code in contenders.items():
    _dur = timeit(stmt=_code, globals=locals())
    print(f"{_name} took {_dur * 1000:.2f} ms")

print("\n################### joining")

_el = ["one", "two", "three", "four", "five"]
_et = ("one", "two", "three", "four", "five")
_ef = frozenset(["one", "two", "three", "four", "five"])
_glue = " | "

contenders = {
    "str.join-list": "_e = _glue.join(_el)",
    "str.join-tuple": "_e = _glue.join(_et)",
    "str.join-frozenset": "_e = _glue.join(_ef)",
}

for _name, _code in contenders.items():
    _dur = timeit(stmt=_code, globals=locals())
    print(f"{_name} took {_dur * 1000:.2f} ms")
