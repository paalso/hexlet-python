from faker import Faker

faker = Faker()


def get_default_data():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
    }


def build_user(data={}):
    default_data = get_default_data()
    return {**default_data, **data}


def for_each(coll, func):
    for c in coll:
        func(c)


class Sqrer:
    def __init__(self, dependency):
        self.dependency = dependency

    def sqr(self):
        return self.dependency.get_value() ** 2
