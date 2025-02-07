import os
import psycopg2
from dotenv import load_dotenv

from productDAO import ProductDAO
from catalog import Catalog


def connect():
    DB_URL = os.getenv('DB_URL')
    try:
        conn = psycopg2.connect(DB_URL)
        print('Successfully connected to database')
    except:
        print('Can`t establish connection to database')
        raise
    return conn


def main():
    load_dotenv()
    conn = connect()
    product_dao = ProductDAO(conn)
    catalog = Catalog(conn)

    product_name = 'kiwi'
    result = catalog.get_product(product_name)
    # result = product_dao.get_product(product_name)

    print(result)

    conn.close()


if __name__ == '__main__':
    main()
