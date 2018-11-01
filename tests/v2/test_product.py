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

        self.product_data = json.dumps(dict(
            category_id=1,
            product_name='cappuccino coffee',
            unit_price=200,
            inventory_level=1000,
            minimum_inventory_level=50
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
