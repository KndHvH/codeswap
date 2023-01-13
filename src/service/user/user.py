
import click

from src.service.database.repository import Repository


class NewUser():

    def __init__(self) -> None:
        if Repository.get_json()['code'] == []:
            self.__warning()

    def __warning(self):
        click.secho('Warning!', bg='yellow', fg='black')
        click.secho('project still under development', fg='yellow')
        click.secho(
            'don\'t save any data you can\'t afford to lose', fg='yellow')
        click.secho('see all comands with cs -h', fg='yellow')
