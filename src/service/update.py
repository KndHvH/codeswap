import subprocess
import os
import requests as req
import click

from src.service.version import get_version



def update():


    subprocess.run(["pip", "install", "codeswap"])
    subprocess.run(["pip", "install", "codeswap"])

    click.secho('app updated successfully', bg='blue', fg='white')
    

def update_verif():
    try:
        new = req.get("https://kndhvh.github.io/codeswap.json").json()['codeswap']

        if new != get_version():

            want_update(new)
    except:
        pass


def want_update(new):

    click.secho('new version avaliable:', bg='blue', fg='white')
    click.secho(f'remote: v{new}')
    click.secho(f'local: v{get_version()}')
    if click.confirm(click.style('want to update?'), prompt_suffix=''):
        update(new)
