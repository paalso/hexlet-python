# https://ru.hexlet.io/courses/python-declarative-programming/lessons/list-comprehensions/exercise_unit
# https://ru.hexlet.io/code_reviews/435789

# Генераторы списков
# ================================================

# написать функцию non_empty_truths(). Она должна вычислять копию входного
# списка списков с помощью генераторов списков. При этом копия должна быть
# очищена от всего лишнего:

# От ложных элементов — не только False, а любых ложных
# От пустых списков — они могу появиться сами по себе или получаться после
# отбрасывания всех элементов из них


def non_empty_truths(list_of_lists):
    return [L for L in
            [[e for e in list_ if e] for list_ in list_of_lists] if L]


assert non_empty_truths([]) == []
assert non_empty_truths([[], []]) == []
assert non_empty_truths([[0]]) == []
assert non_empty_truths([[0, ""], [False, None]]) == []
assert non_empty_truths([[0, 1, 2], [], [], [False, True, 42]]) == \
    [[1, 2], [True, 42]]
