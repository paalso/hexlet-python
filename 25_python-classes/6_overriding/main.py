# https://ru.hexlet.io/courses/python-classes/lessons/overriding/exercise_unit
# https://ru.hexlet.io/code_reviews/1211554

# Python: Погружаясь в классы
# 7. Переопределение методов

# Реализуйте класс SmartFileInfo, наследующийся от FileInfo...

from SmartFileInfo import SmartFileInfo


def main():
    file_stat = SmartFileInfo('Makefile')
    print(file_stat.get_size())  # 67
    print(file_stat.get_size('b'))  # 67
    print(file_stat.get_size('kb'))  # 0.0654296875
    print(file_stat.get_size('udav'))  # ValueError


if __name__ == '__main__':
    main()
