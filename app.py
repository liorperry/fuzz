#!/usr/bin/env python3

import getopt
import logging.config
import os
import sys

import setup
from service.ApiController import app
from service.ApiController import initController
from setup import FLASK_SERVER_NAME
from setup import RESTPLUS_SWAGGER_UI_DOC_EXPANSION, RESTPLUS_VALIDATE, RESTPLUS_MASK_SWAGGER, RESTPLUS_ERROR_404_HELP, \
    FLASK_DEBUG

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
    # from service import init
    # init()
    initController()
    configure_app(flask_app)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ho:i:", ["host=", "index="])
    except getopt.GetoptError:
        print('test.py -o <elasticsearch host> -i <elasticsearch log index>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -o <elasticsearch host> -i <elasticsearch log index>')
            sys.exit()
        elif opt in ("-o", "--host"):
            print('-o param"', arg)
            setup.ES_HOST = arg
        elif opt in ("-i", "--index"):
            print('-i param"', arg)
            setup.ES_LOG_INDEX = arg
    print('ES host"', setup.ES_HOST)
    print('ES log Index"', setup.ES_LOG_INDEX)

    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/fuzz <<<<<'.format(app.config['SERVER_NAME']))


if __name__ == "__main__":
    main(sys.argv[1:])
    app.run(debug=FLASK_DEBUG, host="0.0.0.0", port=8090)
