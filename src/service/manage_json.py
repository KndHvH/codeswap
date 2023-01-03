
import json
import os

from src.service.remove_file_from_list import delete
from src.service.manage_bd import create_db
scriptPath = os.path.dirname(__file__)


def save_json(dict, replace=False):
    files = get_json()

    files = [] if files == None else files['code']

    for file in files:
        if file['title'] == dict['title']:
            replace = True

    if replace:
        files = delete(files, dict)

    if dict['file'] != '':
        files.append(dict)

    save_on_dbjson_file(files)

def save_on_dbjson_file(files):
    full_file = {'code': files}

    relPath = '../database/db.json'
    filepath = os.path.join(scriptPath, relPath)
    with open(filepath, 'w') as outfile:
        json.dump(full_file, outfile)


def local_path():
    relPath = '../database/db.json'
    return os.path.join(scriptPath, relPath)

def get_json(path=local_path()):
    for i in range(0, 2):
        try:            
            with open(path, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            create_db()


def get_file(title):
    file = get_json()['code']

    for i in file:
        if i['title'] == title:
            return i['file']
    return 'None'


