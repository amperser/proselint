"""Web app that serves proselint's API."""

from flask import Flask, request
import subprocess
from flask_cors import CORS, cross_origin
import uuid
import os
import re
import json
try:
    # For Python 3.0 and later
    from urllib.parse import unquote
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import unquote


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Origin, X-Requested-With, Content-Type, Accept"


@app.route('/v1/', methods=['GET', 'POST'])
@cross_origin()  # allow all origins all methods.
def lint():
    """Run linter on the provided text and return the results."""
    id = uuid.uuid4()
    filename = os.path.join("tmp", "{}.md".format(id))

    text = unquote(request.values['text'])

    with open(filename, "w+") as f:
        f.write(text)

    out = subprocess.check_output("proselint {}".format(filename), shell=True)

    r = re.compile(
        "(?:.*).md:(?P<line>\d*):(?P<column>\d*): (?P<err>\w{6}) (?P<msg>.*)")

    out2 = sorted([r.search(line).groupdict() for line in out.splitlines()])

    return json.dumps(out2)


if __name__ == '__main__':
    app.debug = True
    app.run()
