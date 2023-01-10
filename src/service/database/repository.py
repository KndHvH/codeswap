import os
import json
from src.helper.app import AppHelper
from src.helper.binary import BinaryHelper
from src.helper.string import StringHelper
from src.service.database.database import Database

script_path = os.path.dirname(__file__)

class Repository():
    DATABASE_PATH: str = AppHelper.get_db_path()

    def _local_json_path(self):
        return os.path.join(script_path, self.DATABASE_PATH)

    def get_json(self) -> None:
        for _ in range(0, 2):
            try:            
                with open(self._local_json_path, "r") as file:
                    return json.load(file)

            except FileNotFoundError:
                Database()

    def get_file(self, title):
        file = self.get_json()['code']

        for i in file:
            if i['title'] == title:
                return i['file']
        return 'None'

    def save_json(self, dict, replace=False):
        files = self.get_json()
        files = [] if files == None else files['code']

        for file in files:
            if file['title'] == dict['title']:
                replace = True

        if replace:
            files = self.delete(files, dict)

        if dict['file'] != '':
            files.append(dict)

        self.save_on_dbjson_file(files)
    
    def save_on_dbjson_file(self, files):

        full_file = {'code': files}
        file_path = os.path.join(script_path, self.DATABASE_PATH)

        with open(file_path, 'w') as outfile:
            json.dump(full_file, outfile)

    def delete(self, files, dict):

        for i, v in enumerate(files):
            if v['title'] == dict['title']:
                files.pop(i)

        return files

    
    def get_key(title, user):
        files = Repository.get_json()['code']

        for file in files:
            if file['title'] == title:
                key = BinaryHelper.binary_to_code(BinaryHelper.count_to_binary(file['user']//user))

                return key[1:]
        return None


    def add_file(master, password, title, user) -> dict:

        master = StringHelper.swap(master, password)
        password = ':' + password
        user = user * int(BinaryHelper.binary_to_count(BinaryHelper.code_to_binary(password)))

        data = {'title': '', 'user': '', 'file': ''}

        if len(str(user)) > 255:
            data['file'] = master
            data['title'] = title
            data['user'] = user

        return data