# https://ru.hexlet.io/challenges/python_oop_basics_binary_tree_build_exercise/instance

# Python: Введение в ООП
# Испытание: Построение двоичного дерева

"""
Реализуйте класс, который представляет собой узел дерева.

Класс должен содержать:

    Атрибут key — ключ узла.
    Атрибуты left и right — ссылки на левого и правого ребёнка соответственно.
    Если ребёнок в узле отсутствует, геттер возвращает None.
    Метод insert(key) — выполняет добавление узла, формируя правильное
    воичное дерево.
"""


def test_empty_node():
    tree = Node()
    assert tree.key is None
    assert tree.left is None
    assert tree.right is None


def test_node():
    tree = Node()
    tree.insert(9)
    tree.insert(17)
    tree.insert(4)
    tree.insert(3)
    tree.insert(6)
    tree.insert(22)
    tree.insert(5)
    tree.insert(7)
    tree.insert(20)
    tree.insert(4)
    tree.insert(3)

    assert tree.key == 9

    assert tree.left.key == 4

    assert tree.left.left.key == 3
    assert tree.left.left.left is None
    assert tree.left.left.right is None

    assert tree.left.right.key == 6

    assert tree.left.right.left.key == 5
    assert tree.left.right.left.left is None
    assert tree.left.right.left.right is None

    assert tree.left.right.right.key == 7
    assert tree.left.right.right.left is None
    assert tree.left.right.right.right is None

    assert tree.right.key == 17
    assert tree.right.left is None

    assert tree.right.right.key == 22
    assert tree.right.right.right is None

    assert tree.right.right.left.key == 20
    assert tree.right.right.left.left is None
    assert tree.right.right.left.right is None


def test_liskov_substitution():

    tree = NewNode()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)

    assert isinstance(tree.left, NewNode), "Sibling should be NewNode too"
    assert isinstance(tree.right, NewNode), "Sibling should be NewNode too"


class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node: {self.key}'

    def insert(self, key):
        if not self.key:
            self.key = key

        if key < self.key:
            if not self.left:
                self.left = self.__class__(key)
            else:
                self.left.insert(key)

        if key > self.key:
            if not self.right:
                self.right = self.__class__(key)
            else:
                self.right.insert(key)


class NewNode(Node):
    """A simple subclass of Node."""


test_empty_node()
test_node()
test_liskov_substitution()
