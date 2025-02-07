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


def get_all_cars(conn):
    sql = '''
        SELECT * FROM cars
        ORDER BY brand'''
    cursor = conn.cursor()
    with cursor:
        cursor.execute(sql)
        return(list(cursor))


def main():
    conn = connect()
    with conn:
        sql_file_path = "init_cars.sql"
        initialize_database(conn, sql_file_path)

        print(get_all_cars(conn))


if __name__ == '__main__':
    main()
