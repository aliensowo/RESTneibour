import os


class Config(object):

    DEBUG = False
    CSRF = True
    SECRET_KEY = '123456'

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost:5432/postgres'
    # export DATABASE_KEY='postgresql://postgres@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATION = False


class DevelopmentConfig(Config):
    Development = True
    DEBUG = True
