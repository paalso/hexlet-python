#!/usr/bin/env python3

# https://ru.hexlet.io/challenges/python_io_reading_and_writing_exercise/instance
# https://ru.hexlet.io/code_reviews/1082307

KEY_LEN = 10
VALUE_LEN = 20


def get_(path, key):
    db = open(path)
    key = _fill(key, KEY_LEN)
    search_positon = 0

    head = db.read(KEY_LEN)
    while head:
        if head == key:
            data = db.read(VALUE_LEN)
            return data.strip()
        search_positon += KEY_LEN + VALUE_LEN
        db.seek(search_positon)
        head = db.read(KEY_LEN)

    db.close()


def set_(path, key, value):
    db = open(path, 'r+')
    key = _fill(key, KEY_LEN)
    search_positon = 0

    head = db.read(KEY_LEN)
    while head:
        if head == key:
            current_pos = db.tell()
            db.seek(current_pos)
            db.write(_fill(value, VALUE_LEN))
            return
        search_positon += KEY_LEN + VALUE_LEN
        db.seek(search_positon)
        head = db.read(KEY_LEN)

    db.write(_fill(key, KEY_LEN))
    db.write(_fill(value, VALUE_LEN))
    db.close()


def _fill(name, size):
    return name[:size].ljust(size, ' ')


def main():
    path = './nosql.db'
    set_(path, 'key2', '+ + + ')


if __name__ == '__main__':
    main()
