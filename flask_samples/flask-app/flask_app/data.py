import random
import sys
import uuid
from faker import Faker
from flask import session


SEED = 1234


def generate_companies_old(companies_count):
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


class Repository:
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
