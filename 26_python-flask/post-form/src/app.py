# https://ru.hexlet.io/courses/python-flask/lessons/post-form/exercise_unit
# https://ru.hexlet.io/code_reviews/1467155

from flask import Flask, redirect, render_template, request
from dotenv import load_dotenv
import os

# BEGIN (write your solution here)
from validator import validate
# END

from data import Repository


app = Flask(__name__)

load_dotenv()
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

repo = Repository()


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/courses')
def courses_get():
    courses = repo.content()
    return render_template(
        'courses/index.html',
        courses=courses,
        )


# BEGIN (write your solution here)
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
# END
