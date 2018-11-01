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
