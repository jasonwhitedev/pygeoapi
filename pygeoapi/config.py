import os

class Config():
    DEBUG = True

class DevelopmentConfig(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

config_settings = {'development': DevelopmentConfig}
