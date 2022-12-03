from service.features.add import add


class TestClass:

    def test_when_add_recieve_text_return_json(self):

        text = 'text'
        password = 'rtef'
        title = 'test'
        expect = {'code': [{'title': 'test', 'file': 'rfxr'}]}

        assert expect == add(text, password=password,title=title)
