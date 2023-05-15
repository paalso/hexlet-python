# https://ru.hexlet.io/courses/python-basics/lessons/type-annotations/exercise_unit

# Основы Python → Аннотации типов
# ================================

# Реализуйте функцию letter_multiply(). Она должна принимать три параметра:
#     Строку
#     Символ
#     Число, которое обозначает, сколько раз нужно повторить символ в слове


def letter_multiply(text: str, letter_to_repete: str, repetitions: int) -> str:
    result_symbols: list = (c * repetitions if c == letter_to_repete else c
                            for c in text)
    return "".join(result_symbols)


text = 'python'

assert letter_multiply(text, 'p', 2) == 'ppython'
assert letter_multiply(text, 'y', 3) == 'pyyython'
assert letter_multiply(text, 'n', 4) == 'pythonnnn'


# BEGIN
# def letter_multiply(text: str, letter: str, repetitions: int) -> str:
#     result: str = text.replace(letter, letter*repetitions)
#     return result
# END
