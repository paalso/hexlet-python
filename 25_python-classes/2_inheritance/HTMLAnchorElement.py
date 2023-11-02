from HTMLElement import HTMLElement


class HTMLAnchorElement(HTMLElement):
    def __str__(self):
        attr_line = self.stringify_attributes()
        body = self.get_text_content()
        return f'<a{attr_line}>{body}</a>'
