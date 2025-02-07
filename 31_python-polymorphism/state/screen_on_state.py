class ScreenOnState:
    def __init__(self, screen):
        self.screen = screen

    def touch(self):
        self.screen.notify('touch')

    def swipe(self):
        self.screen.notify('swipe')
