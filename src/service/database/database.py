import json
import os
import shutil
from src.helper.app import AppHelper
from src.service.errors.FileAlreadyExistsError import FileAlreadyExists

script_path = os.path.dirname(__file__)


class Database():
    app = AppHelper()

    DATABASE_PATH = app.db_path
    DATABASE_FILE_NAME = app.db_file_name
    DATABASE_FOULDER_PATH = app.db_foulder_path

    def __init__(self) -> None:
        self.__create_db()

    def __create_db(self):

        if Database.__move_foulder():
            return

        database_foulder_path = os.path.join(script_path, self.DATABASE_FOULDER_PATH)

        if not os.path.exists(database_foulder_path):
            os.mkdir(database_foulder_path)

        filepath = os.path.join(database_foulder_path, self.DATABASE_FILE_NAME)

        try:
            with open(filepath, "r") as file:
                file = json.load(file)
                raise FileAlreadyExists

        except FileNotFoundError:
            with open(filepath, "w") as file:
                json.dump({'code': []}, file)

    def __move_foulder():
        old_path = '../../../../database'
        folder_path = os.path.join(script_path, old_path)

        if not os.path.exists(folder_path): return False

        rel_path = Database.DATABASE_FOULDER_PATH
        destiny_path = os.path.join(script_path, rel_path)

        shutil.move(folder_path, destiny_path)

        return True
