# https://ru.hexlet.io/courses/python-oop-basics/lessons/properties/exercise_unit
# https://ru.hexlet.io/code_reviews/355194


# Python: Введение в ООП -> Свойства
# -----------------------------------

# Реализуйте класс HourClock, который будет изображать часы с одной лишь
# часовой стрелкой. Текущее время (час) должно сообщать свойство hours.
# Это же свойство должно позволять изменять положение часовой стрелки
# (посредством сеттера). При изменении положения стрелки нужно
# контролировать, чтобы значение оставалось в диапазоне 0..11 (часов).


class HourClock:
    def __init__(self, hours=0):
        self.hours_passed = hours

    @property
    def hours(self):
        return self.hours_passed % 12

    @hours.setter
    def hours(self, new):
        self.hours_passed = new


def test_clock():
    clock = HourClock()
    assert clock.hours == 0
    clock.hours += 6
    clock.hours += 5
    assert clock.hours == 11
    clock.hours += 4
    assert clock.hours == 3
    clock.hours -= 4
    assert clock.hours == 11
    clock.hours = 123
    assert clock.hours == 3


test_clock()


# BEGIN
# class HourClock:
#     def __init__(self):
#         """Create a new hour clock."""
#         self.hand_position = 0

#     @property
#     def hours(self):
#         return self.hand_position

#     @hours.setter
#     def hours(self, new_position):
#         self.hand_position = new_position % 12
# END