from service.features.read import read_file
from service.features.add import add_file
from service.text.manage_json import *
from service.text.get_key import get_key
import click
import os
scriptPath = os.path.dirname(__file__)


def edit_file(title, user, delete=False):

    file = read_file(title, user)

    if not delete:
        master = click.edit(file)

        if master == None:
            master = file
    else:
        master = ''
        
    key = get_key(title, user)

    json = add_file(master, key, title, user)


    save_json(json, replace=True)
