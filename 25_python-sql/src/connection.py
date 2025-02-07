import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.extras import DictCursor

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


def create_post(conn, post_dict):
    query = '''INSERT INTO posts (title, content, author_id)
               VALUES (%(title)s, %(content)s, %(author_id)s)
               RETURNING id;''' 
    with conn.cursor() as cursor:
        cursor.execute(query, post_dict)
        id_ = cursor.fetchone()[0]
    conn.commit()
    return id_


def add_comment(conn, comment_dict):
    query = '''INSERT INTO comments (post_id, author_id, content)
               VALUES (%(post_id)s, %(author_id)s, %(content)s)
               RETURNING id;''' 
    with conn.cursor() as cursor:
        cursor.execute(query, comment_dict)
        id_ = cursor.fetchone()[0]
    conn.commit()
    return id_


def get_latest_posts(conn, n):
    get_posts_query = \
        '''SELECT * FROM posts
           ORDER BY created_at DESC
           LIMIT %s;''' 

    get_comments_query = \
        '''SELECT id, author_id, content, created_at FROM comments
           WHERE post_id = %s;''' 

    with conn.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute(get_posts_query, (n,))
        posts = cursor.fetchall()

        result = []
        for post in posts:
            post = dict(post)
            post_id = post.get('id')
            cursor.execute(get_comments_query, (post_id,))
            comments = cursor.fetchall()
            post['comments'] = [dict(comment) for comment in comments]
            result.append(post)

        conn.commit()
    return result

def main():
    conn = connect()

    # post_dict = {'title': 'Lorem ipsum',
    #              'content': 'Lorem ipsum...',
    #              'author_id': 1}    

    # result = create_post(conn, post_dict)
    # print(result)

    # comment_dict = {'content': 'Lorem ipsum',
    #                 'post_id': 1,
    #                 'author_id': 1}    

    # result = add_comment(conn, comment_dict)

    result = get_latest_posts(conn, 10)
    for e in result:
        print(e)

    conn.close()


if __name__ == '__main__':
    main()
