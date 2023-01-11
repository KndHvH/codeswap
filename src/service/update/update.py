import subprocess
import os
import requests as req
import click

from src.helper.app import AppHelper
app = AppHelper()


class UpdateApp():

    def __init__(self) -> None:
        try:
            remote_version = self.__get_remote_version()

            if self.__match_version(remote_version):
                self.__ask_update(remote_version)

        except:
            pass

    def __match_version(self,new_version) -> bool:

        if 'beta' in app.version: return False

        new_version = new_version.split('.')
        local_version = app.version.split('.')

        for index, _ in enumerate(new_version):
            if int(new_version[index]) > int(local_version[index]): return True
            if int(new_version[index]) < int(local_version[index]): return False
        
        return False

    def __ask_update(self, new):

        click.secho('new version avaliable:', bg='blue', fg='white')
        click.secho(f'remote: v{new}')
        click.secho(f'local: v{app.version}')
        if click.confirm(click.style('want to update?'), prompt_suffix=''):
            self.__update(new)

    def __update(self, new):

        subprocess.run(["pip", "install", "codeswap"])
        subprocess.run(["pip", "install", f"codeswap=={new}"])
        click.secho('app updated successfully', bg='blue', fg='white')

    def __get_remote_version(self):
        return req.get("https://kndhvh.github.io/codeswap.json").json()['codeswap']
