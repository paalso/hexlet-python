class MultiKeyDict(object):
    """Словареподобный контейнер, позволяющий иметь псевдонимы ключей."""

    def __init__(self, **kwargs):
        """
        Инициализирует контейнер.

        Arguments:
            kwargs — пары "ключ-значение", которые будет содержать
            контейнер сразу после инициализации.

        """
        # BEGIN
        self._sequence  # счётчик, используемый для промежуточных ключей
        self._keys  # отображение внешних ключей во внутренние
        self._values  # отображение внутренних ключей в значения
        # END

    def __getitem__(self, key):
        """
        Возвращает значение по ключу.

        Arguments:
        - key — один из ключей, связанных со значением.

        """

    def __setitem__(self, key, value):
        """
        Сохраняет значение по указанному ключу.

        Изменение затрагивает все псевдонимы ключа. Любой из псевдонимов
        может быть указан в роли ключа.

        Arguments:
            key — ключ, по которому будет сохранено значение,
            value — сохраняемое по указанному ключу значение.

        """

    def alias(self, **kwargs):
        """
        Добавляет псевдоним(ы) для существующих ключей.

        Arguments:
            kwargs — пары "новый ключ - старый ключ". Все "старые ключи"
            должны уже присутствовать в контейнере.

        """
        # BEGIN



mkd = MultiKeyDict(a=1, b='foo', c=3.14)
print()
print(f'_keys:   {mkd._keys}')
print(f'_values: {mkd._values}')

mkd.alias(a1='a', b1='b')

print()
print(f'_keys:   {mkd._keys}')
print(f'_values: {mkd._values}')

mkd['a1'] = 19
print()
print(f'_keys:   {mkd._keys}')
print(f'_values: {mkd._values}')
# mkd.alias(aa1='a1', b1='b')
# mkd.alias(aaa1='aa1', bb1='b')

# print(f"a: {mkd['a']}")
# print(f"a1: {mkd['a1']}")
# print(f"aa1: {mkd['aa1']}")
# print(f"aaa1: {mkd['aaa1']}")

# mkd.alias(a='c')

# try:
#     print(f"a: {mkd['a']}")
# except KeyError:
#     print(f"No key {'a'}")
# print(f"a1: {mkd['a1']}")
# print(f"aa1: {mkd['aa1']}")
# print(f"aaa1: {mkd['aaa1']}")

# print(f'_keys:   {mkd._keys}')
# print(f'_values: {mkd._values}')
