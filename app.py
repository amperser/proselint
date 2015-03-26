"""Web app that serves proselint's API."""

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from flask_limiter import Limiter
import uuid
import os
import urllib2
import io
from proselint import command_line
from rq import Queue
from worker import conn

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Origin, X-Requested-With, Content-Type, Accept"
limiter = Limiter(app, global_limits=["600 per hour"])

q = Queue(connection=conn)


def worker_function(text):
    """Lint the text using a worker dyno."""
    id = uuid.uuid4()
    filename = os.path.join("tmp", "{}.md".format(id))
    with io.open(filename, "w+", encoding='utf8') as f:
        f.write(text)

    return command_line.lint(filename)


@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(
        jsonify(status="error", message="Rate limit exceeded."), 429
    )


@app.route('/v1/', methods=['GET', 'POST'])
@limiter.limit("60 per minute")
@cross_origin()  # allow all origins all methods.
def lint():
    """Run linter on the provided text and return the results."""
    if 'text' in request.values:
        text = urllib2.unquote(request.values['text'])
        job = q.enqueue(worker_function, text)

        return jsonify(job_id=job.id), 202

    elif 'job_id' in request.values:
        job = q.fetch_job(request.values['job_id'])

        if not job:
            return jsonify(
                status="error",
                message="No job with requested job_id."), 404

        elif job.result is None:
            return jsonify(
                status="error",
                message="Job is not yet ready."), 202

        else:
            errors = []
            for i, e in enumerate(job.result):
                app.logger.debug(e)
                errors.append({
                    "check": e[0],
                    "message": e[1],
                    "line": e[2],
                    "column": e[3],
                    "start": e[4],
                    "end": e[5],
                    "extent": e[5] - e[4],
                    "severity": e[7],
                    "replacements": e[8],
                })
            return jsonify(
                status="success",
                data={"errors": errors})


if __name__ == '__main__':
    app.debug = True
    app.run()
