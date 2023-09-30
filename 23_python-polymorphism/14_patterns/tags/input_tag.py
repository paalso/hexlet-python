class InputTag:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def render(self):
        return f'<input type="{self.type}" value="{self.value}">'

    def __str__(self):
        return self.render()
