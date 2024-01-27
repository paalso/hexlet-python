from faker import Faker
from flask import Flask, request, jsonify, render_template, make_response

fake = Faker()
fake.seed_instance(1234)

domains = [fake.domain_name() for i in range(10)]
phones = [fake.phone_number() for i in range(10)]
message = 'It is a message'

app = Flask(__name__)




@app.route('/')
def index():
    return 'go to the /phones or /domains'


@app.route('/request-headers')
def get_request_headers():
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


@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        return 'Hello from POST /users'
    return 'Hello from GET /users'


@app.route('/json/')
def json():
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
