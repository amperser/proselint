from flask import Flask, request, make_response, current_app
import subprocess
import uuid
import os
import re
import json
from datetime import timedelta
from functools import update_wrapper

app = Flask(__name__)


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        f.required_methods = ['OPTIONS']
        return update_wrapper(wrapped_function, f)
    return decorator


@app.route('/v1/', methods=["GET"])
@crossdomain(origin='*', headers=['Origin, X-Requested-With, Content-Type, Accept'])
def lint():

    id = uuid.uuid4()
    filename = os.path.join("tmp", "{}.md".format(id))

    with open(filename, "w+") as f:
        f.write(request.values['text'])

    out = subprocess.check_output("proselint {}".format(filename), shell=True)

    r = re.compile(
        "(?:.*).md:(?P<line>\d*):(?P<column>\d*): (?P<err>\w{6}) (?P<msg>.*)")

    out2 = sorted([r.search(line).groupdict() for line in out.splitlines()])

    return json.dumps(out2)


if __name__ == '__main__':
    app.debug = True
    app.run()
