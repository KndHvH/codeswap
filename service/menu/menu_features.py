import click

from text.generator import genCode
from features.add import add_file
from features.read import read_file
from features.edit import edit_file
from text.manage_json import save_json


def menu_add(title, user):
    master = list(input(click.style('file_', fg='green')))
    json = add_file(master, genCode(), title, user)
    save_json(json)


def menu_read(title, user):
    click.echo(read_file(title, user))


def menu_edit(title, user):
    click.echo(read_file(title, user))
    newText = input('newfile_')
    edit_file(newText, title, user)


def menu_delete(title,user):
    click.echo(read_file(title, user))
    if input('d_to_delete_') == 'd':
        edit_file('', title, user)

