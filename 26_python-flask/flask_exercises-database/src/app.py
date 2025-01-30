import os
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
)

from repository import ProductsRepository, get_db

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')

repo = ProductsRepository(get_db(app))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/products')
def products():
    products = repo.get_entities()
    return render_template('products/index.html', products=products)


# BEGIN (write your solution here)
@app.route('/products/new')
def new_product():
    return render_template('products/new.html')
# END