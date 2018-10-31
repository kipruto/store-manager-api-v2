from flask import abort
import re


class RegistrationValidation:
    def __init__(self, is_admin, first_name, last_name, email_address, password):
        self.email = is_admin
        self.first_name = first_name,
        self.last_name = last_name,
        self.email_address = email_address
        self.password = password

    def validate_user_data(self):
        """REGEX to verify email address format"""
        if re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email_address) is None:
            message = "Invalid email address"
            abort(400, message)
        if self.email_address == "":
            message = "Your must provide an email address"
            abort(400, message)
        if self.password == "":
            message = "You must provide a password"
            abort(400, message)
        if type(self.email_address) != str:
            message = "Email address must be a string"
            abort(400, message)
        if len(self.password) <= 6:
            message = "Password must be at least 6 characters long"
            abort(400, message)
        elif not any(char.isdigit() for char in self.password):
            message = "Password must contain a digit"
            abort(400, message)
        elif not re.search("[#@$]", self.password):
            message = "Password must contain of these special characters -> [#@$]'"
            abort(400, message)