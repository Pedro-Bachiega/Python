import os

DATABASE_NAME = 'python_training.db'
DATABASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'database'))

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////%s/%s' % (DATABASE_PATH, DATABASE_NAME)

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True