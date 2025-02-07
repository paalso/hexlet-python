from productDAO import ProductDAO
from dataclasses import asdict
from psycopg2.extras import RealDictCursor


class Catalog:
    def __init__(self, conn):
        self.product_dao = ProductDAO(conn)

    def get_product(self, product_name):
        product = self.product_dao.get_product(product_name)
        if product:
            return asdict(product)
        raise KeyError('Product not found')
