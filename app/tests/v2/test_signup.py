import unittest
from app import create_app
import json


class TestDB(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

    def teardown(self):
        self.app_context.pop()

    def test_create_user(self):
        response = self.client.post(
            '/api/v2/auth/signup',
            data=json.dumps(dict(
                is_admin="True", first_name='jane', last_name="doe", email_address="admin@admin.com",
                password="admin123"
            )),
            content_type='application/json'
        )
        # response_data = json.load(response.data)
        self.assertEqual(response.status_code, 201)
