import logging.config
import os

from service import init
from service.ApiController import initController, app
from setup import FLASK_SERVER_NAME
from setup import RESTPLUS_SWAGGER_UI_DOC_EXPANSION, RESTPLUS_VALIDATE, RESTPLUS_MASK_SWAGGER, RESTPLUS_ERROR_404_HELP, FLASK_DEBUG

logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)


def configure_app(flask_app):
    flask_app.config['SERVER_NAME'] = FLASK_SERVER_NAME
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    init()
    initController()
    configure_app(flask_app)


def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=FLASK_DEBUG)


if __name__ == "__main__":
    main()
