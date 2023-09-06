# https://ru.hexlet.io/challenges/python_oop_basics_binary_tree_build_exercise/instance
# https://ru.hexlet.io/code_reviews/357429

# Python: Введение в ООП
# Испытание: Агрегация в двоичном дереве

"""
Реализуйте следующие методы в классе Node:
    __len__() — возвращает количество узлов в дереве (используется в len()).
    __repr__() — возвращает строковое представление дерева.
    total() — возвращает сумму всех ключей дерева.
    minimum() — возвращает минимальный ключ дерева.
    maximum() — возвращает максимальный ключ дерева.
    to_list() — возвращает плоский список, содержащий все ключи.
    every(fn) — проверяет, удовлетворяют ли все ключи дерева условию,
    заданному в передаваемой функции.
    some(fn) — проверяет, удовлетворяет ли какой-либо ключ дерева условию,
    заданному в передаваемой функции.

При обходе дерева нужно использовать порядок слева-направо.То есть вначале
обрабатываем ключ узла, затем ключ левого ребёнка, после чего ключ правого ребёнка.
"""


class Node:
    def __init__(self, key, left=None, right=None):
        """Create a new tree node."""
        self.key = key
        self.left = left
        self.right = right

    def __len__(self):
        return len(self.to_list())

    def __repr__(self):
        left_repr = repr(self.left) if self.left else 'None'
        right_repr = repr(self.right) if self.right else 'None'
        class_name = self.__class__.__name__
        return f'{class_name}({self.key}, {left_repr}, {right_repr})'

    def to_list(self):
        left_sublist = self.left.to_list() if self.left else []
        right_sublist = self.right.to_list() if self.right else []
        return [self.key, *left_sublist, *right_sublist]

    def total(self):
        return sum(self.to_list())

    def minimum(self):
        return min(self.to_list())

    def maximum(self):
        return max(self.to_list())

    def every(self, fn):
        return all(map(fn, self.to_list()))

    def some(self, fn):
        return any(map(fn, self.to_list()))


tree = Node(
    9,
    Node(
        4,
        Node(8),
        Node(
            6,
            Node(3),
            Node(7),
        ),
    ),
    Node(
        17,
        right=Node(
            22,
            Node(20),
        ),
    ),
)


class N(Node):
    pass


tree2 = Node(3, Node(1), Node(2))
print(tree2)


tree3 = N(3, N(1), N(2))
print(tree3)


'''
# Hexlet's solution
# ------------------

class Node:
    def __init__(self, key, left=None, right=None):
        """Create a new tree node."""
        self.key = key
        self.left = left
        self.right = right

    def fold(self, combine, make):
        result = make(self.key)
        if self.left is not None:
            result = combine(
                result,
                self.left.fold(combine, make),
            )
        if self.right is not None:
            result = combine(
                result,
                self.right.fold(combine, make),
            )
        return result

    def __len__(self):
        """Return a total count of tree nodes."""
        return self.fold(operator.add, lambda _: 1)

    def total(self):
        return self.fold(operator.add, lambda x: x)

    def to_list(self):
        return self.fold(operator.add, lambda x: [x])

    def some(self, pred):
        return self.fold(operator.or_, pred)

    def every(self, pred):
        return self.fold(operator.and_, pred)

    def minimum(self):
        return self.fold(min, lambda x: x)

    def maximum(self):
        return self.fold(max, lambda x: x)

    def __repr__(self):
        """Return text representation of the tree."""
        return '{cls}({key}, {left}, {right})'.format(
            cls=self.__class__.__name__,
            key=self.key,
            left=repr(self.left),
            right=repr(self.right),
        )
'''
