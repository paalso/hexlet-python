from faker import Faker
from flask import (
    Flask,
    redirect,
    request,
    jsonify,
    render_template,
    make_response
)

from flask_app.data import generate_companies_old, generate_companies
from flask_app.course import Course
from flask_app.user import User

fake = Faker()
fake.seed_instance(1234)

domains = [fake.domain_name() for i in range(10)]
phones = [fake.phone_number() for i in range(10)]
USERS = [User(i + 1, fake.name()) for i in range(10)]

message = 'It is a message'

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/request-headers')
def get_request_headers():
    print("\nPrinting request.headers...") # Выводит все заголовки
    print(request.headers) # Выводит все заголовки
    return str(request.headers)


@app.route('/phones')
def get_phones():
    return jsonify(phones)


@app.route('/domains')
def get_domains():
    return jsonify(domains)


@app.route('/message')
def get_message():
    return message


@app.route('/json/')
def json():
    print("\nPrinting Response...") # Выводит все заголовки
    return {'json': 42} # Возвращает тип application/json


@app.route('/not_found')
def not_found():
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


@app.route('/greet/<name>')
def greet(name):
    return render_template(
        'greet.html',
        name=name
    )


@app.route('/users')
def users():
    name_piece = request.args.get('name_piece')
    filtered_users = USERS

    if name_piece:
        filtered_users = [user for user in USERS if name_piece.lower() in user.name.lower()]

    return render_template(
        'users/view.html',
        dirname='users',
        items=filtered_users,
        name_piece=(name_piece or '')
    )


@app.post('/users')
def users_post():
    repo = UserRepository()
    user = request.form.to_dict()
    errors = validate(user)
    if errors:
        return render_template(
          'users/new.html',
          user=user,
          errors=errors,
        )
    repo.save(user)
    return redirect('/users', code=302)


@app.route('/users/<int:id>')
def user(id):
    user = _find_by_id(USERS, id)
    if user is None:
        return 'User not found\n', 404
    return render_template(
        'users/show.html',
        user=user
    )


@app.route('/courses/')
def courses():
    courses = _get_courses()

    return render_template(
        'courses/view.html',
        courses=courses
    )


@app.route('/process')
def process():
    data = request.args.get('data')
    processed_result = ' '.join(token.upper() for token in data.split())

    return render_template(
        'items_result.html',
        processed_result=processed_result,
        data=data,
    )


def _get_courses():
    courses = [
        Course('1', 'Python for beginners'),
        Course('2', 'Python for advanced users'),
        Course('3', 'Python for girls'),
    ]
    return courses


def _get_users(users):
    return users


def _find_by_id(data, id_):
    for item in data:
        if item.id == id_:
            return item
