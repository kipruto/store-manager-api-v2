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
        total_cost = int(data['quantity']) * int(data['unit_price'])

        sale = self.sale.create_sale(user_id, product_id, quantity, unit_price)
        return make_response(jsonify({
            "message": "success",
            "sale": sale,
            "total_cost": total_cost
        }), 201)

    def get(self):
        sales = self.sale.get_all_sales()
        return make_response(jsonify({
            "status": "OK",
            "message": "success",
            "products": sales
        }), 200)


class FilterRecordsByAttendant(Resource):
    def __init__(self):
        self.sales = Sale()

    def get(self, user_id):
        sale_records = self.sales.filter_sales_records_by_attendant(user_id)
        return make_response(jsonify({
            "status": "OK",
            "message": "success",
            "product": sale_records
        }), 200)
