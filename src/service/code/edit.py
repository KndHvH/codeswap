
import click
import os
scriptPath = os.path.dirname(__file__)


def edit_file(title, user, delete=False):

    file = read_file(title, user)

    if not file:
        json = add_file(click.edit(), genCode(), title, user)

    else:
        if delete:
            master = ''

        else:
            master = click.edit(file)

            if master == None:
                master = file

        key = get_key(title, user)

        json = add_file(master, key, title, user)

    save_json(json)
