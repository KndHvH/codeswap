import subprocess
import os
import requests as req
import click

from service.version import version_number


def update():

    wd = os.getcwd()
    os.chdir(os.path.dirname(__file__))
    os.chdir('..')

    subprocess.run(["git", "fetch"])
    subprocess.run(["git", "pull"])
    subprocess.run(["pip", "install", "-e", "."])

    os.chdir(wd)

    update_verif()


def update_verif():

    new = req.get("https://kndhvh.github.io/codeswap.json")
    
    new = new.json()['codeswap']

    current = version_number()

    if new != current:

        want_update(new)
    
    else:
        click.secho('app currently updated', bg='blue', fg='white')


def want_update(new):

    click.secho('new version avaliable:', bg='red', fg='white')
    click.secho(f'remote: v{new}')
    click.secho(f'local: v{version_number()}')
    if click.confirm(click.style('want to update?'), prompt_suffix=''):
        update()
