import unittest
from app import create_app
import json


class TestDB(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')

        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

        self.user_signup_data = json.dumps(dict(
            is_admin="True",
            first_name='jane',
            last_name="doe",
            email_address="admgrny@admin.com",
            password="admin#123"
        ))
        self.user_n_signup_data = json.dumps(dict(
            is_admin="True",
            first_name='jane',
            last_name="doe",
            email_address="admgnyt@admin.com",
            password="admin#123"
        ))
        self.user_login_data = json.dumps(dict(
            email_address="admgnyt@admin.com",
            password="admin#123"
        ))

        # invalid email
        self.user_invalid_email = json.dumps(dict(
            is_admin="True",
            first_name='jane',
            last_name="doe",
            email_address="admin@admi",
            password="admin@123"
        ))

        # registered email
        self.user_registered_email = json.dumps(dict(
            is_admin="True",
            first_name='jane',
            last_name="doe",
            email_address="admin@admin.com",
            password="admin@123"
        ))

        # empty email
        self.user_empty_email = json.dumps(dict(
            is_admin="True",
            first_name='jane',
            last_name="doe",
            email_address="",
            password="admin@123"
        ))

        # empty password
        self.user_empty_password = json.dumps(dict(
            is_admin="True",
            first_name='jane',
            last_name="doe",
            email_address="adminly@admin.com",
            password=""
        ))

        # empty role
        self.user_empty_role = json.dumps(dict(
            is_admin="",
            first_name='jane',
            last_name="doe",
            email_address="admn@admin.com",
            password="admin@123"
        ))

        # non string role
        self.user_non_string_role = json.dumps(dict(
            is_admin=8,
            first_name='jane',
            last_name="doe",
            email_address="amn@admin.com",
            password="admin@123"
        ))

        # invalid password format
        self.password_invalid_format = json.dumps(dict(
            is_admin="True",
            first_name='jane',
            last_name="doe",
            email_address="admyn@admin.com",
            password="admin123"
        ))

        # password no digit
        self.password_no_digit = json.dumps(dict(
            is_admin="True",
            first_name='jane',
            last_name="doe",
            email_address="admin@adminy.com",
            password="admin@admin"
        ))

        # no special char
        self.password_no_special_chars = json.dumps(dict(
            is_admin="True",
            first_name='jane',
            last_name="doe",
            email_address="admin@admin.com",
            password="admin123"
        ))

    def teardown(self):
        self.app_context.pop()

    # test invalid email
    def test_invalid_email_signup(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=self.user_invalid_email,
                                    content_type='application/json'
                                    )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'], "Invalid email address")
        self.assertEqual(response.status_code, 400)

    # registered email
    def test_registered_email_signup(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=self.user_registered_email,
                                    content_type='application/json'
                                    )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'], "This email is already registered")
        self.assertEqual(response.status_code, 400)

    # empty email
    def test_empty_email_signup(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=self.user_empty_email,
                                    content_type='application/json'
                                    )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'], "Invalid email address")
        self.assertEqual(response.status_code, 400)

    # empty password
    def test_empty_password_signup(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=self.user_empty_password,
                                    content_type='application/json'
                                    )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'], "You must provide a password")
        self.assertEqual(response.status_code, 400)

    # empty role
    def test_empty_role_signup(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=self.user_empty_role,
                                    content_type='application/json'
                                    )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'], "Role cannot be empty")
        self.assertEqual(response.status_code, 400)

    # non string role
    def test_non_string_role_signup(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=self.user_non_string_role,
                                    content_type='application/json'
                                    )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'], "Role must be a string")
        self.assertEqual(response.status_code, 400)

    # invalid password format
    def test_invalid_password_signup(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=self.password_invalid_format,
                                    content_type='application/json'
                                    )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'], "Password must have one of the special character [#@$]")
        self.assertEqual(response.status_code, 400)

    def test_with_digit_password_signup(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=self.password_no_digit,
                                    content_type='application/json'
                                    )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'], "Password must contain a digit")
        self.assertEqual(response.status_code, 400)

    def test_user_login(self):

        resp = self.client.post('/api/v2/auth/login',
                                data=self.user_login_data,
                                content_type='application/json'
                                )
        response_data = json.loads(resp.data.decode())
        self.assertEqual(response_data['message'], "success")
        self.assertTrue(response_data['access-token'])
