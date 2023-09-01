# https://ru.hexlet.io/challenges/python_oop_basics_multikey_dictionary_exercise/instance\

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
            self.aliases[new_key] = existing_key

    def __get_basic_key(self, key):
        while key not in self.vault:
            key = self.aliases[key]
        return key


mkd = MultiKeyDict(a=1, b='foo', c=3)
mkd.alias(a1='a', b1='b')
mkd.alias(aa1='a1', b1='b')
mkd.alias(aaa1='aa1', b1='b')

mkd.alias(a='c', b1='b')

mkd['aaa1'] = 47

print(mkd['aaa1'])
print(mkd['aa1'])
print(mkd['a1'])
print(mkd['a'])
