# https://ru.hexlet.io/courses/python-basics/lessons/default-parameters/exercise_unit

# Основы Python → Необязательные параметры функций
# =================================================

# Реализуйте функцию get_hidden_card(), которая:
# - Принимает на вход номер кредитки (состоящий из 16 цифр) в виде строки
# - Возвращает его скрытую версию, которую можно использовать на сайте для
# отображения Если исходная карта имела номер 2034399002125581, то скрытая
# версия выглядит так ****5581.


def get_hidden_card(card_number, asterisks_to_leave=4):
    return f'{"*" * asterisks_to_leave}{card_number[-4:]}'


assert get_hidden_card('2034399002121100', 1) == '*1100'  # *1100
assert get_hidden_card('1234567812345678', 2) == '**5678'  # **5678
assert get_hidden_card('1234567812345678', 3) == '***5678'  # ***5678
assert get_hidden_card('1234567812345678') == '****5678'  # ****5678
