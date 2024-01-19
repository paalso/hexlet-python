#!/usr/bin/env python3

# https://ru.hexlet.io/courses/basic-algorithms
# https://ru.hexlet.io/courses/basic-algorithms/lessons/binary-search/exercise_unit
# https://ru.hexlet.io/code_reviews/1270083

# Основы алгоритмов и структур данных 
# 2 Бинарный поиск 

'''
Функция принимает два параметра phoneBook и name. Первый - это телефонная
книга, а второй — имя, которое нужно найти.
Если имени нет в телефонной книге, то функция должна вернуть строку
Name not found!, а если телефонная книга пуста, то Phonebook is empty!.
Экспортируйте функцию по умолчанию.
'''


 


def binary_search_classical(collection, item, comparator):
    first_id = 0
    last_id = len(collection) - 1
    while first_id <= last_id:
        middle_id = (first_id + last_id) // 2
        if comparator(item, collection[middle_id]) == 0:
            return middle_id
        if comparator(item, collection[middle_id]) < 0:
            last_id = middle_id - 1
        else:
            first_id = middle_id + 1
    return -1


def comparator(item, entry):
    if item == entry['name']:
        return 0
    if item < entry['name']:
        return -1
    return 1


def solution(data, item):
    if len(data) == 0:
        return 'Phonebook is empty!'
    
    index = binary_search(data, item, comparator)
    
    if index < 0:
        return 'Name not found!'

    return data[index]['number']


def main():
    phonebook = [
        {'name': 'Alex Bowman', 'number': '48-2002'},
        {'name': 'Aric Almirola', 'number': '10-1001'},
        {'name': 'Bubba Wallace', 'number': '23-1111'},
    ]

    assert solution(phonebook, 'Alex Bowman') == '48-2002'
    assert solution(phonebook, 'Bubba Wallace') == '23-1111' 
    assert solution(phonebook, 'None') == 'Name not found!'
    assert solution([], 'Alex Bowman') == 'Phonebook is empty!'


if __name__ == '__main__':
    main()
