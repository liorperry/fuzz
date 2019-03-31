import json

from flask import abort, Flask, logging, send_from_directory, request
from flask_swagger_ui import get_swaggerui_blueprint
from service import apiService, manager
from service.plugins import PLUGINS
from service.plugins.PluginsManager import PluginsMgr
from setup import FLASK_SERVER_NAME
from .utils import JSON_MIME_TYPE, json_response

app = Flask(__name__, static_url_path='/static')
log = logging.getLogger(__name__)

SWAGGER_URL = '/fuzz/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://'+FLASK_SERVER_NAME+'/fuzz/swagger'  # Our API url (can of course be a local resource)


def initController():
    # Call factory function to create our blueprint
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Fuzzer"
        },
        # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        #    'clientId': "your-client-id",
        #    'clientSecret': "your-client-secret-if-required",
        #    'realm': "your-realms",
        #    'appName': "your-app-name",
        #    'scopeSeparator': " ",
        #    'additionalQueryStringParams': {'test': "hello"}
        # }
    )

    # Register blueprint at URL
    # (URL must match the one given to factory function above)
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# **********************************************************************************************************************

@app.errorhandler(404)
def not_found(e):
    return '', 404

# **********************************************************************************************************************
@app.route('/fuzz/swagger', endpoint='swagger')
def swagger():
    return send_from_directory('../static', 'swagger.json')


@app.route('/fuzz/swagger/<string:name>', endpoint='plugin')
def plugin(name):
    if name is None:
        abort(404)

    swagger = PluginsMgr(PLUGINS).plugin(name).swagger()
    return send_from_directory('../service/plugins/' + name +'/static' , swagger)


# **********************************************************************************************************************

@app.route('/fuzz/status')
def status():
    content = json.dumps({
        'id': 33,
        'status': 'my status',
        'manager id': 1,
        'running targets': 10,
    })
    return content, 200, {'Content-Type': JSON_MIME_TYPE}


# **********************************************************************************************************************
@app.route('/fuzz/plugins', endpoint='plugins')
def plugins():
    content = PluginsMgr(PLUGINS).plugins()
    return json.dumps(content), 200, {'Content-Type': JSON_MIME_TYPE}


@app.route('/fuzz/plugin/<string:name>/status', endpoint='plugin_status')
def plugin_status(name):
    if name is None:
        abort(404)

    content = json.dumps(manager.status(name))
    return content, 200, {'Content-Type': JSON_MIME_TYPE}


@app.route('/fuzz/plugin/<string:role>/do/<string:command>', methods=['POST'], endpoint='do')
def do(role, command):
    # todo - execute command
    if role is None or command is None:
        abort(404)

    if request.content_type != JSON_MIME_TYPE:
        error = json.dumps({'error': 'Invalid Content Type'})
        return json_response(error, 400)

    data = request.json
    if not all([data.get('role'), data.get('cmd'), data.get('details')]):
        error = json.dumps({'error': 'Missing field/s (role, cmd, details)'})
        return json_response(error, 400)

    switcher = {
        "run": apiService.run,
        "pause": apiService.pause,
        "restart": apiService.restart,
        "stop": apiService.stop
    }

    func = switcher.get(apiService.run(data), lambda: "Invalid command")
    # Execute the function
    result = func()
    content = json.dumps(result.toJSON())
    return content, 200, {'Content-Type': JSON_MIME_TYPE}

# **********************************************************************************************************************

@app.route('/fuzz/do/<string:command>', endpoint='doAll')
def doAll(command):
    if command is None:
        abort(404)

    switcher = {
        "run": apiService.run,
        "pause": apiService.pause,
        "restart": apiService.restart,
        "stop": apiService.stop
    }

    func = switcher.get(command, lambda: "Invalid command")
    # Execute the function
    result = func()
    content = json.dumps(result)
    return content, 200, {'Content-Type': JSON_MIME_TYPE}


