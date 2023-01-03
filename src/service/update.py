import subprocess
import os
import requests as req
import click

from src.service.version import version_number


def update(new):

    wd = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    os.chdir('...')

    subprocess.run(["git", "fetch"])
    subprocess.run(["git", "pull"])
    subprocess.run(["pip", "install", "-e", "."])

    os.chdir(wd)

    if new == version_number():
        click.secho('app updated successfully', bg='blue', fg='white')
    else:
        click.secho('app update failed', bg='red', fg='white')

def update_verif():
    new = req.get("https://kndhvh.github.io/codeswap.json").json()['codeswap']

    if new != version_number():

        want_update(new)


def want_update(new):

    click.secho('new version avaliable:', bg='blue', fg='white')
    click.secho(f'remote: v{new}')
    click.secho(f'local: v{version_number()}')
    if click.confirm(click.style('want to update?'), prompt_suffix=''):
        update(new)
