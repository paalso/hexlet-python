import os
from hashlib import sha256

from flask import (
    Flask,
    flash,
    get_flashed_messages,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


users = [
    {'name': 'tota', 'password': sha256(b'password123').hexdigest()},
    {'name': 'alice', 'password': sha256(b'donthackme').hexdigest()},
    {'name': 'bob', 'password': sha256(b'qwerty').hexdigest()},
]


def get_user(form_data, repo):
    name = form_data['name']
    password = sha256(form_data['password'].encode()).hexdigest()
    for user in repo:
        if user['name'] == name and user['password'] == password:
            return user


@app.route('/')
def index():
    messages = get_flashed_messages(with_categories=True)
    current_user = session.get('user')
    return render_template(
        'index.html',
        messages=messages,
        current_user=current_user,
        )


# BEGIN (write your solution here)
@app.post('/session/new')
def new_session():
    form_data = request.form.to_dict()
    user = get_user(form_data, users)
    if user:
        user_name = user['name']
        session['user'] = {'name': user_name}
        flash('User successfully logged in', 'success')
    else:
        flash('Wrong password or name', 'error')
    return redirect(url_for('index'))


@app.route('/session/delete', methods=['POST', 'DELETE'])
def delete_session():
    session.pop('user')
    return redirect(url_for('index'))
# END
