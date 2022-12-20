
import click


from service.menu.menu_features import *
from service.login import login


@click.group()
def main():
    pass


@main.command()
@click.option('-t', default=None, help='file title')
def add(t):
    if not t:
        #TODO fix windows color, input to other method
        t = click.prompt(click.style('file title_', fg='blue'))
    menu_add(t, login())


@main.command()
@click.option('-t', default=None, help='file title')
def read(t):
    if not t:
        t = click.prompt(click.style('file title_', fg='blue'))
    menu_read(t, login())


@main.command()
@click.option('-t', default=None, help='file title')
def edit(t):
    if not t:
        t = click.prompt(click.style('file title_', fg='blue'))
    menu_edit(t, login())


@main.command()
@click.option('-t', default=None, help='file title')
def delete(t):
    if not t:
        t = click.prompt(click.style('file title_', fg='blue'))
    menu_delete(t, login())
