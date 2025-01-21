from flask import Flask, render_template, request

from src.repository import PostsRepository

app = Flask(__name__)

repo = PostsRepository(50)


@app.route('/')
def index():
    return render_template('index.html')


# BEGIN
@app.route('/posts')
def posts_index():
    posts = repo.content()
    request_args = request.args
    page = max(1, request_args.get('page', default=1, type=int))
    per = request_args.get('per', default=5, type=int)
    filtered_posts = _get_page_items(posts, page, per)
    return render_template(
        'posts/index.html',
        collection=filtered_posts,
        page=page,
        per=per
    )


@app.route('/posts/<string:slug>')
def posts_show(slug):
    post_by_slug = repo.find(slug)
    if post_by_slug:
        return render_template(
            'posts/show.html',
            element=post_by_slug,
        )
    return 'Page not found', 404


def _get_page_items(items, page, per):
    from_id = (page - 1) * per
    to_id = from_id + per
    return items[from_id: to_id]
# END
