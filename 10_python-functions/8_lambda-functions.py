# https://ru.hexlet.io/courses/python-functions/lessons/lambda-functions/exercise_unit
# https://ru.hexlet.io/code_reviews/273059

# Анонимные функции
# ==================

# Реализуйте функцию make_module так, чтобы она принимала аргумент step со
# значением по умолчанию равным 1, возвращала словарь с ключами "inc"
# (от "увеличить"/"increment") и "dec" (от "уменьшить"/"decrement"),
# по которым можно было бы получить лямбды, одна из которых добавляет,
# а вторая вычитает step из своего аргумента.
# Тело функции make_module должно состоять из одного выражения — return {…}.
# То есть лямбда-функции должны быть объявлены прямо в литерале словаря!


def make_module(step=1):
    return {
        'inc': lambda x: x + step,
        'dec': lambda x: x - step
    }


m = make_module()
print(m['inc'](10))     # 11
print(m['dec'](20))     # 19

m2 = make_module(step=2)
print(m2['inc'](1))     # 3
