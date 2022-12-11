import click

from service.text.swap import swap
from service.bin import *


def add_file(master, password, title, user):

    master = swap(master, password)

    password = ':' + password

    user = user*int(bin_to_count(code_to_bin(password)))

    if len(str(user)) > 255:
        return {'title': title, 'user': user, 'file': master}
    return {'title': 'None', 'user': 'None', 'file': 'None'}
