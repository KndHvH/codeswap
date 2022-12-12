from service.features.add import add_file
from service.features.read import read_file
from service.managejson import *
from service.text.title_verificator import title_verif


import os
scriptPath = os.path.dirname(__file__)


class TestClass:

    def test_when_add_recieve_text_return_json(self):

        text = 'text'
        password = 'rtef'
        title = 'test'
        user = int('1'*300)

        expect = 'test'

        assert expect == add_file(text, password=password,
                                  title=title, user=user)['title']

    def test_when_receive_json_create_file(self):

        entry = {'title': 'test2', 'file': 'rfxr'}

        save_json(entry)

        data = get_file(entry['title'])

        assert data == entry['file']

    def test_when_add_text_create_file_and_read_file(self):

        entry = 'text'
        title = 'test3'
        password = 'abcdefghij'
        user = int('1'*300)

        json = add_file(entry, password, title, user)
        save_json(json)

        data = read_file(title, user)

        assert data == entry

    def test_when_add_receive_less_300_user_return_json(self):

        entry_user = 1233
        expect = {'title': 'None', 'user': 'None', 'file': 'None'}

        assert expect == add_file('text', 'pass', 'title', entry_user)

    def test_when_title_verif_receive_test4_already_created_return_false(self):

        entry = {'title': 'test4', 'file': 'rfxr'}
        expect = False

        save_json(entry)

        assert title_verif('test4') == expect

    def test_delete_feature(self):

        entry_file_list = [
            {
                'title': 'title',
                'code': 'code',
                'file': 'file'
            },
            {
                'title': 'mustremove',
                'code': 'code',
                'file': 'file'
            },
        ]

        entry = {
            'title': 'mustremove',
            'code': 'code',
            'file': 'file'
        }

        expected = [
            {
                'title': 'title',
                'code': 'code',
                'file': 'file'
            }
        ]

        assert expected == delete(entry_file_list, entry)

    def test_when_save_json_receive_double_files_replace_call_delete_funcion(self):

        entry = {
            'title': 'title6',
            'code': 'code',
            'file': 'oldfilefile'
        }

        entry2 = {
            'title': 'title6',
            'code': 'code',
            'file': 'newfile'
        }

        expect = [{
            'title': 'title6',
            'code': 'code',
            'file': 'newfile'
        }]

        relPath = '../database/db.json'
        filepath = os.path.join(scriptPath, relPath)

        os.remove(filepath)

        create_db()

        save_json(entry)
        save_json(entry2)

        assert expect == get_json()['code']
