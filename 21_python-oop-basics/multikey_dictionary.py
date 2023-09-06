# https://ru.hexlet.io/challenges/python_oop_basics_multikey_dictionary_exercise/instance\
# https://ru.hexlet.io/code_reviews/1130510

# Python: Введение в ООП -> Исключения
# Испытание: Словарь с псевдонимами


'''
Рреализовать класс MultiKeyDict, который должен уметь работать по протоколу
__getitem__()/__setitem__().

Класс принимает именованные параметры, которые становятся первыми ключами
и значениями.
В этом класс максимально похож на dict. А вот метод alias() уже является
отличием: вызывая этот метод с параметрами "новыйключ='старыйключ'",
вы создаёте псевдонимы для существующих ключей.

Обращение по созданному псевдониму ничем не отличается от обращения по
оригинальному ключу, то есть с момента создания псевдонима у значения
становится два ключа (или больше, конечно же).

Важно, что с помощью метода alias() должно быть возможно "перекинуть"
старые ключи на новые значения без потери этих самых значений, если
останется хотя бы один псевдоним, всё ещё ссылающийся на значение.

    При перебрасывании последнего ключа, некие значения могут остаться
вообще без ключа. По условиям задачи вам не нужно производить чистку таких
значений, но вы можете попробовать реализовать и такую функциональность!
'''


def test_multikeydict_access():
    mkd = MultiKeyDict(a=1, b='foo')
    assert mkd['a'] == 1
    assert mkd['b'] == 'foo'

    mkd.alias(aa='a', bb='b')
    assert mkd['aa'] == 1
    assert mkd['bb'] == 'foo'


def test_multikeydict_assignment():
    mkd = MultiKeyDict(x=100, y=[10, 20])

    mkd.alias(z='x')
    mkd['z'] += 1
    assert mkd['x'] == 101

    mkd.alias(z='y')
    mkd['z'] += [30]
    assert mkd['y'] == [10, 20, 30]


class MultiKeyDict():
    def __init__(self, **kwargs):
        self.vault = kwargs
        self.aliases = {}

    def __getitem__(self, key):
        basic_key = self.__get_basic_key(key)
        return self.vault[basic_key]

    def __setitem__(self, key, value):
        basic_key = self.__get_basic_key(key)
        self.vault[basic_key] = value

    def alias(self, **kwargs):
        for new_key, existing_key in kwargs.items():
            basic_key = self.__get_basic_key(existing_key)
            if new_key in self.vault:
                self.__relink_basic_key(new_key)
            self.aliases[new_key] = basic_key

    def print_inner_structure(self):
        print(f'vault:   {self.vault}')
        print(f'aliases: {self.aliases}')
        print()

    def __get_basic_key(self, key):
        if key not in self.vault:
            key = self.aliases[key]
        return key

    def __relink_basic_key(self, basic_key):
        basic_key_aliases = self.__get_basic_key_aliases(basic_key)
        value = self.vault.pop(basic_key)
        if not basic_key_aliases:
            return
        first_aliase, *rest_aliases = basic_key_aliases
        self.vault[first_aliase] = value
        for alias in rest_aliases:
            self.aliases[alias] = first_aliase
        self.aliases.pop(first_aliase)

    def __get_basic_key_aliases(self, basic_key):
        return list(map(lambda pair: pair[0],
                        filter(lambda pair: pair[1] == basic_key,
                               self.aliases.items())))


test_multikeydict_access()
test_multikeydict_assignment()

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
