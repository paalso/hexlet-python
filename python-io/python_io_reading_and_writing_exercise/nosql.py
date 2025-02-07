#!/usr/bin/env python3

# https://ru.hexlet.io/challenges/python_io_reading_and_writing_exercise/instance
# https://ru.hexlet.io/code_reviews/1082307

KEY_LEN = 10
VALUE_LEN = 20


def get_(path, key):
    with open(path, 'r') as f:
        for line in f:
            current_key = line[:KEY_LEN].rstrip()
            if current_key == key:
                value = line[KEY_LEN:].rstrip()
                return value


def set_(path, key, value):
    current_value = get_(path, key)

    if current_value == value:
        return

    key_value_line = f'{key.ljust(KEY_LEN)}{value}\n'

    if current_value is None:
        with open(path, 'a') as f:
            f.write(key_value_line)
        return

    with open(path, 'r') as f:
        result_lines = []
        for line in f:
            current_key = line[:KEY_LEN].rstrip()
            if current_key == key:
                line = f'{line[:KEY_LEN]}{value}\n'
            result_lines.append(line)

    with open(path, 'w') as f:
        f.writelines(result_lines)


def main():
    path = './nosql.db'
    set_(path, 'key2', '$$$$$$  $$$')


if __name__ == '__main__':
    main()
