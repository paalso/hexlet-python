def without(coll, *values):
    """ Принимает первым параметром список и возвращает его копию, из которой
        исключены значения, переданные вторым и последующими параметрами"""
    return list(filter(lambda e: e not in values, coll))
