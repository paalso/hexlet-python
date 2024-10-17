# https://ru.hexlet.io/courses/python-flask/lessons/flash/exercise_unit
# https://ru.hexlet.io/code_reviews/1474451

from flask import (
    Flask,
    flash,
    get_flashed_messages,
    render_template,
    redirect,
    url_for
)
import os

app = Flask(__name__)
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.secret_key = "secret_key"


# BEGIN (write your solution here)
@app.route('/')
def index():
    messages = get_flashed_messages(with_categories=False)
    message = messages[0] if messages else '' 
    return render_template(
        'index.html',
        message=message,
    )


@app.post('/courses')
def courses():
    flash('Course Added', 'success')
    return redirect(url_for('index'))
# END
