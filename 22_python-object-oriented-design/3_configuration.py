# https://ru.hexlet.io/courses/python-object-oriented-design/lessons/configuration/exercise_unit
# https://ru.hexlet.io/code_reviews/1133501

# Python: Объектно-ориентированный дизайн 
# 2. Конфигурация

# Реализуйте класс PasswordValidator ориентируясь на тесты.
# Этот валидатор поддерживает следующие опции:
# min_len (по умолчанию 8) — минимальная длина пароля
# contain_numbers (по умолчанию False) — требование содержать хотя бы одну цифру

class PasswordValidator():
    OPTIONS = {
        'min_len': 8,
        'contain_numbers': False,
        }

    def __init__(self, **options):
        self.options = PasswordValidator.OPTIONS | options

    def validate(self, password):
        errors = {}
        if len(password) < self.options['min_len']:
            errors['min_len'] = 'too small'
        if self.options['contain_numbers'] and \
                not self._has_number(password):
            errors['contain_numbers'] = 'should contain at least one number'
        return errors

    def _has_number(self, password):
        return any(char.isdigit() for char in password)


def test_validate_with_default_options():
    validator = PasswordValidator()
    errors1 = validator.validate('qwertyui')
    assert not errors1

    errors2 = validator.validate('qwerty')
    assert errors2 == {'min_len': 'too small'}

    errors3 = validator.validate('another-password')
    assert not errors3


def test_validate_with_options():
    validator = PasswordValidator(contain_numbers=True)
    errors1 = validator.validate('qwertya3sdf')
    assert not errors1

    errors2 = validator.validate('qwerty')
    assert errors2 == {
        'min_len': 'too small',
        'contain_numbers': 'should contain at least one number'
        }
    errors3 = validator.validate('q23ty')
    assert errors3 == {'min_len': 'too small'}


def test_validate_with_incorrect_options():
    validator = PasswordValidator(contain_numberz=None)
    errors1 = validator.validate('qwertya3sdf')
    assert not errors1

    errors2 = validator.validate('qwerty')
    assert errors2 == {'min_len': 'too small'}


# test_validate_with_default_options()
# test_validate_with_options()
test_validate_with_incorrect_options()
