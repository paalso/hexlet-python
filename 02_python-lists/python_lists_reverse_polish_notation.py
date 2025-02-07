# https://ru.hexlet.io/challenges/python_lists_snail_exercise
# https://ru.hexlet.io/code_reviews/246115

# Python: Обратная польская запись
# =================================
# Реализовать функцию rpn_calc, которая принимает список, каждый элемент
# которого содержит число или знак операции (+, -, *, /). Функция должна вернуть
# результат вычисления по обратной польской записи.


def rpn_calc(opers):
    import operator
    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }
    stack = []
    for e in opers:
        if type(e) in (int, float):
            stack.append(e)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(operations[e](operand1, operand2))
    return stack[-1]


assert rpn_calc([1, 2, '+', 4, '*', 3, '+']) == 15
assert rpn_calc([7, 2, 3, '*', '-']) == 1
