import os

from flask import (
    Flask,
    json,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


@app.route('/', methods=['GET'])
def index():
    cart = json.loads(request.cookies.get('cart', json.dumps({})))
    session_cart = session.get('cart', {})
    return render_template(
        'index.html',
        cart=cart,
        session_cart=session_cart
    )


# BEGIN (write your solution here)
@app.post('/cart-items')
def add_cart_item():

    selected_item = request.form.to_dict()
    item_name = selected_item.get('item_name')
    item_id = selected_item.get('item_id')

    cart = json.loads(request.cookies.get('cart', json.dumps({})))
    
    cart_item = cart.setdefault(item_id, {'name': item_name, 'count': 0})
    cart_item['count'] += 1
    encoded_сart = json.dumps(cart)

    response = make_response(redirect(url_for('index')))
    response.set_cookie('cart', encoded_сart)

    return response


@app.post('/cart-items/clean')
def clear_cart():
    response = make_response(redirect(url_for('index')))
    response.delete_cookie('cart')
    return response
# END


@app.post('/session-cart-items')
def add_session_cart_item():

    selected_item = request.form.to_dict()
    name = selected_item.get('item_name')
    print(f'name: {name}')

    session_cart = session.setdefault('cart', {'Three': 0, 'Four': 0})
    session_cart[name] += 1
    session.modified = True

    return redirect(url_for('index'))


@app.post('/session-cart-clean')
def clean_session_cart():
    session['cart'] = {'Three': 0, 'Four': 0}
    return redirect(url_for('index'))