import os


class FileInfo:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_stat = os.stat(self.file_path)

    def get_size(self):
        return self.file_stat.st_size
