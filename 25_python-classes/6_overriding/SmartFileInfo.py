from FileInfo import FileInfo


# BEGIN (write your solution here)
class SmartFileInfo(FileInfo):
    allowed_units = {
        'b': 1,
        'kb': 1024.0
    }
    def get_size(self, unit='b'):
        if unit not in self.__class__.allowed_units:
            raise ValueError(f'File size error: {unit} unit does not exist')
        size_in_bytes = super().get_size()
        if unit == 'b':
            return size_in_bytes
        return  size_in_bytes / self.__class__.allowed_units[unit]
# END
