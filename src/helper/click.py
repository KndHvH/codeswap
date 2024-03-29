

import os
import click
from src.helper.app import AppHelper
from src.service.backup.backup import BackupDatabase
from src.service.database.repository import Repository
from src.service.user.login import login


class ClickHelper():

    @staticmethod
    def delete(t):
        t = Repository.get_file_title(t)

        click.echo(Repository.get_file_text(t, login()))

        if click.confirm(click.style('confirm delete?', bg='red', fg='white'), prompt_suffix=''):
            Repository.delete_file(t, login())

    @staticmethod
    def list_files():
        click.secho('titles_', fg='blue')

        files = Repository.get_json()

        sorted_files = sorted(files["code"], key=lambda x: x["title"])

        for file in sorted_files:

            if 'date' not in file:
                file['date'] = '00:00:01 01-01-1900'

            title_size = len(file['title'])
            i = 30 - title_size

            click.echo(file['title'] + i*'.' + file['date'])

    @staticmethod
    def info():
        app = AppHelper()

        click.echo(f'install dir: {os.path.dirname(__file__)}')
        click.echo(f'app version: v{app.version}')
        click.echo(f'repo: https://github.com/KndHvH/codeswap')

    @staticmethod
    def backup():
        option = BackupDatabase.get_option()

        match option:
            case 's':
                BackupDatabase.backup_database()
                click.secho('database saved successfully!',
                            bg='blue', fg='white')

            case 'l':
                BackupDatabase.load_database()
                click.secho('database loaded successfully!',
                            bg='blue', fg='white')

    @staticmethod
    def default(title):
        return Repository.edit_file(Repository.get_file_title(title), login())
