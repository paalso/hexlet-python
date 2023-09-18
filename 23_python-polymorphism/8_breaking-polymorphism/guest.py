class Guest:
    def __init__(self):
        self.name = 'Guest'
        # BEGIN (write your solution here)

        # END

    def get_name(self):
        return self.name

    # BEGIN (write your solution here)
    def greet(self):
        return f'Nice to meet you {self.get_name()}'
    # END
