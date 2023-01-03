
from src.service.text.swap import swap
from src.service.text.bin import *


def add_file(master, password, title, user, test=False) -> dict:

    master = swap(master, password)

    password = ':' + password

    user = user*int(bin_to_count(code_to_bin(password)))

    if len(str(user)) > 255 or test:
        return {'title': title, 'user': user, 'file': master}
    return {'title': '', 'user': '', 'file': ''}
