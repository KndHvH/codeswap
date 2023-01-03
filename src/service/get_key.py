

from src.service.binary import bin_to_code, count_to_bin
from src.service.manage_json import get_json


def get_key(title, user):
    files = get_json()['code']

    for file in files:
        if file['title'] == title:
            key = bin_to_code(count_to_bin(file['user']//user))

            return key[1:]
    return None
