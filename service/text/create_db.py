import json
import os
scriptPath = os.path.dirname(__file__)


class FileAlreadyExists(Exception):
    pass


def create_db():
    relPath = '../../database/db.json'
    filepath = os.path.join(scriptPath, relPath)

    create_foulder()

    try:
        with open(filepath, "r") as file:
            file = json.load(file)
            raise FileAlreadyExists

    except FileNotFoundError:
        with open(filepath, "w") as file:
            json.dump({'code':[]}, file)

def create_foulder():
    relPath = '../../database'
    filepath = os.path.join(scriptPath, relPath)

    if not os.path.exists(filepath):
        os.mkdir(filepath)

        