
import click
import os
from src.service.generator import genCode
from src.service import get_dict, get_file, get_key
from src.service.manage_json import save_json

scriptPath = os.path.dirname(__file__)


def edit_file(title, user, delete=False):

    file = get_file(title, user)

    if not file:
        json = get_dict(click.edit(), genCode(), title, user)

    else:
        if delete:
            master = ''

        else:
            master = click.edit(file)

            if master == None:
                master = file

        key = get_key(title, user)

        json = get_dict(master, key, title, user)

    save_json(json)
