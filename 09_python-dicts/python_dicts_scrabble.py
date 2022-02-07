# https://ru.hexlet.io/challenges/python_dicts_scrabble
# https://ru.hexlet.io/code_reviews/248488

# Python: Скрэббл
# ================

# Реализуйте функцию-предикат scrabble, которая принимает на вход два параметра:
# набор символов (строку) и слово, и проверяет, можно ли из переданного набора
# составить это слово. В результате вызова функция возвращает True или False.
# При проверке учитывается количество символов, которые нужны для составления
# слова, и не учитывается их регистр.


def scrabble(symbols_string, word):
    import collections
    string_counter = collections.Counter(symbols_string.lower())
    for c, qty in collections.Counter(word.lower()).items():
        if string_counter.get(c, 0) < qty:
            return False
    return True


assert scrabble('rkqodlw', 'world') == True
assert scrabble('avj', 'java') == False
assert scrabble('avjafff', 'java') == True
assert scrabble('', 'Hexlet') == False
assert scrabble('scriptingjava', 'JavaScript') == True

# Можно было сделать ещё короче, если учесть то,
# как работает вычитание для пары Counter!
# Хватило бы: return not (Counter(word.lower()) - Counter(string.lower()))
