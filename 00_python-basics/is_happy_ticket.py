# https://ru.hexlet.io/challenges/python_basics_happy_ticket_exercise/instance

# Основы Python. Испытание → Счастливый билет
# ============================================

# Реализуйте функцию is_happy_ticket(), проверяющую является ли номер
# счастливым (номер — всегда строка). Функция должна возвращать True,
# если билет счастливый, или False, если нет.


def is_happy_ticket(number):
    half_size = len(number) // 2
    return sum(map(int, number[:half_size])) == sum(map(int, number[half_size:]))


assert is_happy_ticket('123123')
assert is_happy_ticket('341800')
assert not is_happy_ticket('42')
assert not is_happy_ticket('12345678')
