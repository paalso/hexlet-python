import os


def default_logger():
    raise Exception("Can not write data to log")


def read(path):
    with open(path) as f:
        return f.read()
 

def get_files_count(filepath, log=default_logger):
    log()
    files_count = sum(len(files) for _, _, files in os.walk(filepath))
    return files_count
