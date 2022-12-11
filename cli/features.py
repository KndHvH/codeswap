import click

from service.login import login
from service.features import add
from service.text.generator import genCode
from service.managejson import save_json

def a(user=None):
    if user == None:
        user = login()

    click.clear()
    master = list(input(click.style('file_', fg='green')))
    title = input(click.style('file_', fg='green'))
    json = add(master, genCode(), title, user)
    save_json(json)
