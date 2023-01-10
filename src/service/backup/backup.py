import os
import click
import shutil
from dataclasses import dataclass
from tkinter import filedialog as fd
from src.helper.app import AppHelper
from src.service.database.repository import Repository

desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
scriptPath = os.path.dirname(__file__)

@dataclass
class BackupDatabase():
    DATABASE_PATH : str = AppHelper.get_db_path()
    FILE_TYPES : tuple = ( ('json file', '*.json'), ('All files', '*.*') )

    def _get_backup_path(self) -> str:
        return fd.askopenfilename(
            title='load the backup', 
            initialdir=desktop,
            filetypes=self.FILE_TYPES
        )
    
    def _backup_overrite_warning(self) -> None:
            click.secho('Warning!', bg='yellow', fg='black')
            click.secho('if you want to replace an local file content', fg='yellow')
            click.secho('you must first delete the local version, use', fg='yellow')
            click.secho('\'cswap delete -t ~filename\'', fg='yellow')

    def save_backup_path(self) -> str:
        return fd.askdirectory(title='select save foulder',initialdir=desktop)

    def backup_database(self) -> None:
        filepath = os.path.join(scriptPath, self.DATABASE_PATH)
        shutil.copy(filepath, self._get_backup_path())

    def load_database(self):

        remote_file_list = Repository.get_json(path=self._get_backup_path())['code']
        local_file_list = Repository.get_json()['code']

        for remote_file in remote_file_list:
            append = True
            warning = False

            for local_file in local_file_list:
                if remote_file['title'] != local_file['title']: continue
                append = False
                warning = True

            if append:
                local_file_list.append(remote_file)

        if warning:
            self._backup_overrite_warning()
            
        Repository.save_on_dbjson_file(local_file_list)