# https://ru.hexlet.io/courses/python-functions/lessons/high-order-functions/exercise_unit
# https://ru.hexlet.io/code_reviews/272106
# Функции высшего порядка

# реализовать пару функций:
# Функцию-ключ get_first_name(), которая получает имя пользователя из
# строки вида "Имя_Фамилия"
# Функцию сортировки sort_by(), которая принимает функцию-ключ и список и
# сортирует список по этому ключу. Функция не должна изменять оригинальный список.



def get_first_name(name):
    return name.split('_')[0]


def sort_by(key_func, items):
    return sorted(items, key=lambda e: key_func(e))


users = ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]
sort_by(get_first_name, users)  # ["Boba_Fett", "Luke_Skywalker", "Vader_Darth"]
sorted_users = sort_by(get_first_name, users)
print(sorted_users)
print(users)    # => ["Vader_Darth", "Luke_Skywalker", "Boba_Fett"]

