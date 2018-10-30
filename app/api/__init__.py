from flask import Blueprint
from flask_restful import Api

from .v2.views.user_views import SignUp


# create blueprint
v2_blueprint = Blueprint('api_v2', __name__, url_prefix="/api/v2")
api_v2 = Api(v2_blueprint)

api_v2.add_resource(SignUp, '/auth/signup')
