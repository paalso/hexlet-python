import os
from dotenv import load_dotenv
from flask import (
    abort,
    Flask,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from repository import ProductsRepository, get_db
from validator import validate


load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL') or ...
app.config['DATABASE_URL'] = DATABASE_URL

repo = ProductsRepository(get_db(app))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    products = repo.get_entities()
    return render_template('products/index.html', products=products)


# BEGIN (write your solution here)
@app.route('/products/<id>')
def show_product(id):
    product = repo.find(id)
    if product:
        return render_template(
            'products/show.html',
            product=product
        )
    abort(404)


@app.route('/products/new')
def new_product():
    product = {}
    errors = {}
    return render_template(
        'products/new.html',
        product=product,
        errors=errors
    )

@app.post('/products')
def products_post():
    product = request.form.to_dict()
    errors = validate(product)
    if errors:
        return render_template(
            'products/new.html',
            product=product,
            errors=errors
        ), 422

    repo.save(product)
    return redirect(url_for('products'))
# END