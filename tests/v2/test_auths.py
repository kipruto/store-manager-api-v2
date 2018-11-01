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
            email_address="admin@admin.com",
            password="admin123"
        ))
        self.user_login_data = json.dumps(dict(
            email_address="admin@admin.com",
            password="admin123"
        ))

    def teardown(self):
        self.app_context.pop()

    def test_user_signup(self):
        response = self.client.post('/api/v2/auth/signup',
                                    data=self.user_signup_data,
                                    content_type='application/json'
                                    )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'], "success")
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        response = self.client.post('/api/v2/auth/login',
                                    data=self.user_login_data,
                                    content_type='application/json'
                                    )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'], "success")
        self.assertTrue(response_data['access-token'])
        self.assertEqual(response.status_code, 201)
