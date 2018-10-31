from flask import jsonify, make_response, request
from flask_jwt_extended import (create_access_token, get_jwt_claims, jwt_required)
from flask_restful import Resource
from ..models.category_model import *


class ProductCategories(Resource):
    def __init__(self):
        self.categories = Category()

    @jwt_required
    def get(self):
        claims = get_jwt_claims()
        if claims['role'] == 'True':
            return make_response(jsonify({
                "status": "Failure",
                "message": "You are not authorized to access that endpoint"
            }), 401)
        product_categories = self.categories.get_all_product_categories()
        return make_response(jsonify({
            "status": "OK",
            "message": "success",
            "product_categories": product_categories
        }), 200)


class GetSpecificCategory(Resource):
    def __init__(self):
        self.category = Category()

    def get(self, category_id):
        category = self.category.get_specific_category(category_id)
        return make_response(jsonify({
            "status": "OK",
            "message": "success",
            "category": category
        }), 200)
