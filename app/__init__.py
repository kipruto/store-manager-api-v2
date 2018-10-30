from flask import Flask
from instance.config import app_config


def create_app(config_name):
    """
    This function creates the flask application. Doing it this way
    allows me to pass in different configuration settings from the
    config file
    :param config_name:
    :return: app
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    return app
