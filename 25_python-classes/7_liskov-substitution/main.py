# https://ru.hexlet.io/courses/python-classes/lessons/liskov-substitution/exercise_unit

# Python: Погружаясь в классы
# 7. Прицип подстановки Лисков

'''
В этом задании вам придется написать код, который нарушает принцип Лисков.
Запомните его и никогда так больше не делайте :D Представьте себе библиотеку,
которая предоставляет абстракции для работы с хранилищами ключ-значение. Все
они предоставляют интерфейс из трех методов:

    set(key, value) – устанавливает значение
    get(key) – возвращает значение
    count() – возвращает количество ключей в хранилище

В директории src три таких хранилища: Redis, InMemory, GoogleStorage. Первые
два умеют возвращать число ключей внутри них, а последнее – нет. Для простоты
реализации, каждое хранилище складывает значения во внутренний объект.
В реальности, они бы выполняли запросы по сети, но для текущего задания это
ненужное усложнение.
GoogleStorage.py

Реализуйте интерфейс хранилища в классе GoogleStorage. Так как GoogleStorage
не поддерживает подсчет количества элементов, то сделайте так, чтобы этот
метод кидал исключение Exception, если его вызывают.
'''

def main():
    pass


if __name__ == '__main__':
    main()