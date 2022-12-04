from service.features.add import add
from service.features.read import read
from service.json.managejson import *
from service.text.splitKey import getKey


class TestClass:

    def test_when_add_recieve_text_return_json(self):

        text = 'text'
        password = 'rtef'
        title = 'test'

        expect = {'code': [{'title': 'test', 'file': 'rfxr'}]}

        assert expect == add(text, password=password,title=title)


    def test_when_receive_json_create_file(self):

        entry = {'code': [{'title': 'test', 'file': 'rfxr'}]}

        save_json(entry)

        data = read_json(entry['code'][0]['title'])
       
        assert data == entry


    def test_when_add_secret_create_file_and_read_file(self):

        entry = 'secret'
        key = 'test:abcdefghij'

        keyList = getKey(key)

        json = add(entry,keyList[1],keyList[0])
        save_json(json)

        data = read(key)
       
        assert data == entry