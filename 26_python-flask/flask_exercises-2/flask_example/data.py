import random
import sys
import uuid
from flask import session
from faker import Faker

SEED = 1234


class Course():
    def __init__(self, id_, name):
       self.id = id_
       self.name = name


def generate_companies(companies_count):
    fake = Faker()
    fake.seed_instance(SEED)
    ids = list(range(companies_count))
    random.seed(SEED)
    random.shuffle(ids)
    companies = []
    for i in range(companies_count):
        companies.append({
            "name": fake.company(),
            "phone": fake.phone_number(),
        })
    return companies


def generate_companies(companies_count):
    fake = Faker()
    fake.seed_instance(SEED)
    ids = list(range(companies_count))
    random.seed(SEED)
    random.shuffle(ids)
    companies = []
    for i in range(companies_count):
        companies.append({
            "id": ids[i],
            "name": fake.company(),
            "phone": fake.phone_number(),
        })

    return companies


def generate_users(users_count):
    fake = Faker()
    fake.seed_instance(SEED)

    ids = list(range(1, users_count))
    random.seed(SEED)
    random.shuffle(ids)

    users = []

    for i in range(users_count - 1):
        users.append({
            'id': ids[i],
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.free_email(),
        })

    return users


class Repository:
    # Session values sample:
    # dict_values(
    #     [{'id': '23f11777-e30a-403f-a6da-6dcae0708835', 'name': 'Jane'},
    #      {'id': '4150ae36-09e3-4927-bdf9-205162ce2b08', 'name': 'John'}])
    def content(self):
        return session.values()

    def find(self, id):
        try:
            return session[id]
        except KeyError:
            sys.stderr.write(f'Wrong item id: {id}')
            raise

    def save(self, item):
        item['id'] = str(uuid.uuid4())
        session[item['id']] = item
