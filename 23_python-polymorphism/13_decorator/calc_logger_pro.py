# GPT Version:
# Класс CalcLogger можно упростить и сделать его более компактным и читаемым с
# помощью использования атрибута __getattr__ для перехвата всех операций,
# выполняемых над экземпляром Calculator. Вместо создания метода sum, sub,
# и mul вручную, вы можете динамически определить их и автоматически выполнять
# логирование. Вот улучшенная версия класса CalcLogger:

class CalcLoggerPro:
    def __init__(self, calculator):
        self.calculator = calculator
        self.operations = []

    def __getattr__(self, attr):
        if attr in ('sum', 'sub', 'mul'):
            def wrapper(*args):
                first_operand = self.calculator.result()
                operation_func = getattr(self.calculator, attr)
                result = operation_func(*args).result()
                self._print_log_message(first_operand, args[0], result, attr)
                self.operations.append((attr, args[0], result))
                return self
            return wrapper
        elif attr == 'result':
            def get_result():
                return self.calculator.result()
            return get_result
        else:
            raise AttributeError(
                f"'CalcLogger' object has no attribute '{attr}'")

    def _print_log_message(
            self, first_operand, second_operand, result, operation):
        operation_name = {
            'sum': 'Сумма',
            'sub': 'Разность',
            'mul': 'Результат',  # Произведение
        }[operation]
        print("Первое число: {0} Второе число: {1} {3}: {2}".format(
            first_operand, second_operand, result, operation_name
        ))

# В этой версии класса CalcLogger мы используем метод __getattr__ для
# перехвата операций sum, sub, и mul динамически. Код становится более
# читаемым и гибким, и он автоматически поддерживает логирование всех
# этих операций.
