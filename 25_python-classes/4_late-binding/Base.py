class Base:
    # BEGIN (write your solution here)
    def is_instance_of(self, classname):
        return classname in self._ancestor_names()

    def _ancestor_names(self):
        return list(map(
            self._class_name,
            self.__class__.mro())) 

    def _class_name(self, clazz):
        return clazz.__name__
    # END
