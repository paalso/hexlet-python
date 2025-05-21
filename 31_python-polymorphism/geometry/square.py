# https://ru.hexlet.io/code_reviews/1807254

from dispatcher import defmethod



# Конструктор, который принимает на вход длину стороны
# Селектор get_side, который возвращает сторону
# Полиморфную функцию get_area, которая возвращает площадь квадрата


# BEGIN (write your solution here)
# defmethod(type_name, method_name, fn):
def init():
    defmethod(
        __name__,
        'get_area',
        lambda self: self['data']['side'] ** 2)

def make(side):
    print(f'Making a {__name__} with the side {side}')
    return {'name': __name__, 'data':{'side': side}}

def get_square_side(self):
    return self['data']['side']
# END
