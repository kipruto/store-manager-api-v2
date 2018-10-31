from manage import init_db


class Category:
    def __init__(self):
        self.db = init_db()

    def create_product_category(self, category_title):
        payload = {
            'category_title': category_title
        }
        query = """INSERT INTO categories(category_title) VALUES
                    (%(category_title)s)"""
        cursor = self.db.cursor()
        cursor.execute(query, payload)
        self.db.commit()
        return payload

    def get_all_product_categories(self):
        cursor = self.db.cursor()
        cursor.execute("""SELECT category_id, category_title, date_created FROM categories""")
        data = cursor.fetchall()
        rows = []
        for i, items in enumerate(data):
            category_id, category_title, date_created = items
            datum = dict(
                category_id=int(category_id),
                category_title=category_title,
                date_created=date_created
            )
            rows.append(datum)
        return rows

    def get_specific_category(self, category_id):
        cursor = self.db.cursor()
        cursor.execute("""SELECT * FROM categories WHERE category_id={} """.format(category_id))
        data = cursor.fetchall()
        row = []
        for i, items in enumerate(data):
            category_id, category_title, date_created = items
            datum = dict(
                category_id=int(category_id),
                category_title=category_title,
                date_created=date_created
            )
            row.append(datum)
        return row
