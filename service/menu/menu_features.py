import click

from service.text.generator import genCode
from service.features.add import add_file
from service.features.read import read_file
from service.features.edit import edit_file
from service.text.manage_json import save_json


def menu_add(title, user):
    master = list(input(click.style('file_', fg='green')))
    json = add_file(master, genCode(), title, user)
    save_json(json)


def menu_read(title, user):
    click.echo(read_file(title, user))


def menu_edit(title, user):
    click.echo(read_file(title, user))
    newText = input(click.style('new file_', fg='green'))    
    edit_file(newText, title, user)


def menu_delete(title,user):
    click.echo(read_file(title, user))
    if input('d_to_delete_') == 'd':
        edit_file('', title, user)

