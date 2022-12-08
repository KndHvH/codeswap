import os
import json
scriptPath = os.path.dirname(__file__)


def title_verif(title) -> bool:
    relPath = '../../database/db.json'
    filepath = os.path.join(scriptPath, relPath)
    with open(filepath, "r") as file:
        db = json.load(file)

        for file in db['code']:
            if file['title'] == title:
                return False
        return True
