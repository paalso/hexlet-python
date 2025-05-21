# circle.py

from dispatcher import defmethod
from math import pi


def init():
    print(f'Initaliazing {__name__}')
    defmethod(__name__, 'get_area', lambda self: pi * self['data']['radius'] ** 2)


def make(radius):
    print(f'Making a {__name__} with the radius {radius}')
    return {'name': __name__, 'data': {'radius': radius}}


def get_circle_radius(self):
    return self['data']['radius']
 