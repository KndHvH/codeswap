from tkinter import filedialog as fd
import shutil
import os
import click

from service.text.manage_json import get_json, save_on_dbjson_file
desktop = os.path.normpath(os.path.expanduser("~/Desktop"))
scriptPath = os.path.dirname(__file__)


def get_backup_path():
    filetypes = (
        ('json file', '*.json'),
        ('All files', '*.*')
    )

    filepath = fd.askopenfilename(
        title='load the backup',
        initialdir=desktop,
        filetypes=filetypes)

    return filepath


def get_save_backup_path():
    return fd.askdirectory(title='select save foulder',initialdir=desktop)


def backup_database():

    path = get_save_backup_path()

    relPath = '../../database/db.json'
    filepath = os.path.join(scriptPath, relPath)

    shutil.copy(filepath,path)



def load_database():
    remote_file_list = get_json(path=get_backup_path())['code']

    local_file_list = get_json()['code']

    for remote_file in remote_file_list:
        append = True
        warning = False

        for local_file in local_file_list:
            if remote_file['title'] == local_file['title']:
                append = False
                warning = True

        if append:
            local_file_list.append(remote_file)

    if warning:
        click.secho('if you want to replace an local file content,', bg='yellow', fg='white')
        click.secho('you must first delete the local version, use', bg='yellow', fg='white')
        click.secho('\'cswap delete -t ~filename\'', bg='yellow', fg='white')
        
    save_on_dbjson_file(local_file_list)



