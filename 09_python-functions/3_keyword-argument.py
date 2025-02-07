# https://ru.hexlet.io/courses/python-functions/lessons/keyword-arguments/exercise_unit
# Python: Словари и Множества → Именованные аргументы

# Используя функцию rgb, реализовать функцию get_colors, которая должна вернуть
# словарь цветов (о цветовой модели RGB вы можете почитать тут). В словаре
# должны присутствовать ключи 'red', 'green', 'blue'. Каждому ключу должен
# соответствовать результат вызова функции rgb со значением 255 для
# соответствующего ключу аргумента. Для построения каждого цвета используйте
# только один аргумент!


def rgb(red=0, green=0, blue=0):
    return 'rgb({}, {}, {})'.format(red, green, blue)


def get_colors():
    return {
        'red': rgb(red=255),
        'green': rgb(green=255),
        'blue': rgb(blue=255),
    }


colors = get_colors()
set(colors.keys()) == {'red', 'green', 'blue'}   # True
print(colors['red'])   # 'rgb(255, 0, 0)'
print(colors['blue'])  # 'rgb(0, 0, 255)'


