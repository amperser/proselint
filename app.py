from flask import Flask, request
import subprocess
import uuid
import os
import re
import json

app = Flask(__name__)


@app.route('/api/v1/', methods=["GET"])
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
