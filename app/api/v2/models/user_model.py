from manage import init_db
from passlib.hash import pbkdf2_sha256 as sha256


class User:
    def __init__(self):
        self.db = init_db()

    def create_user(self, is_admin, first_name, last_name, email_address, password):
        payload = {
            "is_admin": is_admin,
            "first_name": first_name,
            "last_name": last_name,
            "email_address": email_address,
            "password": password
        }
        query = """INSERT INTO users(is_admin, first_name, last_name, email_address, password) VALUES
                    (%(is_admin)s, %(first_name)s, %(last_name)s, %(email_address)s, %(password)s) """
        cursor = self.db.cursor()
        cursor.execute(query, payload)
        self.db.commit()
        return payload

    def get_users(self):
        cursor = self.db.cursor()
        cursor.execute("""SELECT user_id, is_admin, first_name, last_name, email_address, date_created FROM users""")
        data = cursor.fetchall()
        rows = []
        for i, items in enumerate(data):
            user_id, is_admin, first_name, last_name, email_address, date_created = items
            datum = dict(
                user_id=int(user_id),
                is_admin=bool(is_admin),
                first_name=first_name,
                last_name=last_name,
                email_address=email_address,
                date_created=date_created
            )
            rows.append(datum)
        return rows

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hashed_password):
        return sha256.verify(password, hashed_password)

    def login(self, email_address, password):
        cursor = self.db.cursor()
        cursor.execute(
            """SELECT is_admin, email_address FROM users 
                WHERE email_address='{}' AND password='{}'""".format(email_address, password))
        data = cursor.fetchone()
        return data
