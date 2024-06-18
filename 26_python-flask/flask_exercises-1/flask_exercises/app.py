from dotenv import load_dotenv
from faker import Faker
from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    flash,
    get_flashed_messages
)
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
    print(app.secret_key)
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
generated_users = generate_users(100)


@app.route('/users')
def users():
    filtered_users = generated_users

    term = request.args.get('term')
    if term:
        filtered_users = \
            [user for user in generated_users if 
             user['first_name'].lower().startswith(term.lower())]

    return render_template(
        'users/index.html',
        users=filtered_users,
        search=term or '',
        full_name=full_name
    )


@app.route('/users/<int:id>')
def user_page(id):
    filtered_by_id = _find_items_by_id(generated_users, id)

    if not filtered_by_id:
        return 'Page not found', 404
    
    user = filtered_by_id[0]
    return render_template(
        'users/show.html',
        user=user,
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
def courses():
    courses = repo.content()
    messages = get_flashed_messages(with_categories=True)
    print(messages) 
    return render_template(
        'courses/index.html',
        courses=courses,
        messages=messages
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
    errors = validate(course)
    if errors:
        flash('Some errors happened while creating', 'error')
        messages = _print_errors_to_console(errors)
        return render_template(
            'courses/new.html',
            course=course,
            errors=errors,
            messages=messages
        ), 422
    repo.save(course)
    flash('Course created successfully', 'success')
    return redirect(url_for('courses'), code=302)


def _print_errors_to_console(errors):
    print()
    print(f'errors:{errors}')
    print()
    messages = messages_with_categories = get_flashed_messages(with_categories=True)
    print(f'messages with categories: {messages_with_categories}')
    messages_without_categories = get_flashed_messages(with_categories=False)
    print()
    print(f'messages without categories: {messages_without_categories}')
    print()
    return messages

# -----------------------------------------------------------------------
@app.post('/foo')
def foo():
    # Добавление флеш-сообщения.
    # Оно станет доступным только на следующий HTTP-запрос.
    # 'success' — тип флеш-сообщения. Используется при выводе для форматирования.
    # Например, можно ввести тип success и отражать его зеленым цветом. На Хекслете такого много.
    flash('This is a message', 'success')
    flash('another message', 'error')
    return redirect('/bar')


@app.get('/bar')
def bar():
    # Извлечение flash-сообщений, которые установлены на предыдущем запросе
    messages = get_flashed_messages(with_categories=True)
    print(messages)  # => [('success', 'This is a message')]
    return render_template(
        'bar.html',
        messages=messages,
    )


@app.get('/goodbye')
def goodbye():
    return 'Goodbye!'
