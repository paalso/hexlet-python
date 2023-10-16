from hexlet_pytest.my_object import MyObject
from unittest.mock import Mock


def test_my_object():
    # Создаем мок-объект для зависимости
    mock_dependency = Mock()

    # Создаем объект, который мы будем тестировать
    my_object = MyObject(mock_dependency)

    # Имитируем поведение зависимости в мок-объекте
    mock_dependency.some_method.return_value = 42

    # Тестируем метод объекта
    result = my_object.my_method("some argument")

    # Проверяем, что метод объекта вызвал метод зависимости
    # с правильным аргументом
    mock_dependency.some_method.assert_called_once_with("some argument")

    # Проверяем, что метод объекта вернул правильный результат
    assert result == 42
