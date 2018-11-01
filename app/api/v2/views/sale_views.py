from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.sale_model import *


class Sales(Resource):
    def __init__(self):
        self.sale = Sale()

    def post(self):
        data = request.get_json()
        user_id = data['user_id']
        product_id = data['product_id']
        quantity = data['quantity']
        unit_price = data['unit_price']
        total_cost = data['total_cost']

        sale = self.sale.create_sale(user_id, product_id, quantity, unit_price, total_cost)
        return make_response(jsonify({
            "status": "OK",
            "message": "success",
            "sale": sale
        }), 201)
