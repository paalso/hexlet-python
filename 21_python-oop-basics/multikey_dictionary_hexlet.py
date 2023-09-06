class MultiKeyDict(object):
    """Словареподобный контейнер, позволяющий иметь псевдонимы ключей."""

    def __init__(self, **kwargs):
        """
        Инициализирует контейнер.

        Arguments:
            kwargs — пары "ключ-значение", которые будет содержать
            контейнер сразу после инициализации.
        """
        self._sequence = 0  # счётчик, используемый для промежуточных ключей
        self._keys = {}     # отображение внешних ключей во внутренние
        self._values = {}   # отображение внутренних ключей в значения
        for key, val in kwargs.items():
            self[key] = val

    def __getitem__(self, key):
        """
        Возвращает значение по ключу.

        Arguments:
        - key — один из ключей, связанных со значением.
        """
        return self._values[self._keys[key]]

    def __setitem__(self, key, value):
        """
        Сохраняет значение по указанному ключу.

        Изменение затрагивает все псевдонимы ключа. Любой из псевдонимов
        может быть указан в роли ключа.

        Arguments:
            key — ключ, по которому будет сохранено значение,
            value — сохраняемое по указанному ключу значение.
        """
        if key in self._keys:
            self._values[self._keys[key]] = value
            return

        self._sequence += 1
        self._keys[key] = self._sequence
        self._values[self._sequence] = value

    def alias(self, **kwargs):
        """
        Добавляет псевдоним(ы) для существующих ключей.

        Arguments:
            kwargs — пары "новый ключ - старый ключ". Все "старые ключи"
            должны уже присутствовать в контейнере.
        """
        for alias, key in kwargs.items():
            if alias in self._keys and not self.__find_aliases(alias):
                self._values.pop(self._keys[alias])
            self._keys[alias] = self._keys[key]

    def print_inner_structure(self):
        print(f'_keys:   {self._keys}')
        print(f'_values: {self._values}')
        print()

    def __find_aliases(self, key):
        value = self._keys[key]
        return [k for k, v in self._keys.items() if v == value and k != key]


def print_aliases(mkd, alias):
    print(f'aliases of {alias}: {mkd.find_aliases(alias)}')


mkd = MultiKeyDict(a=1, b='foo', c=3.14)
mkd.alias(a1='a', b1='b')
mkd.alias(aa1='a1', b1='b')
mkd.alias(aaa1='aa1', bb1='b')

print(f"a: {mkd['a']}")
print(f"a1: {mkd['a1']}")
print(f"aa1: {mkd['aa1']}")
print(f"aaa1: {mkd['aaa1']}")
print(f"c: {mkd['c']}")

mkd.print_inner_structure()
mkd.alias(a='c')

try:
    print(f"a: {mkd['a']}")
except KeyError:
    print(f"No key {'a'}")

print(f"a1: {mkd['a1']}")
print(f"aa1: {mkd['aa1']}")
print(f"aaa1: {mkd['aaa1']}")
print(f"c: {mkd['c']}")

mkd.print_inner_structure()
