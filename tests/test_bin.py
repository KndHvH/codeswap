

from service.text.bin import *

class TestClass:
    

    def test_when_code_to_bin_receive_test_must_return_bin(self):
        entry = 'test'
        expect = '01110100011001010111001101110100'

        assert expect == code_to_bin(entry)

    def test_when_bin_to_count_receive_bin_must_return_count(self):
        entry = '01110100011001010111001101110100'
        expect = '11321121120312113231'

        assert expect == bin_to_count(entry)

    def test_when_count_to_bin_receive_count_must_return_bin(self):
        entry = '11321121120312113231'
        expect = '01110100011001010111001101110100'

        assert expect == count_to_bin(entry)

    def test_when_bin_to_code_receive_bin_must_return_test(self):
        entry = '01110100011001010111001101110100'
        expect = 'test'

        assert expect == bin_to_code(entry)