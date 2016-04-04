"""Web app that serves proselint's API."""

from flask import Flask, request, jsonify, make_response, Response
from flask_cors import CORS, cross_origin
from flask_limiter import Limiter
from functools import wraps
from future.moves.urllib.parse import unquote
import hashlib
import proselint
from rq import Queue
from worker import conn


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = "Origin, X-Requested-With, Content-Type, Accept"
limiter = Limiter(app)

q = Queue(connection=conn)


def worker_function(text):
    """Lint the text using a worker dyno."""
    return proselint.tools.lint(text)


@app.errorhandler(429)
def ratelimit_handler(e):
    """Inform user that the rate limit has been exceeded."""
    return make_response(
        jsonify(status="error", message="Rate limit exceeded."), 429)


def check_auth(username, password):
    """Check if a username / password combination is valid."""
    legal_hashes = [
        "15a7fdade5fa58d38c6d400770e5c0e948fbc03ba365b704a6d205687738ae46",
        "057b24043181523e3c3717071953c575bd13862517a8ce228601582a9cbd9dae",
        "c8d79ae7d388b6da21cb982a819065b18941925179f88041b87de2be9bcde79c",
        "bb7082271060c91122de8a3bbac5c7d6dcfe1a02902d57b27422f0062f602f72",
        "90e4d9e4ec680ff40ce00e712b24a67659539e06d50b538ed4a3d960b4f3bda5",
        "9a9a241b05eeaa0ca2b4323c5a756851c9cd15371a4d71a326749abc47062bf0",
        "0643786903dab7cbb079796ea4b27a81fb38442381773759dd52ac8615eb6ab2",
        "886078097635635c1450cf52ca0ec13a887ea4f8cd4b799fdedc650ec1f08781",
        "d4c4d2d16c7fec2d0d60f0a110eb4fbd9f1bb463033298e01b3141a7e4ca10bc",
        "83dfe687131d285a22c5379e19f4ebabcdfe8a19bade46a5cdcdc9e9c36b52a2",
        "7c4000e5d6948055553eb84fc2188ccad068caa1b584303f88dc0c582a0ecd42",
        "43c693fa32545b7d4106e337fe6edf7db92282795d5bdb80705ef8a0ac7e8030",
        "ebb17f7f9050e3c1b18f84cbd6333178d575d4baf3aca6dfa0587cc2a48e02d0",
        "ce910c4368092bf0886e59dc5df0b0ad11f40067b685505c2195463d32fa0418",
        "86fc704debb389a73775e02f8f0423ffbbb787a1033e531b2e47d40f71ad5560",
        "308af1914cb90aeb8913548cc37c9b55320875a2c0d2ecfe6afe1bfc02c64326",
        "bd3486100f2bb29762100b93b1f1cd41655ab05767f78fb1fc4adfe040ebe953",
        "29f56ee67dd218276984d723b6b105678faa1868a9644f0d9c49109c8322e1d8",
        "704c3ddde0b5fd3c6971a6ef16991ddff3e241c170ed539094ee668861e01764",
        "aaebc3ca0fe041a3a595170b8efda22308cd7d843510bf01263f05a1851cb173",
    ]
    return hashlib.sha256(username + password).hexdigest() in legal_hashes


def authenticate():
    """Send a 401 response that enables basic auth."""
    return Response(
        'Could not verify your access level for that URL.\n'
        'You have to login with proper credentials', 401,
        {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(f):
    """Decorator for methods that require authentication."""
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated


def rate():
    """Set rate limits for authenticated and nonauthenticated users."""
    auth = request.authorization

    if not auth or not check_auth(auth.username, auth.password):
        return "60/minute"
    else:
        return "600/minute"


@app.route('/v0/', methods=['GET', 'POST'])
@limiter.limit(rate)
@cross_origin()  # allow all origins all methods.
def lint():
    """Run linter on the provided text and return the results."""
    if 'text' in request.values:
        text = unquote(request.values['text'])
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
                    "source_name": "",
                    "source_url": "",
                })
            return jsonify(
                status="success",
                data={"errors": errors})


if __name__ == '__main__':
    app.debug = True
    app.run()
