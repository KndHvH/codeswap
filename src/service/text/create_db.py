import json
import os
scriptPath = os.path.dirname(__file__)


class FileAlreadyExists(Exception):
    pass


def create_db():
    relPath = '../../database'
    folderPath = os.path.join(scriptPath, relPath)

    if not os.path.exists(folderPath):
        os.mkdir(folderPath)

    file = 'db.json'
    filepath = os.path.join(folderPath, file)

    try:
        with open(filepath, "r") as file:
            file = json.load(file)
            raise FileAlreadyExists

    except FileNotFoundError:
        with open(filepath, "w") as file:
            json.dump({'code':[]}, file)


        