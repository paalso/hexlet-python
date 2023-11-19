import os
from errors.NotExistsError import NotExistsError
from errors.NotReadableError import NotReadableError


class File:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        filepath = self.filepath

        # BEGIN (write your solution here)
        if not os.path.exists(filepath):
            raise NotExistsError(f'{filepath} no exists')
        
        if not os.access(filepath, os.R_OK):
            raise NotReadableError(f'{filepath} is no readable')
        # END
        with open(filepath, 'r') as file:
            return file.read()
