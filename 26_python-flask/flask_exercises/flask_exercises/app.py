from dotenv import load_dotenv
from faker import Faker
from flask import Flask, request, jsonify, render_template, redirect
import os

from flask_exercises.data import (
    generate_companies_old,
    generate_companies_new,
    generate_users,
    Repository
)
from flask_exercises.course import Course

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# 5. Flask
# https://ru.hexlet.io/courses/python-flask/lessons/flask/exercise_unit
@app.route('/')
def hello_hexlet():
    return 'Welcome to Hexlet!'
# -----------------------------------------------------------------------

# 6. Handlers
# https://ru.hexlet.io/courses/python-flask/lessons/handlers/exercise_unit
fake = Faker()
fake.seed_instance(123  )

domains = [fake.domain_name() for i in range(10)]
phones = [fake.phone_number() for i in range(10)]

@app.route('/phones')
def get_phones():
    return jsonify(phones)


@app.route('/domains')
def get_domains():
    return jsonify(domains)


# Http session
# https://ru.hexlet.io/courses/python-flask/lessons/http-session/exercise_unit
def get_page_content(data, from_page, per_page):
    from_id = (from_page - 1) * per_page
    return data[from_id : from_id + per_page]


@app.route('/companies')
def get_companies():
    generate_companies = generate_companies_old
    companies = generate_companies(100)
    page = request.args.get('page', 1, int)
    per = request.args.get('per', 5, int)
    result = jsonify(get_page_content(companies, page, per))
    return result
# -----------------------------------------------------------------------

# Dynamic routing
# https://ru.hexlet.io/courses/python-flask/lessons/dynamic-routing/exercise_unit
@app.route('/companies/<int:company_id>')
def get_company(company_id):
    generate_companies = generate_companies_new
    companies = generate_companies(100)
    company = _find_by_id(companies, company_id)
    if company:
        return company
    return 'Page not found', 404


def _find_by_id(data, id_):
    for item in data:
        if item['id'] == id_:
            return item
# -----------------------------------------------------------------------
        

# Templates, get-form
# https://ru.hexlet.io/courses/python-flask/lessons/templates/exercise_unit
# https://ru.hexlet.io/courses/python-flask/lessons/get-form/exercise_unit
# https://ru.hexlet.io/code_reviews/1310635
# https://ru.hexlet.io/code_reviews/1317515
users = generate_users(100)


@app.route('/users')
def get_all_users():
    filtered_users = users

    term = request.args.get('term')
    if term:
        filtered_users = \
            [user for user in users if 
             user['first_name'].lower().startswith(term.lower())]

    return render_template(
        'users/index.html',
        users=filtered_users,
        search=term or '',
        full_name=full_name
    )


@app.route('/users/<int:user_id>')
def get_users_by_id(user_id):
    filtered_users = _find_items_by_id(users, user_id)
    if not filtered_users:
        return 'Page not found', 404
    return render_template(
        'users/show.html',
        users=filtered_users,
        full_name=full_name
    )


def full_name(first_name, last_name):
    return f'{first_name} {last_name}'


def _find_items_by_id(data, key_value, key='id'):
    return list(filter(lambda item: item[key] == key_value, data))
# -----------------------------------------------------------------------

# post-form
# https://ru.hexlet.io/courses/python-flask/lessons/post-form/exercise_unit

from flask_exercises.validator import validate

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
repo = Repository()


@app.get('/courses')
def courses_get():
    courses = repo.content()
    return render_template(
        'courses/index.html',
        courses=courses,
    )


@app.get('/courses/new')
def courses_new():
    course = {
        'title': '',
        'paid': True
    }
    errors = {}
    return render_template(
        'courses/new.html',
        course=course,
        errors=errors
    )


@app.post('/courses')
def courses_post():
    course = request.form.to_dict()
    print(f'course: {course}')
    errors = validate(course)
    if errors:
        print(errors)
        return render_template(
            'courses/new.html',
            course=course,
            errors=errors
        ), 422
    repo.save(course)
    return redirect('/courses', code=302)
