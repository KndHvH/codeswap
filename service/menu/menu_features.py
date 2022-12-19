import click

from service.input import input_file
from service.text.generator import genCode
from service.features.add import add_file
from service.features.read import read_file
from service.features.edit import edit_file
from service.text.manage_json import save_json


def menu_add(title, user):

    json = add_file(input_file(), genCode(), title, user)
    save_json(json)


def menu_read(title, user):
    file = read_file(title, user)
    for line in file:
        click.echo(line)


def menu_edit(title, user):
    file = read_file(title, user)
    for line in file:
        click.echo(line)

    edit_file(input_file(), title, user)


def menu_delete(title, user):
    file = read_file(title, user)
    for line in file:
        click.echo(line)

    if input('d_to_delete_') == 'd':
        edit_file('', title, user)
