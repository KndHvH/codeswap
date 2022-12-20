from service.text.create_db import create_db, FileAlreadyExists
import os
import json
import pytest
from service.text.manage_json import get_json, get_file
scriptPath = os.path.dirname(__file__)


class TestClass:
    def test_when_create_file_runs_must_create_empty_json(self):

        expect = {'code': []}

        relPath = '../database/db.json'
        filepath = os.path.join(scriptPath, relPath)

        if os.path.exists(filepath):
            os.remove(filepath)

        create_db()

        with open(filepath, "r") as file:
            file = json.load(file)

        assert expect == file

    def test_when_create_file_receive_file_already_created_must_return_exception(self):

        with pytest.raises(FileAlreadyExists):

            create_db()

    def test_when_file_dont_exists_its_get_created_when_acess(self):

        relPath = '../database/db.json'
        filepath = os.path.join(scriptPath, relPath)

        if os.path.exists(filepath):
            os.remove(filepath)

        assert get_json() != None

    def test_when_get_file_cant_find_file_return_none(self):

        relPath = '../database/db.json'
        filepath = os.path.join(scriptPath, relPath)

        if os.path.exists(filepath):
            os.remove(filepath)

        assert get_file('title') == 'None'
