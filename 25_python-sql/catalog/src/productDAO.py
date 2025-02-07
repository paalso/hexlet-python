from product import Product
from psycopg2.extras import RealDictCursor


class ProductDAO:
    def __init__(self, conn):
        self.conn = conn

    def get_product(self, product_name):
        query = 'SELECT * FROM products WHERE name = %s;'
        with self.conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (product_name,))
            data = cursor.fetchone()
            self.conn.commit()
        if data:
            product = Product(**data)
            return product
