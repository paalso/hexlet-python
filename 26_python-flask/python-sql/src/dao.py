import psycopg2

from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST
from models import Course
from models import Lesson


def get_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST
        )
    except:
        print('Can`t establish connection to database')
        raise
    return conn


def commit(conn):
    conn.commit()


def save_course(conn, course):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        if course.id is None:
            cur.execute(
                "INSERT INTO courses (name, description) VALUES (%s, %s) RETURNING id;",
                (course.name, course.description)
            )
            course.id = cur.fetchone().id
        else:
            cur.execute(
                "UPDATE courses SET name = %s, description = %s WHERE id = %s;",
                (course.name, course.description, course.id)
            )
    return course.id


def find_course(conn, course_id):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT id, name, description FROM courses WHERE id = %s;", (course_id,))
        result = cur.fetchone()
        if result:
            return Course(
                id=result.id,
                name=result.name,
                description=result.description
                )
    return None


def get_all_courses(conn):
    with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
        cur.execute("SELECT id, name, description FROM courses;")
        return [
            Course(id=row.id, name=row.name, description=row.description)
            for row in cur.fetchall()
        ]


def save_lesson(conn, lesson):
    id = lesson.id
    if not id:
        query = '''INSERT INTO lessons (name, text, course_id)
                   VALUES (%(name)s, %(text)s, %(course_id)s)
                   RETURNING id;'''
    else:
        query = '''UPDATE lessons
                   SET name = %(name)s, text = %(text)s, course_id = %(course_id)s
                   WHERE id = %(id)s
                   RETURNING id;'''
    with conn.cursor() as cursor:
        cursor.execute(query, lesson.__dict__)
        id = cursor.fetchone()[0]
    return id


def find_lesson(conn, id):
    query = '''SELECT name, text, course_id, id FROM lessons
               WHERE id = %s;'''
    with conn.cursor() as cursor:
        cursor.execute(query, (id,))
        result = cursor.fetchone()
    if result:
        return Lesson(*result)


def delete_course(conn, id):
    query = '''DELETE FROM courses
               WHERE id = %s RETURNING id;'''
    with conn.cursor()  as cursor:
        cursor.execute(query, (id,))
        result = cursor.fetchone()
    return result


def get_course_lessons(conn, course_id):
    query = '''SELECT name, text, course_id, id FROM lessons
               WHERE course_id = %s
               ORDER BY id;'''
    with conn.cursor()  as cursor:
        cursor.execute(query, (course_id,))
        result = [Lesson(*item) for item in cursor.fetchall()]
    return result


def main():
    conn = get_connection()
    
    print(get_course_lessons(conn, 4))
    commit(conn)

    conn.close()


if __name__ == '__main__':
    main()



