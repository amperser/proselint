"""Web app that serves proselint's API."""

from flask import Flask, request
import subprocess
from flask_cors import CORS, cross_origin
import uuid
import os
import re
import urllib2
import json
import io

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Origin, X-Requested-With, Content-Type, Accept"


@app.route('/v1/', methods=['GET', 'POST'])
@cross_origin()  # allow all origins all methods.
def lint():
    """Run linter on the provided text and return the results."""
    id = uuid.uuid4()
    filename = os.path.join("tmp", "{}.md".format(id))

    text = urllib2.unquote(request.values['text'])

    with io.open(filename, "w+", encoding='utf8') as f:
        f.write(text)

    out = subprocess.check_output("proselint {}".format(filename), shell=True)

    r = re.compile(
        "(?:.*).md:(?P<line>\d*):(?P<column>\d*): (?P<err>\w{6}) (?P<msg>.*)")

    out2 = sorted([r.search(line).groupdict() for line in out.splitlines()])

    return json.dumps(out2)


if __name__ == '__main__':
    app.debug = True
    app.run()
