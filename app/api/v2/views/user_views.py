from flask import jsonify, make_response, request
from flask_restful import Resource
from ..models.user_model import *


class SignUp(Resource):
    def __init__(self):
        self.user = User()

    def get(self):
        users = self.user.get_users()
        return make_response(jsonify({
            "status": "OK",
            "message": "success",
            "users": users
        }), 200)

    def post(self):
        data = request.get_json()
        is_admin = data['is_admin']
        first_name = data['first_name']
        last_name = data['last_name']
        email_address = data['email_address']
        password = data['password']

        result = self.user.create_user(is_admin=is_admin,
                                       first_name=first_name,
                                       last_name=last_name,
                                       email_address=email_address,
                                       password=password)
        return make_response(jsonify({
            "status": "OK",
            "message": "success",
            "user": result
        }), 201)


class Login(Resource):
    def __init__(self):
        self.user = User()

    def post(self):
        data = request.get_json()
        email_address = data['email_address']
        password = data['password']

        user_login = self.user.login(email_address=email_address, password=password)
        if user_login is None:
            return make_response(jsonify({
                "status": "Fail",
            }), 400)
        return jsonify(message="Login successful!")
