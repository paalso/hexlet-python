from flask import session
import json
import os
import sys
import uuid


class Repository:
    def content(self):
        return session.values()

    def find(self, id):
        for session_id, item in session.items():
            if item['id'] == id:
                return item

        sys.stderr.write(f'Wrong item id: {id}')
        raise KeyError

    def save(self, item):
        session_id = str(uuid.uuid4())
        session[session_id] = item


class UserRepository:
    def __init__(self, path):
        self.path = path
        self.id = 0
        if not os.path.exists(self.path):
            self.id = 0
            with open(self.path, 'w') as file:
                json.dump([], file)
        else:
            data = self._load_data()
            self.id = max(user['id'] for user in data)

    def save(self, user):
        data = self._load_data()
        self.id += 1
        numerized_user = user | {'id': self.id}
        data.append(numerized_user)
        self._save_data(data)

    def find_by_id(self, id_):
        result = self.find('id', id_)
        if result:
            return result[0]

    def find(self, key, value):
        data = self._load_data()
        return [user for user in data if user[key] == value]

    def get_all(self):
        return self._load_data()

    def _load_data(self):
        with open(self.path, 'r') as file:
            return json.load(file)

    def _save_data(self, data):
        with open(self.path, 'w') as file:
            json.dump(data, file, indent=4)
