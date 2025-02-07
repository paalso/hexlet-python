class HTMLElement:
    def __init__(self, attributes=None):
        self.attributes = attributes if attributes else {}
        self.body = None

    def set_attribute(self, key, value):
        self.attributes[key] = value

    def get_attribute(self, key):
        return self.attributes.get(key)

    def set_text_content(self, body):
        self.body = body

    def get_text_content(self):
        return self.body

    def stringify_attributes(self):
        if not self.attributes:
            return ''
        attribute_string = ' '.join(
            f'{key}="{value}"' for key, value in self.attributes.items())
        return f' {attribute_string}'

"""
Hexlet's version
    # BEGIN
    def _stringify_attributes(self):
        print(self.attributes.items())
        line = ''.join(f' {k}="{v}"' for k, v in self.attributes.items())
        return line
    # END
"""
