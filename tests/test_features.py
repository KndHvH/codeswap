from service.features.add import add
from service.features.read import read
from service.json.managejson import *
from service.text.splitKey import getKey
from service.text.titleVerificator import  titleVerif

import pytest


class TestClass:

    def test_when_add_recieve_text_return_json(self):

        text = 'text'
        password = 'rtef'
        title = 'test'

        expect = {'title': 'test', 'file': 'rfxr'}

        assert expect == add(text, password=password, title=title)

    def test_when_receive_json_create_file(self):

        entry = {'title': 'test2', 'file': 'rfxr'}

        save_json(entry)

        data = get_file(entry['title'])

        assert data == entry['file']

    def test_when_add_secret_create_file_and_read_file(self):

        entry = 'secret'
        key = 'test3:abcdefghij'

        keyList = getKey(key)

        json = add(entry, keyList[1], keyList[0])
        save_json(json)

        data = read(key)

        assert data == entry

    def test_when_title_verif_receive_test4_already_created_return_false(self):

        entry = {'title': 'test4', 'file': 'rfxr'}
        expect = False

        save_json(entry)

        assert titleVerif('test4') == expect
            
