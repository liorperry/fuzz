import json

from flask import abort, Flask

from service import apiService
from .utils import JSON_MIME_TYPE

app = Flask(__name__)


@app.route('/fuzz/do/<string:command>')
def do(command):
    # todo - execute command
    if command is None:
        abort(404)

    switcher = {
        "run": apiService.run,
        "pause": apiService.pause,
        "restart": apiService.pause,
        "stop": apiService.pause
    }

    func = switcher.get(command, lambda: "Invalid command")
    # Execute the function
    result = func()
    content = json.dumps(result)
    return content, 200, {'Content-Type': JSON_MIME_TYPE}


@app.route('/fuzz/status')
def status():
    content = json.dumps({
        'id': 33,
        'status': 'my status',
        'manager id': 1,
        'running targets': 10,
    })
    return content, 200, {'Content-Type': JSON_MIME_TYPE}


@app.errorhandler(404)
def not_found(e):
    return '', 404
