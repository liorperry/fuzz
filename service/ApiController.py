import json

from flask import abort, Flask, logging, send_from_directory, request
from flask_swagger_ui import get_swaggerui_blueprint

from model.Command import Command
from service import apiService, pluginMgr, statusMgr
from setup import FLASK_SERVER_NAME
from .utils import JSON_MIME_TYPE, json_response, MyEncoder

app = Flask(__name__, static_url_path='/static')
log = logging.getLogger(__name__)

SWAGGER_URL = '/fuzz/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://' + FLASK_SERVER_NAME + '/fuzz/swagger'  # Our API url (can of course be a local resource)


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


@app.route('/fuzz/swagger/<string:name>', endpoint='swagger_plugin')
def swagger_plugin(name):
    if name is None:
        abort(404)

    swagger = pluginMgr.plugin(name).swagger()
    return send_from_directory('../service/plugins/' + name + '/static', swagger)


# **********************************************************************************************************************

@app.route('/fuzz/status')
def status():
    return statusMgr.toJSON()


# **********************************************************************************************************************
@app.route('/fuzz/plugins', endpoint='plugins')
def plugins():
    content = pluginMgr.moduleNames()
    return json.dumps(content), 200, {'Content-Type': JSON_MIME_TYPE}


@app.route('/fuzz/plugin/<string:name>/status', endpoint='plugin_status')
def plugin_status(name):
    if name is None:
        abort(404)

    content = json.dumps(statusMgr.status(name), cls=MyEncoder)
    return content, 200, {'Content-Type': JSON_MIME_TYPE}


@app.route('/fuzz/plugin/<string:role>/do/<string:command>', methods=['GET'], endpoint='doGet')
def doGet(role, command):
    # execute command
    if role is None or command is None:
        abort(404)

    # concurrency:int, timeout:int , role:str, data:{}
    commandEntity = Command(role, command,None,5,10)

    # run command
    result = apiService.run(commandEntity)
    # Execute the function
    content = json.dumps(result,cls=MyEncoder)
    return content, 200, {'Content-Type': JSON_MIME_TYPE}

@app.route('/fuzz/plugin/<string:role>/do/<string:command>', methods=['POST'], endpoint='doPost')
def doPost(role, command):
    # execute command
    if role is None or command is None:
        abort(404)

    if request.content_type != JSON_MIME_TYPE:
        error = json.dumps({'error': 'Invalid Content Type'})
        return json_response(error, 400)

    data = request.json
    # concurrency:int, timeout:int , role:str, data:{}
    commandEntity = Command(role, command, data, data.get('concurrency'),data.get('timeout'))

    # run command
    result = apiService.run(commandEntity)
    # Execute the function
    content = json.dumps(result, cls=MyEncoder)
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
