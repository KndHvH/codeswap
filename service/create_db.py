import json
import os
scriptPath = os.path.dirname(__file__)


class FileAlreadyExists(Exception):
    pass


def create_db():
    try:
        relPath = '../database/db.json'
        filepath = os.path.join(scriptPath, relPath)
        with open(filepath, "r") as file:
            file = json.load(file)
            raise FileAlreadyExists

    except FileNotFoundError:
        with open(filepath, "w") as file:
            json.dump({'code':[]}, file)

