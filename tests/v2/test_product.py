import unittest
from app import create_app
import json


class TestProduct(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')

        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client(use_cookies=True)

        self.category_data = self.product_data = json.dumps(dict(
            category_title='beverages'
        ))

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

        self.user_data = json.dumps(dict(
            is_admin='False',
            first_name='',
            last_name='',
            email_address='',
        ))
        self.sale_data = json.dumps(dict(
            user_id=1,
            product_id=1,
            quantity=5,
            unit_cost=5,
            total_cost=25
        ))

        self.product_data = json.dumps(dict(
            category_id=1,
            product_name='cappuccino',
            unit_price=200,
            inventory_level=1000,
            minimum_inventory_level=50
        ))
        self.product_update_data = json.dumps(dict(
            category_id=1,
            product_name='Espresso',
            unit_price=100,
            inventory_level=500,
            minimum_inventory_level=45
        ))

    def teardown(self):
        self.app_context.pop()

    def test_create_category(self):
        response = self.client.post('/api/v2/categories',
                                    data=self.category_data,
                                    content_type='application/json'
                                    )
        response_data = json.loads(response.data.decode())
        self.assertEqual(response_data['message'], "success")
        self.assertEqual(response.status_code, 201)

    def test_create_product(self):
        response = self.client.post('/api/v2/categories',
                                    data=self.category_data,
                                    content_type='application/json'
                                    )
        response_datum = json.loads(response.data.decode())
        self.assertEqual(response_datum['message'], "success")
        resp = self.client.post('/api/v2/products',
                                data=self.product_data,
                                content_type='application/json'
                                )
        response_data = json.loads(resp.data.decode())
        self.assertEqual(response_data['message'], "success")
        self.assertEqual(resp.status_code, 201)

    def test_get_all_products(self):
        response1 = self.client.post('/api/v2/categories',
                                     data=self.category_data,
                                     content_type='application/json'
                                     )
        response_datum = json.loads(response1.data.decode())
        self.assertEqual(response_datum['message'], "success")
        resp = self.client.post('/api/v2/products',
                                data=self.product_data,
                                content_type='application/json'
                                )
        response_data = json.loads(resp.data.decode())
        self.assertEqual(response_data['message'], "success")
        self.assertEqual(resp.status_code, 201)

        response = self.client.get('/api/v2/products', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_product_update(self):
        response = self.client.put('/api/v2/products/update/1',
                                   data=self.product_update_data,
                                   content_type='application/json')
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'update successful')

    def test_get_specific_product(self):
        response1 = self.client.post('/api/v2/categories',
                                     data=self.category_data,
                                     content_type='application/json'
                                    )
        response_datum = json.loads(response1.data.decode())
        self.assertEqual(response_datum['message'], "success")
        resp = self.client.post('/api/v2/products',
                                data=self.product_data,
                                content_type='application/json'
                                )
        response_data = json.loads(resp.data.decode())
        self.assertEqual(response_data['message'], "success")
        self.assertEqual(resp.status_code, 201)

        response = self.client.get('/api/v2/products/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_delete_product(self):
        response1 = self.client.post('/api/v2/categories',
                                     data=self.category_data,
                                     content_type='application/json'
                                     )
        response_datum = json.loads(response1.data.decode())
        self.assertEqual(response_datum['message'], "success")
        resp = self.client.post('/api/v2/products',
                                data=self.product_data,
                                content_type='application/json'
                                )
        response_data = json.loads(resp.data.decode())
        self.assertEqual(response_data['message'], "success")
        self.assertEqual(resp.status_code, 201)

        response = self.client.delete('/api/v2/products/delete/1', content_type='application/json')
        self.assertEqual(response.status_code, 200)
