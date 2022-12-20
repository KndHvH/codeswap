from service.features.read import read_file
from service.features.add import add_file
from service.text.manage_json import *
from service.text.get_key import get_key
import click
import os
scriptPath = os.path.dirname(__file__)


def edit_file(title, user):

    file = read_file(title, user)

    with open('database/temp.txt') as txt:
        for line in file:
            txt.write(f'{line}\n')

    master = click.edit(require_save=True, filename='database/temp.txt')

    print(master)

    
    key = get_key(title, user)

    json = add_file(master, key, title, user)

    save_json(json, replace=True)
