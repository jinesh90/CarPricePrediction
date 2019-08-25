import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'abc'
    PORT = os.environ.get("APP_PORT") or 9090
