# https://ru.hexlet.io/challenges/python_lists_enlarge_image_exercise
# https://ru.hexlet.io/code_reviews/207258

# Python: Увеличение двумерного списка
# =====================================

# Реализуйте функцию enlarge, которая принимает изображение в виде двумерного
# списка строк и увеличивает его в два раза, то есть удваивает каждый символ по
# горизонтали и вертикали.

def print_img(img):
    [print(s) for s in img]


def enlarge(image):
    def enlarge_string(s):
        return "".join([2*e for e in s])

    result = []
    [result.extend([enlarge_string(e), enlarge_string(e)]) for e in image]
    return result


frame = [
    '****',
    '*  *',
    '*  *',
    '****'
    ]

# ********
# ********
# **    **
# **    **
# **    **
# **    **
# ********
# ********
print_img(enlarge(frame))

glider = [
    ' * ',
    '  *',
    '***'
    ]

print()
print_img(enlarge(glider))
#   **
#   **
#     **
#     **
# ******
# ******
