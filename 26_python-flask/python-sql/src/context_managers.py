import psycopg2
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


def get_all_movies(conn):
    sql = 'SELECT * FROM movies'
    cursor = conn.cursor()
    cursor.execute(sql)
    result = [row for row in cursor]
    cursor.close()
    return result


def add_movies(conn):
    sql = '''
        INSERT INTO movies
            (title, release_year, duration)
        VALUES
            ('Godfather', 1972, 175),
            ('The Green Mile', 1999, 189);'''

    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()


def main():
    conn = connect()
    if conn:
        sql_file_path = "init.sql"
        initialize_database(conn, sql_file_path)
        print(get_all_movies(conn))
        add_movies(conn)
        print(get_all_movies(conn))
        conn.commit()
        conn.close()


if __name__ == '__main__':
    main()


# https://ru.hexlet.io/code_reviews/1691518