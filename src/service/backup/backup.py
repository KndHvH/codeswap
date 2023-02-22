import os
import click
import shutil
from dataclasses import dataclass
from tkinter import filedialog as fd
from src.helper.app import AppHelper
from src.service.database.repository import Repository
from src.helper.date import DateHelper



desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
scriptPath = os.path.dirname(__file__)


@dataclass
class BackupDatabase():
    app = AppHelper()

    DATABASE_PATH: str = app.db_path
    FILE_TYPES: tuple = (('json file', '*.json'), ('All files', '*.*'))

    @staticmethod
    def _get_backup_path():
        return fd.askopenfilename(
            title='load the backup',
            initialdir=desktop,
            filetypes=BackupDatabase.FILE_TYPES
        )

    @staticmethod
    def _get_backup_foulder():
        return fd.askdirectory(title='select save foulder', initialdir=desktop)

    @staticmethod
    def _backup_overrite_warning() -> None:
        click.secho('Warning!', bg='yellow', fg='black')
        click.secho('if wan\'t to replace a more recent version with an older version', fg='yellow')
        click.secho('you must first delete the local version, use:', fg='yellow')
        click.secho('\'cs -d -t ~filename\'', fg='yellow')

    @staticmethod
    def save_backup_path():
        return fd.askdirectory(title='select save foulder', initialdir=desktop)

    @staticmethod
    def backup_database() -> None:
        filepath = os.path.join(scriptPath, BackupDatabase.DATABASE_PATH)
        shutil.copy(filepath, BackupDatabase._get_backup_foulder())

    @staticmethod
    def load_database():

        remote_file_list = Repository.get_json(path=BackupDatabase._get_backup_path())['code']
        local_file_list = Repository.get_json()['code']

        for remote_file in remote_file_list:
            append = True

            for local_file in local_file_list:
                if remote_file['title'] != local_file['title']:
                    continue

                BackupDatabase._backup_overrite_warning()

                if 'date' in remote_file:
                    if 'date' in local_file:
                        if DateHelper.remote_date_is_more_recent(local_file['date'],remote_file['date']):
                            continue

                    else: 
                        continue                

                append = False

            if append:
                local_file_list.append(remote_file)
            

        Repository.save_on_dbjson_file(local_file_list)

    @staticmethod
    def get_option():
        while True:
            try:
                option = click.prompt(click.style(
                    '(s)save or (l)load_', fg='blue'), prompt_suffix='').lower()

                if option != 's' and option != 'l':
                    raise ValueError

                return option
            except ValueError:
                click.secho('error!', bg='red', fg='white')
                click.echo('choose from \'s\' or \'l\'_')
