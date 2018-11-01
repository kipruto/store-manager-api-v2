import psycopg2
from instance.config import app_config
import os
env = os.environ['ENV']


def connection():
    con = psycopg2.connect(app_config[env].url)
    return con


def init_db():
    con = connection()
    return con


def create_tables():
    conn = connection()
    cursor = conn.cursor()
    queries = tables()
    for query in queries:
        cursor.execute(query)
    conn.commit()


def destroy_tables():
    pass


def tables():
    sales = """create table if not exists sales(
                    sale_id serial primary key not null, 
                    user_id int not null, 
                    transaction_id int not null, 
                    total_cost money not null, 
                    date_created timestamp with time zone default('now'::text)::date not null,
                    foreign key(user_id) references users(user_id) on update cascade on delete cascade, 
                    foreign key(transaction_id) references transactions(transaction_id) 
                    on update cascade on delete cascade);"""

    users = """create table if not exists users(user_id serial primary key not null, 
                    is_admin boolean default false,
                    first_name varchar(50) not null,
                    last_name varchar(50) not null,
                    email_address varchar(50) not null,
                    password varchar(50) not null,
                    date_created timestamp with time zone default('now'::text)::date not null
                    );"""

    categories = """create table if not exists categories(
                    category_id serial primary key not null, 
                    category_title varchar(50) not null,
                    date_created timestamp with time zone default('now'::text)::timestamp not null);"""

    products = """create table if not exists products(
                    product_id serial primary key not null, 
                    category_id int not null,
                    product_name varchar(50) not null, 
                    unit_price money not null, 
                    inventory_level int not null,
                    minimum_inventory_level int not null,
                    date_created timestamp with time zone default('now'::text)::date not null,
                    foreign key(category_id) references categories(category_id) on update cascade on delete cascade
                    );"""

    transactions = """create table if not exists transactions(
                    transaction_id serial primary key not null, 
                    product_id int not null, 
                    quantity int not null, cost money not null,
                    date_created timestamp with time zone default('now'::text)::timestamp not null,
                    foreign key(product_id) references products(product_id) on update cascade on delete cascade);"""
    queries = [categories, products, users, transactions, sales, ]
    return queries
