"""Web app that serves proselint's API."""

from flask import Flask, request
from flask_cors import CORS, cross_origin
import uuid
import os
import urllib2
import json
import io
from proselint import command_line
from rq import Queue
from worker import conn

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Origin, X-Requested-With, Content-Type, Accept"
app.config["DEBUG"] = True

q = Queue(connection=conn)


@app.route('/v1/', methods=['GET', 'POST'])
@cross_origin()  # allow all origins all methods.
def lint():
    """Run linter on the provided text and return the results."""
    if 'text' in request.values:

        id = uuid.uuid4()
        filename = os.path.join("tmp", "{}.md".format(id))

        text = urllib2.unquote(request.values['text'])

        with io.open(filename, "w+", encoding='utf8') as f:
            f.write(text)

        job = q.enqueue(command_line.lint, filename)

        return json.dumps({"job_id": job.id})

    elif 'job_id' in request.values:

        job = q.fetch_job(request.values['job_id'])

        if not job:
            return json.dumps("expired")
        elif not job.result:
            return json.dumps("not done yet")
        else:
            labels = ["line", "column", "err", "msg"]
            return json.dumps([dict(zip(labels, o)) for o in job.result])


if __name__ == '__main__':
    app.debug = True
    app.run()
