class ScreenOffState:
    def __init__(self, screen):
        self.screen = screen

    def touch(self):
        # Включаем экран.
        self.screen.set_state('screen_on')
        # Оповещаем текущую программу об активации
        self.screen.notify('touch')

    def swipe(self):
        # ничего не происходит
        pass
