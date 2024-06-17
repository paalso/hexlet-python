from  collections import defaultdict
from dotenv import load_dotenv
from flask import Flask, jsonify, redirect, render_template, request
import os
import pprint
import uuid

from flask_example.repo import UserRepository

STORAGE = 'flask_example/data/db.dat'

app = Flask(__name__)

repo = UserRepository(STORAGE)

@app.route('/')
def root():
    return render_template('users_handling/index.html')


@app.route('/users/new')
def users_new():
    user = {'name': '',
            'email': '',
            'password': '',
            'passwordConfirmation': '',
            'city': ''}
    errors = {}

    return render_template(
        'users_handling/new.html',
        user=user,
        errors=errors
    )


@app.get('/users')
def users():
    users = repo.get_all()
    return render_template(
        '/users_handling/show.html',
        users=users
    )


@app.post('/users')
def users_post():
    user = request.form.to_dict()
    errors = validate(user)
    print(f'Errors: {errors}')
    if errors:
        return render_template(
          '/users_handling/new.html',
          user=user,
          errors=errors,
        )
    repo.save(user)
    return redirect('/users', code=302)


@app.get('/users/<id_>')
def user(id_):
    user = repo.find_by_id(int(id_))
    if not user:
        return 'User not found'

    return render_template(
        '/users_handling/show_user.html',
        user=user
    )


def validate(user):
    errors = defaultdict(list)
    _validate_name(user['name'], errors)
    _validate_email(user['email'], errors)
    return errors


def _validate_name(name, errors):
    if len(name) < 3:
        errors['name'].append('name is too short')
    if all(not char.isalpha() for char in name):
        errors['name'].append('name must contain letters')
    return errors


def _validate_email(email, errors):
    if '@' not in email:
        errors['email'].append('email must contain @')
    return errors
