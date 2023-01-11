import os
import json
import click
from src.helper.app import AppHelper
from src.helper.binary import BinaryHelper
from src.helper.string import StringHelper
from src.service.database.database import Database

script_path = os.path.dirname(__file__)


class Repository():
    app = AppHelper()
    DATABASE_PATH = app.db_path

    @staticmethod
    def _local_json_path():
        return os.path.join(script_path, Repository.DATABASE_PATH)

    @staticmethod
    def get_json(path=None) -> None:
        if path == None:
            path = Repository._local_json_path()
        for _ in range(0, 2):
            try:
                with open(path, "r") as file:
                    return json.load(file)

            except FileNotFoundError:
                Database()

    @staticmethod
    def get_file_content(title):
        files = Repository.get_json()['code']

        for file in files:
            if file['title'] == title:
                return file['file']

    @staticmethod
    def get_file_text(title, user):
        key = Repository.get_key(title, user)
        if key != None:

            file = Repository.get_file_content(title)

            return StringHelper.swap(file, key)

    @staticmethod
    def save_json(dict, replace=False):
        files = Repository.get_json()
        files = [] if files == None else files['code']

        for file in files:
            if file['title'] == dict['title']:
                replace = True

        if replace:
            files = Repository.delete(files, dict)

        if dict['file'] != '':
            files.append(dict)

        Repository.save_on_dbjson_file(files)

    @staticmethod
    def save_on_dbjson_file(files):

        full_file = {'code': files}
        file_path = os.path.join(script_path, Repository.DATABASE_PATH)

        with open(file_path, 'w') as outfile:
            json.dump(full_file, outfile)

    @staticmethod
    def delete(files, dict):

        for i, v in enumerate(files):
            if v['title'] == dict['title']:
                files.pop(i)

        return files

    @staticmethod
    def get_key(title, user):
        files = Repository.get_json()['code']

        for file in files:
            if file['title'] == title:
                key = BinaryHelper.binary_to_code(
                    BinaryHelper.count_to_binary(file['user']//user))

                return key[1:]

    @staticmethod
    def gen_dict(master, password, title, user) -> dict:

        master = StringHelper.swap(master, password)
        password = ':' + password
        user = user * \
            int(BinaryHelper.binary_to_count(
                BinaryHelper.code_to_binary(password)))

        data = {'title': '', 'user': '', 'file': ''}

        if len(str(user)) > 255:
            data['file'] = master
            data['title'] = title
            data['user'] = user

        return data

    @staticmethod
    def edit_file(title, user):

        file = Repository.get_file_text(title, user)

        if not file:
            json = Repository.gen_dict(
                click.edit(), StringHelper.genCode(), title, user)
            Repository.save_json(json)
            return

        master = click.edit(file)

        if master == None:
            master = file

        json = Repository.gen_dict(
            master, Repository.get_key(title, user), title, user)

        Repository.save_json(json)

    @staticmethod
    def delete_file(title, user):

        json = Repository.gen_dict(
            '', Repository.get_key(title, user), title, user)

        Repository.save_json(json)

    @staticmethod
    def get_file_title(title):
        if not title:
            return click.prompt(click.style(
            'file title_', fg='blue'), prompt_suffix='')
        return title
