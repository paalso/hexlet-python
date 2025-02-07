import psycopg2
from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST

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

sql1 = "CREATE TABLE users (id SERIAL PRIMARY KEY, username VARCHAR(255), phone VARCHAR(255));"
# Запрос выполняется через создание объекта курсора
cursor = conn.cursor()
cursor.execute(sql1)
cursor.close() # в конце закрывается

sql2 = "INSERT INTO users (username, phone) VALUES ('jimmy', '123456789');"
cursor = conn.cursor()
cursor.execute(sql2)
cursor.close()

sql3 = "SELECT * FROM users;"
cursor = conn.cursor()
# Указатель на набор данных в памяти СУБД
cursor.execute(sql3)
for row in cursor:
    print(row)
cursor.close()

conn.commit() # Коммитим, т.е. сохраняем изменения в БД
conn.close() # Соединение нужно закрыть
