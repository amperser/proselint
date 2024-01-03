from timeit import timeit

import proselint

##################################################################
# Benchmark Hash-Algos
# -> on newer computer md5 is only slightly faster than sha256 (6%)
# -> choose sha224 for now (fastest on newer computers)
# TODO: test on old hw, x32
##################################################################

file_path = proselint.path / "demo.md"
f = file_path.open(encoding="utf-8", errors="replace")
text = f.read()

contenders = {
    "md5": "hashlib.md5(text.encode('utf-8')).hexdigest()",
    "sha1": "hashlib.sha1(text.encode('utf-8')).hexdigest()",
    "sha224": "hashlib.sha224(text.encode('utf-8')).hexdigest()",
    "sha256": "hashlib.sha256(text.encode('utf-8')).hexdigest()",
    "sha384": "hashlib.sha384(text.encode('utf-8')).hexdigest()",
    "sha512": "hashlib.sha512(text.encode('utf-8')).hexdigest()",
    "builtin": "hash(text)",
    "strhash": "text.__hash__()",
}

for _key, _val in contenders.items():
    _dur = timeit(_val, globals=globals(), number=1000)
    _hash = eval(_val)
    print(f"{_key} took {_dur * 1000:.2f} ms, result= {_hash}")
