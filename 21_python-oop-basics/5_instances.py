# https://ru.hexlet.io/courses/python-oop-basics/lessons/instances/theory_unit

# Python: Введение в ООП -> Инстанцирование классов
# --------------------------------------------------

# Цель упражнения состоит в реализации цветовой модели RGB в виде класса с
# именем RGB. Класс должен объявлять три атрибута: red, green и blue, имеющие
# по умолчанию значение 0. Также вам нужно будет объявить в модуле переменные
# red, green и blue, ссылающиеся каждая на свой экземпляр класса RGB. При этом
# у объекта в red атрибут red должен быть равен 255. Атрибуты blue и green
# делаются аналогично.


class RGB:
    red = 0
    green = 0
    blue = 0


def rgb2tuple(rgb):
    if isinstance(rgb, RGB):
        return rgb.red, rgb.green, rgb.blue


red = RGB()
red.red = 255

green = RGB()
green.green = 255

blue = RGB()
blue.blue = 255


assert rgb2tuple(red) == (255, 0, 0)
assert rgb2tuple(green) == (0, 255, 0)
assert rgb2tuple(blue) == (0, 0, 255)
