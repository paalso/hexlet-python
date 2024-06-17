from dotenv import load_dotenv
from flask import Flask, session, jsonify
from flask import render_template
from flask import request
import os
import pprint
import uuid

from flask_example.repo import Repository

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
repo = Repository()


# Пример маршрута для установки значений сессии
@app.route('/')
def hello():
    _print_session_info(session)
    return render_template('session/index.html')


@app.route('/set_session')
def set_session():
    user_name = request.args.get('user_name', '')
    user_id = request.args.get('user_id', '')
    session_data_status = ''

    if user_name and user_id:
        user = {'id': user_id, 'name': user_name}
        repo.save(user)
        session_data_status = 'Session data set'
        print(f'name = {user_name}, id = {user_id}')

    _print_session_items(session)

    return render_template(
        'session/session-setup.html',
        user_name=user_name,
        user_id=user_id,
        session_data_status = session_data_status
    )


@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('session/index.html')


@app.route('/test/<user_id>')
def test_id(user_id):
    # Извлечение данных по идентификатору
    try:
        retrieved_user = repo.find(user_id)
    except KeyError:
        retrieved_user = "User not found"
    
    return jsonify(retrieved_user)


# Пример маршрута для получения значений сессии
@app.route('/get_session')
def get_session():
    user_id = session.get('user_id', 'Not set')
    user_name = session.get('user_name', 'Not set')
    return jsonify(user_id=user_id, user_name=user_name)


def _print_session_info(session):
    print('\nSession:')
    # print(f'Session items: {session.items()}')
    print('Session items')
    pprint.pprint(session.items())
    print()


def _print_session_items(session):
    print('Session items')
    for k, v in session.items():
        print(f'{k} - {v}')


if __name__ == '__main__':
    app.run(debug=True)
