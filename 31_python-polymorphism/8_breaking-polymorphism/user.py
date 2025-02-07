class User:
    def __init__(self, name):
        self.name = name
        # BEGIN (write your solution here)

        # END

    def get_name(self):
        return self.name

    # BEGIN (write your solution here)
    def greet(self):
        return f'Hello {self.get_name()}!'
    # END
