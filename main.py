
import click

from service.features.read import read_file
from service.features.edit import edit_file
from service.text.manage_json import get_json

from service.login import login
from service.version import version_number


@click.group()
def main():
    pass


@main.command()
@click.option('-t', default=None, help='file title')
def file(t):
    if not t:
        t = click.prompt(click.style(
            'file title_', fg='blue'), prompt_suffix='')
    edit_file(t, login())


@main.command()
@click.option('-t', default=None, help='file title')
def delete(t):
    if not t:
        t = click.prompt(click.style(
            'file title_', fg='blue'), prompt_suffix='')
    click.echo(read_file(t, login()))

    if click.confirm(click.style('confirm delete?', bg='red', fg='white'), prompt_suffix=''):
        edit_file(t, login(), delete=True)


@main.command()
def list():
    click.secho('titles_', fg='blue')

    files = get_json()['code']

    for file in files:
        click.echo(file['title'])


@main.command()
def version():
    click.echo(f'v{version_number()}')
