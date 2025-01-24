import psycopg2
from psycopg2.extras import NamedTupleCursor

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


def get_all_products(conn):
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM products ORDER BY price DESC')
        conn.commit()
        result = cursor.fetchall()
    return result


def main():
    conn = connect()

    query1 = 'SELECT * FROM products'
    query2 = '''SELECT MAX(price * quantity)
                FROM products'''

    with conn.cursor(cursor_factory=NamedTupleCursor) as cursor:
        cursor.execute(query2)
        data = cursor.fetchall()
    
    print(data)
    print(data[0].max)

    conn.close()


if __name__ == '__main__':
    main()
