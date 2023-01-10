import subprocess
import os
import requests as req
import click

from src.helper.app import AppHelper
app = AppHelper()


class UpdateApp():

    def __init__(self) -> None:
        try:
            new = req.get(
                "https://kndhvh.github.io/codeswap.json").json()['codeswap']

            if new != app.version:

                self.__want_update(new)
        except:
            pass

    def __want_update(self, new):

        click.secho('new version avaliable:', bg='blue', fg='white')
        click.secho(f'remote: v{new}')
        click.secho(f'local: v{app.version}')
        if click.confirm(click.style('want to update?'), prompt_suffix=''):
            self.__update(new)

    def __update(self, new):

        subprocess.run(["pip", "install", "codeswap"])
        subprocess.run(
            ["pip", "install", f"codeswap=={new}"])

        click.secho('app updated successfully', bg='blue', fg='white')
