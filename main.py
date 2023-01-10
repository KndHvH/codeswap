import click
import os
from src.service.database.repository import Repository
from src.service.user.login import login
from src.service.backup.backup import BackupDatabase
from src.service.database.repository import Repository
from src.service.modules.tkinter import AddTkinterClass
from src.service.update.update import UpdateApp
from src.service.user.user import NewUser

AddTkinterClass()
UpdateApp()
NewUser()
    


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
    Repository.edit_file(t, login())


@main.command(short_help='delete a file')
@click.option('-t', default=None, help='file title')
def delete(t):
    if not t:
        t = click.prompt(click.style(
            'file title_', fg='blue'), prompt_suffix='')
    click.echo(Repository.get_file_text(t, login()))

    if click.confirm(click.style('confirm delete?', bg='red', fg='white'), prompt_suffix=''):
        Repository.delete_file(t, login())


@main.command(short_help='list all files titles')
def list():
    click.secho('titles_', fg='blue')

    files = Repository.get_json()['code']

    for file in files:
        click.echo(file['title'])


@main.command(short_help='show current version')
def version():
    version = os.environ['VERSION']

    click.echo(f'install dir: {os.path.dirname(__file__)}')
    click.echo(f'v{version}')


@main.command(short_help='manage your db backup')
@click.option('-b', required=True, type=click.Choice(['Save', 'Load'], case_sensitive=False))
def backup(b):
    match b:
        case 'Save':
            BackupDatabase.backup_database()
            click.secho('database saved successfully!', bg='blue', fg='white')

        case 'Load':
            BackupDatabase.load_database()
            click.secho('database loaded successfully!', bg='blue', fg='white')
