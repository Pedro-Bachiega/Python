class Config(object):
    DEBUG = False
    TESTING = False
    JSONIFY_PRETTYPRINT_REGULAR = True

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True