
import click


from service.menu.menu_features import *
from service.login import login


@click.group()
@click.option('-t', default=None, help='file title')
def main(t):
    if not t:
        t = input(click.style('file title_', fg='green'))


@main.command()
def add(t):
    menu_add(t, login())


@main.command()
def read(t):
    menu_read(t, login())


@main.command()
def edit(t):
    menu_edit(t, login())


@main.command()
def delete(t):
    menu_delete(t, login())
