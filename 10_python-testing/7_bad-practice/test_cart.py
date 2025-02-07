# https://ru.hexlet.io/courses/python-testing/lessons/bad-practice/exercise_unit
# https://ru.hexlet.io/code_reviews/476489

# Плохие и хорошие практики тестирования
# =======================================

"""
Напишите тесты для корзины интернет-магазина. Интерфейс:

make_cart() – создаёт новую корзину (объект).
add_item(good, count) – добавляет в корзину товары и их количество. Товар – это объект, у которого два свойства: name (имя) и price (стоимость).
get_items() – возвращает список товаров в формате [{ good, count }, { good, count }, ...]
get_cost() – возвращает стоимость корзины. Стоимость корзины высчитывается как сумма всех добавленных товаров с учётом их количества.
get_count() – возвращает общее количество товаров в корзине.
"""

from cart import implementations

make_cart = implementations["wrong1"]
make_cart = implementations["wrong2"]
make_cart = implementations["wrong3"]
make_cart = implementations["right"]


# BEGIN (write your solution here)
import pytest


@pytest.fixture
def get_empty_cart():
    return make_cart()


@pytest.fixture
def get_cart():
    cart = make_cart()
    cart.add_item({ 'name': 'car', 'price': 3 }, 5)
    cart.add_item({ 'name': 'house', 'price': 10 }, 2)
    return cart


def test_empty_cart(get_empty_cart):
    cart = get_empty_cart
    assert cart.get_items() == []
    assert cart.get_cost() == 0
    assert cart.get_count() == 0


def test_cart(get_cart):
    cart = get_cart
    assert cart.get_items() == [
        {'good': { 'name': 'car', 'price': 3 }, 'count': 5},
        {'good': { 'name': 'house', 'price': 10 }, 'count': 2},
    ]
    assert cart.get_count() == 7
    assert cart.get_cost() == 35

# END
