def for_each(collection, callback):
    for e in collection:
        callback(e)


def for_each_in_args(callback, *collection):
    for e in collection:
        callback(e)


def sqr(x):
    return x * x


def summa(x, y):
    return x + x
