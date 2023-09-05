# https://ru.hexlet.io/courses/python-object-oriented-design/lessons/configuration-setters/exercise_unit
# https://ru.hexlet.io/code_reviews/1133840

# Python: Объектно-ориентированный дизайн
# 2. Изменяемая конфигурация 

# Реализуйте класс Truncater с единственным методом truncate().
# В классе уже присутствует конфигурация по умолчанию:

# separator отвечает за символ(ы) добавляющиеся в конце, после обрезания
# строки, а length это длина до которой происходит сокращение. Если строка
# короче или равна этой опции, то никакого сокращения не происходит.
# Конфигурацию по умолчанию можно переопределить передав новую при
# инициализации (она мержится с тем что в классе), а также через передачу
# конфигурации вторым параметром в метод truncate(). Оба этих способа можно
# комбинировать.


class Truncater():
    OPTIONS = {
        'separator': '...',
        'length': 200,
    }

    def __init__(self, **options):
        self.options = Truncater.OPTIONS | options

    def truncate(self, text, **options):
        options = self.options | options
        length = options['length']
        if len(text) <= length:
            return text
        separator = options['separator']
        return f"{text[:length]}{separator}"


def test_truncate():
    truncater = Truncater()
    assert truncater.truncate('one two') == 'one two'
    assert truncater.truncate('one two', length=6) == 'one tw...'
    assert truncater.truncate('one two', separator='.') == 'one two'
    assert truncater.truncate('one two', length=3) == 'one...'

    truncater = Truncater(length=3)
    assert truncater.truncate('one two') == 'one...'
    assert truncater.truncate('one two', separator='!') == 'one!'
    assert truncater.truncate('one two') == 'one...'

    assert truncater.truncate('one two', length=7) == 'one two'


test_truncate()
