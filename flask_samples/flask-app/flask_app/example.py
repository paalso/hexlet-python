from faker import Faker
from flask import Flask, request, jsonify, render_template, make_response
from flask_app.data import generate_companies_old, generate_companies
from flask_app.course import Course

fake = Faker()
fake.seed_instance(1234)

domains = [fake.domain_name() for i in range(10)]
phones = [fake.phone_number() for i in range(10)]
message = 'It is a message'
available_routes = [
    'request-headers',
    'domains',
    'phones',
    'message',
    'users',
    'json/',
    'html/',
    'not_found',
    'users/',
    '/companies',
]

companies_old = generate_companies_old(100)
companies = generate_companies(100)

app = Flask(__name__)


@app.route('/')
def index():
    routes = "\n".join(available_routes)
    return "<a href='/companies'>Companies</a>"
    return routes


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
    print(Response)
    return {'json': 42} # Возвращает тип application/json


@app.route('/html/')
def html():
    return render_template('index.html') # Возвращает тип text/html


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


@app.route('/companies')
def get_companies():
    page = request.args.get('page', 1, int)
    per = request.args.get('per', 5, int)
    result = jsonify(_get_page_content(companies_old, page, per))
    return result


@app.route('/companies/<int:company_id>')
def get_company(company_id):
    company = _find_by_id(companies, company_id)
    if company:
        return company
    return 'Page not found', 404


@app.route('/users/<id>')
def users(id):
    return render_template(
        'index.html',
        name=id,
    )


@app.route('/courses/')
def courses():
    courses = _get_courses() # Возвращает список курсов, которые представлены словарем
    return render_template(
        'courses/view.html',
        courses=courses
    )


def _find_by_id(data, id_):
    for item in data:
        if item['id'] == id_:
            return item


def _get_page_content(data, from_page, per_page):
    from_id = (from_page - 1) * per_page
    return data[from_id : from_id + per_page]


def _get_courses():
    courses = [
        Course('1', 'Python for beginners'),
        Course('2', 'Python for advanced users'),
        Course('3', 'Python for girls'),
    ]
    return courses