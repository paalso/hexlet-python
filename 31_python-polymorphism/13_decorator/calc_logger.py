class CalcLogger:
    def __init__(self, calculator):
        self.calculator = calculator

    def result(self):
        return self.calculator.result()

    def sum(self, num):
        first_operand = self.result()
        operation_result = self.calculator.sum(num).result()
        self._print_log_message(first_operand, num, operation_result, '+')
        return self

    def sub(self, num):
        first_operand = self.result()
        operation_result = self.calculator.sub(num).result()
        self._print_log_message(first_operand, num, operation_result, '-')
        return self

    def mul(self, num):
        first_operand = self.result()
        operation_result = self.calculator.mul(num).result()
        self._print_log_message(first_operand, num, operation_result, '*')
        return self

    def _print_log_message(
            self, first_operand, second_operand, result, operation):
        operation_name = {
            '+': 'Сумма',
            '-': 'Разность',
            '*': 'Результат',    # Произведение
        }[operation]
        print("Первое число: {0} Второе число: {1} {3}: {2}".format(
            first_operand, second_operand, result, operation_name
        ))
