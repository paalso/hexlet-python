# figure.py

from dispatcher import call


def get_area(self, *args):
    return call(self, get_area.__name__, args)
