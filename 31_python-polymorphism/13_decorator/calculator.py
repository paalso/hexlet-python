class Calculator:
    def __init__(self, acc=0):
        self.acc = acc

    def sum(self, num):
        self.acc += num
        return self.__class__(self.acc)

    def sub(self, num):
        self.acc -= num
        return self.__class__(self.acc)

    def mul(self, num):
        self.acc *= num
        return self.__class__(self.acc)

    def result(self):
        return self.acc
