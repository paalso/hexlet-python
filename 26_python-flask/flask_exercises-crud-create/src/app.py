import os

from flask import (
    Flask,
    flash,
    get_flashed_messages,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
)

from repository import PostsRepository
from validator import validate

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.get('/posts')
def posts_get():
    repo = PostsRepository()
    messages = get_flashed_messages(with_categories=True)
    posts = repo.content()
    return render_template(
        'posts/index.html',
        posts=posts,
        messages=messages,
    )


@app.get('/posts/new')
def posts_new():
    post = {}
    errors = {}
    return render_template(
        'posts/new.html',
        post=post,
        errors=errors
    )


@app.post('/posts')
def posts_post():
    repo = PostsRepository()
    data = request.form.to_dict()
    errors = validate(data)
    if errors:
        return render_template(
            'posts/new.html',
            post=data,
            errors=errors,
            ), 422
    id = repo.save(data)
    flash('Post has been created', 'success')
    resp = make_response(redirect(url_for('posts_get')))
    resp.headers['X-ID'] = id
    return resp


# BEGIN (write your solution here)
@app.route('/posts/<id>/update')
def posts_edit(id): 
    repo = PostsRepository()
    try:
        post = repo.find(id)
        return render_template(
            'posts/edit.html',
            post=post
        )
    except KeyError:
        return 'Page not found', 404
    

@app.route('/posts/<id>/update', methods=['post'])
def posts_patch(id):
    data = request.form.to_dict()
    repo = PostsRepository()
    post = repo.find(id)
    errors = validate(data)
    if errors:
        return render_template(
            'posts/edit.html',
            post=post,
            errors=errors
        ), 422

    post.update(data)
    repo.save(post)
    flash('Post has been updated', 'success')

    return redirect(url_for('posts_get'))
# END
