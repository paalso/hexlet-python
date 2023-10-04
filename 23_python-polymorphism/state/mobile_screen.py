from power_off_state import PowerOffState
from screen_on_state import ScreenOnState
from screen_off_state import ScreenOffState


class MobileScreen:
    def __init__(self):
        # Список состояний нужен для переключений между ними
        # Иначе возможно появление циклических зависимостей внутри состояний
        self.states = {
            'power_off': PowerOffState,
            'screen_disabled': ScreenOffState,
            'screen_on': ScreenOnState,
        }
        # Начальное состояние
        # Внутрь передается текущий объект
        # Это нужно для смены состояний (примеры ниже)
        self.set_state('power_off')

    def __str__(self) -> str:
        return f'{self.state.__class__.__name__}'

    def set_state(self, state):
        self.state = self.states[state](self)

    def power_on(self):
        # Предыдущее состояние нас не волнует
        # Все данные хранятся в самом экране
        # Объекты-состояния не имеют своих данных
        self.state = self.states['screen_disabled'](self)

    def touch(self):
        self.state.touch()

    def swipe(self):
        self.state.swipe()

    def notify(self, message):
        print(f'State: {self}, message: {message}')
