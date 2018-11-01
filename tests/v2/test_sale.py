import unittest
from app import create_app
import json


class TestSale(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')

        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

        self.category_data = self.product_data = json.dumps(dict(
            category_title='beverages'
        ))

        self.admin_signup_data = json.dumps(dict(
            is_admin="True",
            first_name='jane',
            last_name="doe",
            email_address="admin@admin.com",
            password="admin123"
        ))
        self.admin_login_data = json.dumps(dict(
            email_address="admin@admin.com",
            password="admin123"
        ))

        self.user_signup_data = json.dumps(dict(
            is_admin='False',
            first_name='Jane',
            last_name='Doe',
            email_address='attendant@storemanager.com',
            password="attendant123"
        ))
        self.user_login_data = json.dumps(dict(
            email_address="attendant@storemanager.com",
            password="attendant123"
        ))
        self.sale_data = json.dumps(dict(
            user_id=1,
            product_id=3,
            quantity=5,
            unit_price=10,
            total_cost=25
        ))

        self.product_data = json.dumps(dict(
            category_id=1,
            product_name='cappuccino',
            unit_price=200,
            inventory_level=1000,
            minimum_inventory_level=50
        ))

    def test_create_sale(self):
        # create user
        signup = self.client.post('/api/v2/auth/signup',
                                  data=self.user_signup_data,
                                  content_type='application/json'
                                  )
        signup_data = json.loads(signup.data.decode())
        self.assertEqual(signup_data['message'], "success")

        # login user
        login = self.client.post('/api/v2/auth/login',
                                 data=self.user_login_data,
                                 content_type='application/json'
                                 )
        user_login_data = json.loads(login.data.decode())
        self.assertEqual(user_login_data['message'], "success")

        # create product_category
        response = self.client.post('/api/v2/categories',
                                    data=self.category_data,
                                    content_type='application/json'
                                    )
        response_datum = json.loads(response.data.decode())
        self.assertEqual(response_datum['message'], "success")
        # create product
        resp = self.client.post('/api/v2/products',
                                data=self.product_data,
                                content_type='application/json'
                                )
        response_data = json.loads(resp.data.decode())
        self.assertEqual(response_data['message'], "success")
        self.assertEqual(resp.status_code, 201)

        # make sale
        sale = self.client.post('/api/v2/sales',
                                data=self.sale_data,
                                content_type='application/json'
                                )
        res_data = json.loads(sale.data.decode())
        self.assertEqual(res_data['message'], "success")
        self.assertEqual(response.status_code, 201)
