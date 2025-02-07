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


# принимает соединение и месяц
# возвращает общую сумму заказов каждого покупателя за этот месяц
def get_order_sum(conn, month):
    query = f'''SELECT c.customer_name, SUM(o.total_amount)
                FROM customers c JOIN orders o ON c.customer_id = o.customer_id
                WHERE EXTRACT(MONTH FROM o.order_date) = {month}
                GROUP BY c.customer_name;'''

    with conn.cursor() as cursor:
        cursor.execute(query)
        query_result = cursor.fetchall()
        conn.commit()

    report = '\n'.join(
        f'Покупатель {name} совершил покупок на сумму {int(sum)}'
        for name, sum in query_result
    )

    return report


def main():
    conn = connect()
    month = 2
    print(get_order_sum(conn, month))

    conn.close()


if __name__ == '__main__':
    main()
