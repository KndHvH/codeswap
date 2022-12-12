from service.text.manage_json import get_json
from service.text.bin import *


def get_key(title, user):
    file = get_json()
    file = file['code']

    for i in file:
        if i['title'] == title:
            key = bin_to_code(count_to_bin(i['user']//user))

            return key[1:]
    return None
