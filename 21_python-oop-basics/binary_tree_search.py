# https://ru.hexlet.io/challenges/python_oop_basics_multikey_dictionary_exercise/instance
# https://ru.hexlet.io/code_reviews/355613

# Python: Введение в ООП
# Испытание: Поиск в двоичном дереве

"""
Двоичное дерево поиска состоит из узлов, каждый из которых содержит
значение ключа и два поддерева (левое и правое), которые в свою очередь
также являются двоичными деревьями. Правильное дерево не содержит
повторяющихся ключей, и для каждого узла гарантируется, что в левом
поддереве все значения меньше текущего, а в правом — больше.

Реализуйте класс, который реализует представление узла. При инициализации
объекта класс принимает на вход три параметра:

    key — значение ключа (число),
    left — левое поддерево (тоже узел, по умолчанию None),
    right — правое поддерево (по умолчанию None).

Каждый экземпляр класса должен содержать атрибуты:

    key
    left
    right

Также класс должен реализовывать метод search(key), который выполняет поиск
узла в правильно построенном двоичном дереве по ключу и возвращает узел.
Если узел не найден, возвращается None.
"""


class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str(self):
        print(f'Node: {self.key}')

    def search(self, key):
        if key == self.key:
            return self

        if key < self.key and self.left:
            return self.left.search(key)

        if key > self.key and self.right:
            return self.right.search(key)


node5 = Node(5)
node22 = Node(22, left=Node(20))
tree = Node(
    9,
    Node(
        4,
        Node(3),
        Node(
            6,
            node5,
            Node(7),
        ),
    ),
    Node(
        17,
        right=node22,
    ),
)

print(tree.search(6).key)  # 6
print(tree.search(6).left.key)  # 5
print(tree.search(6).right.key)  # 7
print(tree.search(5) is node5)  # True
print(tree.left.left.key)  # 3
print(tree.search(100))
