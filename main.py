
import click


from service.menu_features import *
from service.login import login
from service.version import version_number


@click.group()
def main():
    pass


@main.command()
@click.option('-t', default=None, help='file title')
def add(t):
    if not t:
        t = click.prompt(click.style(
            'file title_', fg='blue'), prompt_suffix='')
    menu_add(t, login())


@main.command()
@click.option('-t', default=None, help='file title')
def read(t):
    if not t:
        t = click.prompt(click.style(
            'file title_', fg='blue'), prompt_suffix='')
    menu_read(t, login())


@main.command()
@click.option('-t', default=None, help='file title')
def edit(t):
    if not t:
        t = click.prompt(click.style(
            'file title_', fg='blue'), prompt_suffix='')
    menu_edit(t, login())


@main.command()
@click.option('-t', default=None, help='file title')
def delete(t):
    if not t:
        t = click.prompt(click.style(
            'file title_', fg='blue'), prompt_suffix='')
    menu_delete(t, login())


@main.command()
def list():
    click.secho('titles_', fg='blue')
    for title in menu_list_files():
        click.echo(title)


@main.command()
def version():
    click.echo(f'v{version_number()}')
