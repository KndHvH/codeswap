
import click
import os

from service.features.read import read_file
from service.features.edit import edit_file
from service.text.manage_json import get_json

from service.login import login
from service.update import update_verif
from service.version import version_number

update_verif()


@click.group()
def main():
    """codeswap:

    \b
    create or edit your file with the 'file' command.
    delete your files with the 'delete' command.
    you can use the '-t' option to input the file title through the terminal.


    """
    pass


@main.command(short_help='create or edit a file')
@click.option('-t', default=None, help='file title')
def file(t):
    if not t:
        t = click.prompt(click.style(
            'file title_', fg='blue'), prompt_suffix='')
    edit_file(t, login())


@main.command(short_help='delete a file')
@click.option('-t', default=None, help='file title')
def delete(t):
    if not t:
        t = click.prompt(click.style(
            'file title_', fg='blue'), prompt_suffix='')
    click.echo(read_file(t, login()))

    if click.confirm(click.style('confirm delete?', bg='red', fg='white'), prompt_suffix=''):
        edit_file(t, login(), delete=True)


@main.command(short_help='list all files titles')
def list():
    click.secho('titles_', fg='blue')

    files = get_json()['code']

    for file in files:
        click.echo(file['title'])


@main.command(short_help='show current version')
def version():

    click.echo(f'install dir: {os.path.dirname(__file__)}')
    click.echo(f'v{version_number()}')
