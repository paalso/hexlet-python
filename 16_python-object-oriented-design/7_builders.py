# https://ru.hexlet.io/courses/python-object-oriented-design/lessons/builder/exercise_unit
# https://ru.hexlet.io/code_reviews/1137615

# Python: Объектно-ориентированный дизайн
# 7. Builders

'''
Реализуйте класс Booking, который позволяет бронировать номер отеля на определённые даты. Метод класса book() принимает на вход две даты в текстовом формате. Если бронирование возможно, то метод возвращает True и выполняет бронирование (даты записываются во внутреннее состояние объекта).
'''

from datetime import date, timedelta


class Booking:
    def __init__(self) -> None:
        self.booked_day_intervals = []

    def book(self, begin_date: str, end_date: str) -> bool:
        begin_date = date.fromisoformat(begin_date)
        end_date = date.fromisoformat(end_date)
        new_booking_date_interval = (begin_date, end_date)

        if self.__validate_booking(new_booking_date_interval):
            self.booked_day_intervals.append(new_booking_date_interval)
            return True

        return False

    def __validate_booking(self, new_date_interval):
        if self.__date_interval_length(new_date_interval) <= timedelta(0):
            return False

        for date_interval in self.booked_day_intervals:
            if self.__date_intervals_intersects(
                    date_interval, new_date_interval):
                return False

        return True

    def __date_intervals_intersects(self, interval1, interval2):
        begin_date1, end_date1 = interval1
        begin_date2, end_date2 = interval2

        return max(begin_date1, begin_date2) < min(end_date1, end_date2)

    def __date_interval_length(self, date_interval):
        begin_date, end_date = date_interval
        return end_date - begin_date


def test_booking():
    booking = Booking()

    assert not booking.book('2008-11-10', '2008-11-05')
    assert booking.book('2008-11-11', '2008-11-13')
    assert not booking.book('2008-11-12', '2008-11-12')
    assert not booking.book('2008-11-12', '2008-11-14')
    assert booking.book('2008-11-10', '2008-11-11')
    assert not booking.book('2008-11-12', '2008-11-13')
    assert not booking.book('2008-11-13', '2008-11-13')
    assert booking.book('2008-11-13', '2008-11-14')
    assert booking.book('2008-05-08', '2008-05-18')
    assert not booking.book('2008-05-09', '2008-05-10')


test_booking()

# booking = Booking()

# # забронировать номер на два дня
# assert booking.book('2008-11-10', '2008-11-12')

# # бронь невозможна, 11-го числа номер будет занят
# assert not booking.book('2008-11-11', '2008-11-15')

# # бронь возможна, потому что 12-го числа номер освободится
# assert booking.book('2008-11-12', '2008-11-13')

# # бронь невозможна, съём, сроком менее одного дня, обычно не практикуется
# assert not booking.book('2008-11-17', '2008-11-17')

# # бронь возможна, съём номера на один день
# assert booking.book('2008-11-17', '2008-11-18')
