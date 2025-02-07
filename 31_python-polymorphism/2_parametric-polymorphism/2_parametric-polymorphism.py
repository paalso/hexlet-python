# https://ru.hexlet.io/courses/python-polymorphism/lessons/parametric-polymorphism/theory_unit
# https://ru.hexlet.io/code_reviews/1138479

# Python: Полиморфизм
# 2. Параметрический полиморфизм 

'''
Реализуйте функцию reverse(), которая принимает на вход
односвязный список и переворачивает его.
'''

from node import Node


# Version 1
def assemble(values):
    if not values:
        return
    head, *rest = values
    return Node(head, assemble(rest))


def get_values(list_):
    if not list_:
        return []
    head, tail = list_, list_.get_next()
    return [head.get_value(), *get_values(tail)]


def reverse(list_):
    return assemble(reversed(get_values(list_)))


'''
# Version 2
def get_last(list_):
    next_ = list_.get_next()
    if next_ is None:
        return list_
    return get_last(next_)


def reverse(list_):
    head, tail = list_, list_.get_next()
    if tail is None:
        return head
    reversed_tail = reverse(tail)
    last = get_last(reversed_tail)
    last.next = Node(head.get_value())
    return reversed_tail
'''

'''
# Version 3
def reverse(list_):
    node = list_
    reversed = Node(node.get_value())
    while node.get_next():
        node = node.get_next()
        reversed = Node(node.get_value(), reversed)
    return reversed
'''

numbers = Node(1)                    # (1,)
numbers = Node(1, Node(2, Node(3, Node(4))))  # (1, 2, 3, 4)
print(f'Original: {numbers}')
print(f'Reversed: {reverse(numbers)}')
