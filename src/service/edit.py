
import click
import os
from src.service.generator import genCode
from src.service.get_dict import get_dict
from src.service.get_file import get_file_text
from src.service.get_key import get_key
from src.service.manage_json import save_json

scriptPath = os.path.dirname(__file__)


def edit_file(title, user, delete=False):

    file = get_file_text(title, user)

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
