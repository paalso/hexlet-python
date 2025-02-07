# https://ru.hexlet.io/challenges/python_lists_compare_versions_exercise
# https://ru.hexlet.io/code_reviews/210099

# Python: Сравнение версий
# =========================

# Реализуйте функцию compare_version, которая сравнивает переданные версии
# version1 и version2. Если version1 > version2, то функция должна вернуть 1,
# если version1 < version2, то -1, если же version1 = version2 — 0.
#
# Версия — это строка, в которой два числа (мажорная и минорные версии)
# разделены точкой, например: 12.11. Важно понимать, что версия — это не число
# с плавающей точкой, а несколько чисел не связанных между собой. Проверка на
# больше/меньше производится сравнением каждого числа независимо. Поэтому
# версия 0.12 больше версии 0.2.
# Пример порядка версий: 0.1 < 1.1 < 1.2 < 1.11 < 13.37

def compare_version(ver1, ver2):

    def splitter(version):
        left, right = version.split(".")
        return (int(left), int(right))

    if splitter(ver1) < splitter(ver2):
        return -1
    if splitter(ver1) > splitter(ver2):
        return 1
    return 0


assert compare_version("0.1", "0.2") == -1
assert compare_version("0.2", "0.1") == 1
assert compare_version("4.2", "4.2") == 0
assert compare_version('0.2', '0.12') == -1


"""
def compare_version(ver1, ver2):

    def sgn(x):
        if x == 0: return 0
        return 1 if x > 0 else -1

    v11, v12 = tuple(map(int, ver1.split('.')))
    v21, v22 = tuple(map(int, ver2.split('.')))
    if v11 - v21:
        return sgn(v11 - v21)

    if v12 - v22:
        return sgn(v12 - v22)
    return 0
"""
