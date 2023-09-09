# https://ru.hexlet.io/courses/python-object-oriented-design/lessons/builder/exercise_unit


# Python: Объектно-ориентированный дизайн
# 7. Builders

'''
Реализуйте класс Booking, который позволяет бронировать номер отеля на определённые даты. Метод класса book() принимает на вход две даты в текстовом формате. Если бронирование возможно, то метод возвращает True и выполняет бронирование (даты записываются во внутреннее состояние объекта).
'''

from datetime import date


class Booking:
    def __init__(self) -> None:
        self.begin_date = None
        self.end_date = None

    def book(self, new_begin_date: str, new_end_date: str) -> bool:
        new_begin_date = date(*map(int, new_begin_date.split('-')))
        new_end_date = date(*map(int, new_end_date.split('-')))
        if self.validate(self.begin_date, self.end_date, new_begin_date, new_end_date):
            self.begin_date, self.end_date = new_begin_date, new_end_date
            return True
        return False

    def validate(begin_date, end_date, new_begin_date, new_end_date):
        if not begin_date:
            return True
        min_date = min(begin_date, end_date, new_begin_date, new_end_date)
        max_date = max(begin_date, end_date, new_begin_date, new_end_date)
        return max_date - min_date > end_date - begin_date + new_end_date - new_begin_date


booking = Booking()

# забронировать номер на два дня
assert booking.book('2008-11-10', '2008-11-12')

# бронь невозможна, 11-го числа номер будет занят
assert not booking.book('2008-11-11', '2008-11-15')

# бронь возможна, потому что 12-го числа номер освободится
assert booking.book('2008-11-12', '2008-11-13')

# бронь невозможна, съём, сроком менее одного дня, обычно не практикуется
assert not booking.book('2008-11-17', '2008-11-17')

# бронь возможна, съём номера на один день
assert booking.book('2008-11-17', '2008-11-18')
