from manage import init_db


class Product:
    def __init__(self):
        self.db = init_db()

    def add_product(self, category_id, product_name, unit_price, inventory_level, minimum_inventory_level):
        payload = {
            "category_id": category_id,
            "product_name": product_name,
            "unit_price": unit_price,
            "inventory_level": inventory_level,
            "minimum_inventory_level": minimum_inventory_level
        }
        query = """INSERT INTO products(category_id, product_name, unit_price, inventory_level, minimum_inventory_level)
                    VALUES(%(category_id)s, %(product_name)s, %(unit_price)s, %(inventory_level)s, 
                    %(minimum_inventory_level)s) """
        cursor = self.db.cursor()
        cursor.execute(query, payload)
        self.db.commit()
        return payload
