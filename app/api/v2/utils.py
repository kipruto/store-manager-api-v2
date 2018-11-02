from flask import abort
import re
from .models.user_model import User
from .models.product_model import *


class RegistrationValidation:

    def __init__(self, is_admin, first_name, last_name, email_address, password):
        self.email_address = email_address
        self.is_admin = is_admin
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.user = User()

    def validate_user_data(self):
        """REGEX to verify email address format"""
        if re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email_address) is None:
            message = "Invalid email address"
            abort(400, message)

        for user in self.user.get_users():
            if self.email_address == user["email_address"]:
                message = "This email is already registered"
                abort(400, message)
        if self.email_address == "":
            message = "Your must provide an email address"
            abort(400, message)
        if self.password == "":
            message = "You must provide a password"
            abort(400, message)
        if self.is_admin == "":
            message = "Role cannot be empty"
            abort(400, message)
        if type(self.email_address) != str:
            message = "Email address must be a string"
            abort(400, message)
        if type(self.is_admin) != str:
            message = "Role must be a string"
            abort(400, message)
        if len(self.password) <= 6:
            message = "Password must be at least 6 characters long"
            abort(400, message)
        elif not any(char.isdigit() for char in self.password):
            message = "Password must contain a digit"
            abort(400, message)
        elif not re.search("[#@$]", self.password):
            message = "Password must have one of the special character [#@$]"
            abort(400, message)


class LoginValidation:
    def __init__(self, email_address, password):
        self.email_address = email_address
        self.password = password
        self.user = User()

    def validate_login_data(self):
        if self.email_address == "":
            message = "Email address cannot be empty"
            abort(400, message)
        if self.password == "":
            message = "Password cannot be empty"
            abort(400, message)


class ProductValidation:
    def __init__(self, category_id, product_name, unit_price, inventory_level, minimum_inventory_level):
        self.category_id = category_id
        self.product_name = product_name
        self.unit_price = unit_price
        self.inventory_level = inventory_level
        self.minimum_inventory_level = minimum_inventory_level
        self.product = Product()

    def validate_product_data(self):
        for product in self.product.get_all_products():
            if product['product_name'] == self.product_name:
                message = "Sorry, '" + self.product_name + "' already exists"
                abort(400, message)

        if type(self.product_name) != str:
            message = "product name must be a string"
            abort(400, message)

        if self.product_name == '':
            message = "Product name cannot be empty"
            abort(400, message)

        if self.inventory_level < 0 or self.inventory_level == "":
            message = "quantity must be a positive integer"
            abort(400, message)

        if self.unit_price < 0:
            message = "price must be a positive float"
            abort(400, message)

        if type(self.category_id) != int:
            message = "Category must be an integer"
            abort(400, message)

        if self.category_id < 1:
            message = "Category must be a positive number"
            abort(400, message)

        if self.category_id == "":
            message = "Category cannot be empty"
            abort(400, message)

        if self.unit_price <= 0:
            message = "unit price must be not be less than zero"
            abort(400, message)

        if self.unit_price == "":
            message = "unit price cannot be blank"
            abort(400, message)

