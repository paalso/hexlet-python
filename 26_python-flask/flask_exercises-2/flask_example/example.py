from dotenv import load_dotenv
from faker import Faker
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from flask import make_response
import os
import pprint

from flask_example.data import generate_companies, generate_users
from flask_example.data import Course
from flask_example.data import Repository

fake = Faker()
fake.seed_instance(1234)

load_dotenv()

# Это callable WSGI-приложение
app = Flask(__name__)

# Устанавливаем секретный ключ для сессий
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Создаем экземпляр хранилища объектов
repo = Repository()

# Пример сохранения данных в сессии
@app.route('/initialize')
def initialize():
    # pprint.pprint(f'Session values:\n{repo.content()}')
    user1 = {"name": "John"}
    user2 = {"name": "Jane"}
    
    # Сохранение данных в сессии
    repo.save(user1)
    repo.save(user2)

    return jsonify(user1_id=user1['id'], user2_id=user2['id'])


@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/test/<user_id>')
def test_id(user_id):
    # Извлечение данных по идентификатору
    try:
        retrieved_user = repo.find(user_id)
    except KeyError:
        retrieved_user = "User not found"
    
    return jsonify(retrieved_user)


@app.route('/methods', methods=['GET', 'POST'])
def hello():
    # Получить доступ к содержимому запроса можно через специальный объект request
    if request.method == 'POST':
        return 'Hello, POST!'
    return 'Hello, GET!'


@app.get('/get')
def hello_get():
    return 'Hello, GET!'


@app.post('/post')
def hello_post():
   return 'Hello, POST!'

# --- handlers -----------------------------------------------------------
domains = [fake.domain_name() for i in range(10)]
phones = [fake.phone_number() for i in range(10)]

@app.route('/domains')
def get_domains():
    return jsonify(domains)


@app.route('/phones')
def get_phones():
    return jsonify(phones)
# --------------------------------------------------------------------------


@app.route('/headers')
def get_headers():
    print(request.headers) # Выводит все заголовки
    print(request.method) # Выводит все заголовки
    return str(request.headers)


@app.route('/json/')
def json():
    return {'json': 42} # Возвращает тип application/json


@app.route('/html/')
def html():
    return render_template('index.html') # Возвращает тип text/html


@app.errorhandler(404)
def not_found(error):
    return 'Oops!', 404


@app.route('/foo')
def foo():
    response = make_response('foo')
    # Устанавливаем заголовок
    response.headers['X-Parachutes'] = 'parachutes are cool'
    # Меняем тип ответа
    response.mimetype = 'text/plain'
    # Задаем статус
    response.status_code = 418
    # Устанавливаем cookie
    response.set_cookie('foo', 'bar')
    return response


@app.post('/response302')
def response302():
    return 'Some response 302', 302


# --- http-session ---------------------------------------------------------
companies = generate_companies(100)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/companies')
def get_companies():
    page = request.args.get('page', 1, type=int)
    per = request.args.get('per', 5, type=int)
    companies_to_page = _get_page_items(companies, page, per)
    return jsonify(companies_to_page)


def _get_page_items(items, page, per):
    from_id = (page - 1) * per
    return items[from_id: from_id + per]
# --------------------------------------------------------------------------


@app.route('/courses/<course_id>/lessons/<lesson_id>')
def course_lesson(course_id, lesson_id):
    return f'Course id: {course_id}, Lesson id: {lesson_id}'


# --- Dynamic routing ------------------------------------------------------
@app.route('/companies/<int:id>')
def get_company(id):
    company = _get_items_by_key(companies, 'id', id)
    if company:
        return jsonify(company)
    return 'Page not found', 404
# --------------------------------------------------------------------------

# --- templates ------------------------------------------------------------
# --- get-form -------------------------------------------------------------

# https://ru.hexlet.io/code_reviews/1317515
users = generate_users(100)


@app.route('/users')
def get_users():
    term = request.args.get('term', '').strip().lower()
    filtered_users = [user
                      for user in users
                      if user['first_name'].lower().startswith(term)]
    return render_template(
        'users/index.html',
        users=filtered_users,
        term=term)

@app.route('/users/<id>')
def get_user(id):
    user = _get_items_by_key(users, 'id', int(id))
    if user is None:
        return 'Page not found', 404
    return render_template('users/show.html',
                           user=user)
# --------------------------------------------------------------------------


def _get_items_by_key(items, key, value):
    for item in items:
        if item[key] == value:
            return item


@app.route('/courses/')
def courses():
    courses = _get_courses() # Возвращает список курсов, которые представлены словарем

    return render_template(
        'courses/view.html',
        courses=courses
    )


@app.route('/courses/<int:id>')
def course(id):
    courses = _get_courses()
    print(courses)
    course = next(filter(lambda e: e.id == id, courses), None)
    if not course:
        return "Course not found", 404    
    return render_template(
        'course/view.html',
        course=course
    )


def _get_courses():
    courses = [
        Course(1, 'Python for beginners'),
        Course(2, 'Python for advanced users'),
        Course(3, 'Python for girls'),
        Course(4, 'JS for beginners'),
        Course(5, 'JS for advanced users'),
        Course(6, 'JS for girls'),
        Course(7, 'C for beginners'),
        Course(8, 'C for advanced users'),
        Course(9, 'C for girls'),
    ]
    return courses


@app.route('/youngsters/')
def youngsters():
    term = request.args.get('term').strip().lower()
    youngsters = _get_youngsters()
    if not term:
        filtered_youngsters = youngsters
        search=''
    else:    
        filtered_youngsters = list(
            filter(lambda item: term.lower() in item, youngsters))
        search=term

    return render_template(
        'youngsters/view.html',
        youngsters=filtered_youngsters,
        search=search
    )


def _get_youngsters():
    return ['mike', 'mishel', 'adel', 'keks', 'kamila']


def main():
    print("Hello, Flask!")


if __name__ == '__main__':
    main()
