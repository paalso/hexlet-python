from HTMLElement import HTMLElement


# BEGIN (write your solution here)
class HTMLPairElement(HTMLElement):
    def get_text_content(self):
        if 'text_content' in self.__dict__:
            return self.text_content
        return ''    

    def set_text_content(self, text):
        self.text_content = text

    def __str__(self) -> str:
        return f'<{self.get_tag()}{self._stringify_attributes()}>' + \
               f'{self.get_text_content()}</{self.get_tag()}>'
# END

'''
# BEGIN
class HTMLPairElement(HTMLElement):
    def __init__(self, attributes=None):
        super().__init__(attributes)
        self._body = ''

    def __str__(self):
        attr_line = self._stringify_attributes()
        name = self.get_tag_name()
        body = self.get_text_content()
        return f'<{name}{attr_line}>{body}</{name}>'

    def get_text_content(self):
        return self._body

    def set_text_content(self, body):
        self._body = body
# END
'''