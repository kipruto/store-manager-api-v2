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

    def get_all_products(self):
        cursor = self.db.cursor()
        cursor.execute("""SELECT product_id,category_id, product_name, unit_price, 
        inventory_level, minimum_inventory_level FROM products""")
        data = cursor.fetchall()
        rows = []
        for i, items in enumerate(data):
            product_id, category_id, product_name, unit_price, inventory_level, minimum_inventory_level = items
            datum = dict(
                product_id=int(product_id),
                category_id=int(category_id),
                product_name=product_name,
                unit_price=unit_price,
                inventory_level=int(inventory_level),
                minimum_inventory_level=int(minimum_inventory_level)
            )
            rows.append(datum)
        return rows

    def get_specific_product(self, product_id):
        cursor = self.db.cursor()
        cursor.execute("""SELECT product_id, category_id, product_name, unit_price, 
        inventory_level, minimum_inventory_level FROM products WHERE product_id={} """.format(product_id))
        data = cursor.fetchall()
        row = []
        for i, items in enumerate(data):
            product_id, category_id, product_name, unit_price, inventory_level, minimum_inventory_level = items
            datum = dict(
                product_id=int(product_id),
                category_id=int(category_id),
                product_name=product_name,
                unit_price=unit_price,
                inventory_level=int(inventory_level),
                minimum_inventory_level=int(minimum_inventory_level)
            )
            row.append(datum)
        return row
