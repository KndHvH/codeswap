
import click
import os
from service.backup.backup import backup_database, load_database

from service.features.read import read_file
from service.features.edit import edit_file
from service.text.manage_json import get_json

from service.login import login
from service.update import update_verif
from service.user import is_new_user
from service.version import version_number

update_verif()
if is_new_user():
    click.secho('Warning!', bg='yellow', fg='black')
    click.secho('project still under development', fg='yellow')
    click.secho('don\'t save any data you can\'t afford to lose', fg='yellow')

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


@main.command(short_help='manage your db backup')
@click.option('-b', required=True, type=click.Choice(['Save', 'Load'], case_sensitive=False))
def backup(b):
    match b:
        case 'Save':
            backup_database()
            click.secho('database saved successfully!', bg='blue', fg='white')

        case 'Load':
            load_database()
            click.secho('database loaded successfully!', bg='blue', fg='white')