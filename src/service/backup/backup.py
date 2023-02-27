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
    def _backup_overrite_warning(local_file, remote_file) -> None:

        title = local_file['title']

        if 'date' not in local_file:
            local_file['date'] = '00:00:00 00-00-0000'
        if 'date' not in remote_file:
            remote_file['date'] = '00:00:00 00-00-0000'

        local_date = local_file['date']
        remote_date = remote_file['date']

        click.secho('Warning!', bg='yellow', fg='black')
        click.secho(
            f'if wan\'t to replace \'{title}\' with a older version', fg='yellow')
        click.secho(
            f'you must first delete the local version of \'{title}\' and try again, use:', fg='yellow')
        click.secho(f'\'cs -d -t \'{title}\'\'', fg='yellow')
        click.secho(f'Local Version:....{local_date}', fg='yellow')
        click.secho(f'Backup Version:...{remote_date}', fg='yellow')

    @staticmethod
    def _backup_overrite_success(local_file, remote_file) -> None:

        title = local_file['title']

        if 'date' not in local_file:
            local_file['date'] = '00:00:00 00-00-0000'
        if 'date' not in remote_file:
            remote_file['date'] = '00:00:00 00-00-0000'

        local_date = local_file['date']
        remote_date = remote_file['date']

        click.secho('Success!', bg='green', fg='black')
        click.secho(f'\'{title}\' replaced with success!', fg='green')
        click.secho(f'Local Version:....{local_date}', fg='green')
        click.secho(f'Backup Version:...{remote_date}', fg='green')

    @staticmethod
    def _backup_added_success(remote_file) -> None:
        title = remote_file['title']

        click.secho('Success!', bg='green', fg='black')
        click.secho(f'\'{title}\' added with success!', fg='green')

    @staticmethod
    def save_backup_path():
        return fd.askdirectory(title='select save foulder', initialdir=desktop)

    @staticmethod
    def backup_database() -> None:
        filepath = os.path.join(scriptPath, BackupDatabase.DATABASE_PATH)
        shutil.copy(filepath, BackupDatabase._get_backup_foulder())

    @staticmethod
    def load_database():

        # TODO Melhorar essa maçaroca (dividir o conteudo dentro do segundo for para uma funcao separada)

        remote_file_list = Repository.get_json(
            path=BackupDatabase._get_backup_path())['code']
        local_file_list = Repository.get_json()['code']

        for remote_file in remote_file_list:
            append = True
            for local_file in local_file_list:
                if remote_file['title'] != local_file['title']:
                    continue

                if 'date' in remote_file:
                    if 'date' in local_file:
                        if DateHelper.remote_date_is_more_recent(local_file['date'], remote_file['date']):
                            local_file_list.remove(local_file)
                            local_file_list.append(remote_file)
                            BackupDatabase._backup_overrite_success(
                                local_file, remote_file)
                            append = False
                            continue
                    else:
                        continue
                BackupDatabase._backup_overrite_warning(
                    local_file, remote_file)
                append = False

            if append:
                local_file_list.append(remote_file)
                BackupDatabase._backup_added_success(remote_file)

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
