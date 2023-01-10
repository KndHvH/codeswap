import subprocess
import os
import requests as req
import click

from src.helper.app import AppHelper


class UpdateApp():

    def __init__(self) -> None:
        try:
            new = req.get(
                "https://kndhvh.github.io/codeswap.json").json()['codeswap']

            if new != AppHelper.get_version():

                self.__want_update(new)
        except:
            pass

    def __want_update(self, new):

        click.secho('new version avaliable:', bg='blue', fg='white')
        click.secho(f'remote: v{new}')
        click.secho(f'local: v{AppHelper.get_version()}')
        if click.confirm(click.style('want to update?'), prompt_suffix=''):
            self.__update(new)

    def __update(self):

        subprocess.run(["pip", "install", "codeswap"])
        subprocess.run(
            ["pip", "install", f"codeswap=={AppHelper.get_version()[1:]}"])

        click.secho('app updated successfully', bg='blue', fg='white')
