import psycopg2
from psycopg2.extras import execute_batch, execute_values

from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST


def connect():
    try:
        # Подключение к базе данных
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
        print('Successfully connected to database')
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')
    return conn


def initialize_database(conn, sql_file_path):
    try:
        # Чтение SQL-скрипта из файла
        with open(sql_file_path, 'r') as sql_file:
            sql_script = sql_file.read()
        
        # Выполнение SQL-скрипта
        with conn.cursor() as cursor:
            cursor.execute(sql_script)
            conn.commit()
            print("Database initialized successfully")
    except Exception as e:
        print(f"Error during database initialization: {e}")
        conn.rollback()


def insert_hacker_data(conn):
    name = ") INSERT INTO users (username, phone) VALUES ('i am hacker', '777777')"
    name = "somename', ''); INSERT INTO users (username, phone) VALUES ('i am superhacker', '1488-1488'); --"
    phone = '1234'
    sql = f"INSERT INTO users (username, phone) VALUES ('{name}', '{phone}');"

    with conn:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            conn.commit()
    conn.close()


def insert_execute_batch(conn):
    users = (
        ("Bob", "bob@mail.com"),
        ("Alice", "alice@mail.com"),
        ("John", "john@mail.com")
    )
    with conn.cursor() as cursor:
        execute_batch(
            cursor,
            "INSERT INTO users (username, email) VALUES (%s, %s)",
            users
        )
        conn.commit()


def insert_execute_values(conn):
    users = (
        ("Bob", "bob@mail.com"),
        ("Alice", "alice@mail.com"),
        ("John", "john@mail.com")
    )
    with conn.cursor() as cursor:
        execute_values(
            cursor,
            "INSERT INTO users (username, email) VALUES %s",
            users
        )
        conn.commit()


def batch_insert(conn, products):
    products = (product_dict_to_tuple(item) for item in products)
    with conn.cursor() as cursor:
        execute_values(
            cursor,
            '''INSERT INTO products
                   (name, price, quantity)
                VALUES
                    %s''',
            products
        )
        conn.commit()


def get_all_products(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM products ORDER BY price DESC')
        conn.commit()
        return cursor.fetchall()


def product_dict_to_tuple(d):
    return (
        d['name'],
        d['price'],
        d['quantity'],
    )


def main():
    conn = connect()
    # initialize_database(conn, 'init_products.sql')

    products = [
        {'name': 'milk', 'price': 12, 'quantity': 20},
        {'name': 'bread', 'price': 3, 'quantity': 10},
        {'name': 'orange', 'price': 6, 'quantity': 5}
    ]
    # batch_insert(conn, products)
    print(get_all_products(conn))

    conn.close()


if __name__ == '__main__':
    main()
