from File import File
from errors.FileError import FileError
from errors.NotReadableError import NotReadableError
from errors.NotExistsError import NotExistsError


# BEGIN (write your solution here)
def read_files(file_paths):
    result = []
    for path in file_paths:
        try:
            content = File(path).read()
            result.append(content)
        except FileError as e:
            result.append(None)
    return result
# END
