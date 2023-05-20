# https://ru.hexlet.io/challenges/python_basics_encrypt_exercise/instance

# Основы Python. Испытание → Шифрование
# ======================================

# написать программу, которая шифрует сообщения по следующему алгоритму: она
# берёт текст и переставляет в нем каждые два подряд идущих символа.


def encrypt(text):
    result = []
    is_odd_length = False
    if (size := len(text)) % 2 == 1:
        size -= 1
        is_odd_length = True

    for i in range(0, size, 2):
        result.extend([text[i + 1], text[i]])
    if is_odd_length:
        result.append(text[size])

    return ''.join(result)


assert encrypt("move") == 'omev'
assert encrypt("attack") == 'taatkc'
assert encrypt("go!") == 'og!'


# def encrypt(word):
#     result = ''
#     i = 0
#     while i < len(word):
#         result += word[i:i + 2][::-1]
#         i += 2
#     return result