import click

from service.text.generator import genCode
from service.features.add import add_file
from service.features.read import read_file
from service.features.edit import edit_file
from service.text.manage_json import save_json
from service.text.manage_json import get_json


def menu_add(title, user):
    json = add_file(click.edit(), genCode(), title, user)
    save_json(json)


def menu_read(title, user):
    click.echo(read_file(title, user))


def menu_edit(title, user):
    edit_file(title, user)


def menu_delete(title, user):
    click.echo(read_file(title, user))

    if click.confirm(click.style('confirm delete?', bg='red', fg='white'), prompt_suffix=''):
        edit_file(title, user, delete=True)

def menu_list_files():
    files =  get_json()['code']
    titles = []
    
    for file in files:
        titles.append(file['title'])

    return titles