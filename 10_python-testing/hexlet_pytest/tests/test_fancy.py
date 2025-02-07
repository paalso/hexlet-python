import pytest
from hexlet_pytest.fancy import compact, flatten, select


# Создаем фикстуру
# Запускается перед каждым тестом
@pytest.fixture
def coll():     # имя фикстуры выбирается произвольно
    return ['One', True, 3, [1, 'hexlet', [0]], 'cat', {}, '', [], False]


# Pytest сам прокидывает результат вызова функции там, где функция указана в аргументе
# Имя параметра совпадает с именем фикстуры
def test_compact(coll):
    result = compact(coll)
    assert result is None   # Тут ожидаемое значение


# Не важно, что предыдущий тест сделал с коллекцией
# Здесь коллекция будет новая, так как pytest вызывает coll() заново
def test_select(coll):
    result = select(coll, ...)
    assert result is None   # Тут ожидаемое значение


def test_flatten(coll):
    result = flatten(coll, ...)
    assert result is None   # Тут ожидаемое значение
