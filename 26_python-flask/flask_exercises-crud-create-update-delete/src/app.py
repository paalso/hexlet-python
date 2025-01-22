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
    print(f'Post has been created\nid:{id}\ndata:{data}')
    resp = make_response(redirect(url_for('posts_get')))
    resp.headers['X-ID'] = id
    return resp


@app.route('/posts/<id>/update', methods=['GET', 'POST'])
def post_update(id):
    repo = PostsRepository()
    post = repo.find(id)
    errors = []

    if request.method == 'GET':
        return render_template(
                'posts/edit.html',
                post=post,
                errors=errors,
                data=post,
                )

    if request.method == 'POST':
        data = request.form.to_dict()

        errors = validate(data)
        if errors:
            return render_template(
                'posts/edit.html',
                post=post,
                data=data,
                errors=errors,
                ), 422

        post['title'] = data['title']
        post['body'] = data['body']
        repo.save(post)
        flash('Post has been updated', 'success')
        return redirect(url_for('posts_get'))


@app.route('/posts/count')
def posts_count():
    repo = PostsRepository()
    count = len(repo.content())
    print(count)
    return {'count': count}


@app.post('/posts/<id>/delete')
def post_delete(id):
    repo = PostsRepository()
    try:
        repo.destroy(id)
        flash('Post has been removed', 'success')
    except Exception:
        flash(f'Failed to remove post {id}', 'error')
    return redirect(url_for('posts_get'))
