# https://ru.hexlet.io/courses/python-testing/lessons/fixtures/exercise_unit

# Подготовка данных
# ================

"""
Напишите тесты для функции set(coll, path, value) возвращающей словарь,
в котором она изменяет (или добавляет) значение по указанному пути.
Функция мутирует словарь:

>>> coll = { "a": { "b": { "c": 3 } } }
>>> set(coll, ["a", "b", "c"], 4)
>>> coll["a"]["b"]["c"]
4

>>> set(coll, ['x', 'y', 'z'], 5)
>>> coll['x']['y']['z']
5
"""

@pytest.fixture
def get_dict():
    return { "a": { "b": { "c": 3 } } }


def test_set(get_dict):
    assert get_dict == 4
