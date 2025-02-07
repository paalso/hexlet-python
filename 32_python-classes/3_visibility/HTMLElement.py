class HTMLElement:
    def __init__(self, attributes=None):
        self.attributes = attributes or {}

    def get_attribute(self, key):
        return self.attributes.get(key)

    def get_attributes(self):
        return self.attributes

    # BEGIN (write your solution here)
    def add_tag(self, tag_name):
        if not self.__check_tag(tag_name):
            tags = self.attributes.get('tag', '')
            new_tags = self.__add_token_to_string(tags, tag_name)
            self.attributes['tag'] = new_tags

    def remove_tag(self, tag_name):
        if self.__check_tag(tag_name):
            tags = self.attributes['tag']
            self.attributes['tag'] = \
                self.__remove_token_from_string(tags, tag_name)

    def toggle_tag(self, tag_name):
        if not self.__check_tag(tag_name):
            self.add_tag(tag_name)
        else:
            self.remove_tag(tag_name)

    def __check_tag(self, tag_name):
        return tag_name in self.attributes.get('tag', '').split()

    def __add_token_to_string(self, string, token):
        tokens = string.split() + [token]
        return ' '.join(tokens)

    def __remove_token_from_string(self, string, token):
        tokens = string.split()
        tokens.remove(token)
        return ' '.join(tokens)
    # END
