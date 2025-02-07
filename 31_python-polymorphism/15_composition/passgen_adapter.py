from passgen import generate_password


class PasswordGeneratorAdapter():
    def generate_password(self, len, options=[]):
        return generate_password(len, *options)
