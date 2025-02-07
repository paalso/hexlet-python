from HTMLElement import HTMLElement


class HTMLHrElement(HTMLElement):
    def __str__(self):
        return f'<hr{self.stringify_attributes()}>'
