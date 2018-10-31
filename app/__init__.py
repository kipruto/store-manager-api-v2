from flask import Flask
from instance.config import app_config
from flask_jwt_extended import JWTManager
from manage import create_tables
import os


def create_app(config_name):
    """
    This function creates the flask application. Doing it this way
    allows me to pass in different configuration settings from the
    config file
    :param config_name:
    :return: app
    """
    app = Flask(__name__, instance_relative_config=True)
    create_tables()
    app.config.from_object(app_config[config_name])
    app.config['JWT_SECRET_KEY'] = 'sweet-secret'
    jwt = JWTManager(app)

    @jwt.user_identity_loader
    def check_current_user(current_user):
        """
        This function returns the currently logged-in users attributes(email and is_admin)
        :param current_user:
        :return: current_user
        """
        return current_user[1]

    @jwt.user_claims_loader
    def add_claims_to_access_token(current_user):
        """
        :param current_user:
        :return: a dictionary containing logged in users is_admin attribute
        """
        return {"role": current_user[0]}

    from app.api import v2_blueprint
    app.register_blueprint(v2_blueprint)

    print(os.environ['ENV'])
    return app

