import json
import os
from dataclasses import dataclass

from src.service.errors import FileAlreadyExists

script_path = os.path.dirname(__file__)

@dataclass
class Database():
    DATABASE_PATH: str = os.environ['DATABASE_PATH']
    DATABASE_FILE_NAME: str = os.environ['DATABASE_FILE_NAME']
    DATABASE_RELATIVE_PATH: str = os.environ['DATABASE_RELATIVE_PATH']

    def __init__(self) -> None:
        self.__create_db()

    def __create_db(self):
    
        if Database.__move_foulder(): return

        database_path = os.path.join(script_path, self.DATABASE_PATH)

        if not os.path.exists(database_path):
            os.mkdir(database_path)

        filepath = os.path.join(database_path, self.DATABASE_FILE_NAME)

        try:
            with open(filepath, "r") as file:
                file = json.load(file)
                raise FileAlreadyExists

        except FileNotFoundError:
            with open(filepath, "w") as file:
                json.dump({'code':[]}, file)



    def __move_foulder():
        relPath = '../../database'
        folderPath = os.path.join(script_path, relPath)

        if not os.path.exists(folderPath): return False


        relPath = '../database'
        destinyPath = os.path.join(scriptPath, relPath)
        
        shutil.move(folderPath,destinyPath)

        return True