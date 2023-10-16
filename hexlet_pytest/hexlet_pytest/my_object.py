class MyObject:
    def __init__(self, dependency):
        self.dependency = dependency

    def my_method(self, arg):
        # какой-то метод, который зависит от зависимости
        return self.dependency.some_method(arg)
