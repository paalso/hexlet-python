from faker import Faker

faker = Faker()


def build_user(data={}):
    default_data = _get_default_data()
    return {**default_data, **data}


def _get_default_data():
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
    }


def main():
    print(build_user())


if __name__ == '__main__':
    main()
