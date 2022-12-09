import json
import os
scriptPath = os.path.dirname(__file__)

from service.db_man.create_db import create_db


def save_json(dict):
    #{'code': [{'title': 'test', 'file': 'rfxr'},]}
    files = get_json()

    if files == None:
        files = []
    else:
        files = files['code']

    files.append(dict)

    full_file = {'code': files}

    relPath = '../../database/db.json'
    filepath = os.path.join(scriptPath, relPath)
    with open(filepath, 'w') as outfile:
        json.dump(full_file, outfile)
        # remove str\


def get_json():
    for i in range(0,2):
        try:
            relPath = '../../database/db.json'
            filepath = os.path.join(scriptPath, relPath)
            with open(filepath, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            create_db()


def get_file(title):
    file = get_json()
    file = file['code']

    for i in file:
        if i['title'] == title:
            return i['file']
    return 'None'
