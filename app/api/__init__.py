from flask import Blueprint
from flask_restful import Api

from .v2.views.user_views import SignUp, Login
from .v2.views.category_views import ProductCategories, GetSpecificCategory
from .v2.views.product_views import Products, GetSpecificProduct, DeleteProduct, UpdateProduct
from .v2.views.sale_views import Sales


# create blueprint
v2_blueprint = Blueprint('api_v2', __name__, url_prefix="/api/v2")
api_v2 = Api(v2_blueprint)

api_v2.add_resource(SignUp, '/auth/signup')
api_v2.add_resource(Login, '/auth/login')
api_v2.add_resource(ProductCategories, '/categories')
api_v2.add_resource(GetSpecificCategory, '/categories/<int:category_id>')
api_v2.add_resource(Products, '/products')
# api_v2.add_resource(Products, '/products/<int:product_id>')
api_v2.add_resource(UpdateProduct, '/products/update/<int:product_id>')
api_v2.add_resource(DeleteProduct, '/products/delete/<int:product_id>')
api_v2.add_resource(GetSpecificProduct, '/products/<int:product_id>')
api_v2.add_resource(Sales, '/sales')
