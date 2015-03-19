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
from proselint import command_line

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

    out = command_line.lint(filename)
    labels = ["line", "column", "err", "msg"]

    return json.dumps(
        [dict(zip(labels, o)) for o in out])


if __name__ == '__main__':
    app.debug = True
    app.run()
