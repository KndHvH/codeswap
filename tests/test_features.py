from service.features.add import add
from service.json.managejson import *
import json


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