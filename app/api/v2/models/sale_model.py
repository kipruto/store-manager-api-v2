from manage import init_db


class Sale:
    def __init__(self):
        self.db = init_db()

    def create_sale(self, user_id, product_id, quantity, unit_price):
        payload = {
            "user_id": user_id,
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": unit_price

        }
        query = """INSERT INTO sales(user_id, product_id, quantity, unit_price)
                    VALUES(%(user_id)s, %(product_id)s, %(quantity)s, %(unit_price)s);
                     """
        cursor = self.db.cursor()
        cursor.execute(query, payload)
        self.db.commit()
        return payload
