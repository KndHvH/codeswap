import click
import os
from src.service import get_file
from src.service.login import login
from src.service.backup import backup_database, load_database
from src.service.edit import edit_file
from src.service.manage_json import get_json
from src.service.tkinter import add_tkinter
from src.service.version import get_version
from src.service.update import update_verif
from src.service.user import is_new_user

add_tkinter()
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
    click.echo(get_file(t, login()))

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
    click.echo(f'v{get_version()}')


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