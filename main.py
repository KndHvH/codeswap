import click
import os
from src.service.database.repository import Repository
from src.service.user.login import login
from src.service.backup.backup import BackupDatabase
from src.service.database.repository import Repository
from src.service.modules.tkinter import AddTkinterClass
from src.service.update.update import UpdateApp
from src.service.user.user import NewUser
from src.helper.app import AppHelper

AddTkinterClass()
UpdateApp()
NewUser()


@click.command(short_help='create or edit a file')
@click.option('-t', '--title', default=None, help='file title')
@click.option('-d', 'command',  help='delete a file title',  flag_value='d')
@click.option('-l', 'command',  help='list all files',  flag_value='l')
@click.option('-v', 'command',  help='show app version',  flag_value='v')
@click.option('-b', 'command',  help='backup files',  flag_value='b')
def main(title, command):
    """codeswap:

    \b
    create or edit your files.
    delete your files with the '--delete' command.
    you can use the '--title' option to input the file title through the terminal.

    type=click.Choice(['save', 'load'], case_sensitive=False)
    """
    if not title:
        title = click.prompt(click.style(
            'file title_', fg='blue'), prompt_suffix='')

    Repository.edit_file(title, login())


def delete(t):
    if not t:
        t = click.prompt(click.style(
            'file title_', fg='blue'), prompt_suffix='')
    click.echo(Repository.get_file_text(t, login()))

    if click.confirm(click.style('confirm delete?', bg='red', fg='white'), prompt_suffix=''):
        Repository.delete_file(t, login())


def list():
    click.secho('titles_', fg='blue')

    files = Repository.get_json()['code']

    for file in files:
        click.echo(file['title'])


def version():
    app = AppHelper()

    click.echo(f'install dir: {os.path.dirname(__file__)}')
    click.echo(f'v{app.version}')


def backup(b):
    match b:
        case 'Save':
            BackupDatabase.backup_database()
            click.secho('database saved successfully!', bg='blue', fg='white')

        case 'Load':
            BackupDatabase.load_database()
            click.secho('database loaded successfully!', bg='blue', fg='white')
