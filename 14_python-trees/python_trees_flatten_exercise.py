# https://ru.hexlet.io/challenges/python_trees_flatten_exercise
# https://ru.hexlet.io/code_reviews/348663

# Python: Выравнивание
# =====================

"""
Реализуйте функцию flatten(), которая делает плоским вложенный список.
"""

# Version № 1
def normalize_item(item):
    return flatten(item) if type(item) == list else [item]


def flatten(lists):
	return sum(map(normalize_item, lists), [])


print(flatten([1, 2, 3]))
print(flatten([2, [3, 5], [[4, 3], 2]]))

assert flatten([2, [3, 5], [[4, 3], 2]]) == [2, 3, 5, 4, 3, 2]


# Version № 2
def flatten(L):
    flattened = []
    for e in L:
        if isinstance(e, list):
            flattened.extend(flatten(e))
        else:
            flattened.append(e)
    return flattened
    
   
# Version № 3
def flatten2(lists):
    flattened = []

    def inner(node):
        for e in node:
            inner(e) if isinstance(e, list) else flattened.append(e)

    inner(lists)
    return flattened

