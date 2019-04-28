# Flask settings
FLASK_SERVER_NAME = 'fuzzer:8890'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False
ES_HOST: str = '127.0.0.1'
ES_LOG_INDEX: str = 'log-index'