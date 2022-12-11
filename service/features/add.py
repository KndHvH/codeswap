import click

from service.text.swap import swap
from service.bin import *
from service.login import login
from service.text.generator import genCode
from service.managejson import save_json


def add(master, password, title, user):

    master = swap(master, password)

    password = ':' + password

    user = user*int(bin_to_count(code_to_bin(password)))

    if len(str(user)) > 255:
        return {'title': title, 'user': user, 'file': master}
    return {'title': 'None', 'user': 'None', 'file': 'None'}



    