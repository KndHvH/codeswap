
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
        t = input(click.style('file title_', fg='green'))
    menu_add(t, login())


@main.command()
@click.option('-t', default=None, help='file title')
def read(t):
    if not t:
        t = input(click.style('file title_', fg='green'))
    menu_read(t, login())


@main.command()
@click.option('-t', default=None, help='file title')
def edit(t):
    if not t:
        t = input(click.style('file title_', fg='green'))
    menu_edit(t, login())


@main.command()
@click.option('-t', default=None, help='file title')
def delete(t):
    if not t:
        t = input(click.style('file title_', fg='green'))
    menu_delete(t, login())
