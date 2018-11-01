from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.product_model import *


class Products(Resource):
    def __init__(self):
        self.product = Product()

    def post(self):
        data = request.get_json()
        category_id = data['category_id']
        product_name = data['product_name']
        unit_price = data['unit_price']
        inventory_level = data['inventory_level']
        minimum_inventory_level = data['minimum_inventory_level']

        result = self.product.add_product(category_id, product_name, unit_price, inventory_level,
                                          minimum_inventory_level)
        return make_response(jsonify({
            "status": "OK",
            "message": "success",
            "data": result
        }), 201)

    def get(self):
        products = self.product.get_all_products()
        return make_response(jsonify({
            "status": "OK",
            "message": "success",
            "products": products
        }), 200)


class UpdateProduct(Resource):
    def __init__(self):
        self.product = Product()

    def put(self, product_id):
        data = request.get_json()
        category_id = data['category_id']
        product_name = data['product_name']
        unit_price = data['unit_price']
        inventory_level = data['inventory_level']
        minimum_inventory_level = data['minimum_inventory_level']
        self.product.update_product(category_id, product_name, unit_price, inventory_level,
                                    minimum_inventory_level, product_id)
        return make_response(jsonify({
            "status": "OK",
            "message": "update successful"
        }), 201)
class GetSpecificProduct(Resource):
    def __init__(self):
        self.product = Product()

    def get(self, product_id):
        product = self.product.get_specific_product(product_id)
        return make_response(jsonify({
            "status": "OK",
            "message": "success",
            "product": product
        }), 200)

