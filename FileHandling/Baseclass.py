from datetime import datetime
from pathlib import Path

import pytz


class Base:
    def __int__(self):
        pass


def create_directory():
    # Creating path with test data directory
    path = Path.cwd().joinpath('./testdata/')
    if path.exists():
        print("Folder is already created")
    else:
        print("Creating directory")
        Path(path).mkdir()
    return path


def create_file(extension):
    date = datetime.now(pytz.timezone('Asia/Kolkata'))
    file_name = date.strftime("%d-%m-%Y %I:%M") + extension
    print("file name:", file_name)
    file_path = str(create_directory()) + "/" + file_name
    f = open(file_path, 'w')
    return file_path


def get_file_path(extension):
    date = datetime.now(pytz.timezone('Asia/Kolkata'))
    file_name = date.strftime("%d-%m-%Y") + extension
    print("file name:", file_name)
    file_path = str(create_directory()) + "/" + file_name
    return file_path
