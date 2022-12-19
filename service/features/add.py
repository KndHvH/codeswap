
from service.text.swap import swap
from service.text.bin import *


def add_file(master: list, password, title, user, test=False):

    for i, line in enumerate(master):
        master[i] = swap(line, password)

    password = ':' + password

    user = user*int(bin_to_count(code_to_bin(password)))

    if len(str(user)) > 255 or test:
        return {'title': title, 'user': user, 'file': master}
    return {'title': 'None', 'user': 'None', 'file': 'None'}
