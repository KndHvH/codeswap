
import click

from service.text.generator import genCode
from service.features.add import add_file
from service.features.read import read_file
from service.features.edit import edit_file
from service.login import login
from service.managejson import save_json


@click.group()
def main():
    pass


@main.command()
@click.option('-t', default=None, help='file title')
def add(t):
    user = login()
    if t == None:
        t = input(click.style('file title_', fg='green'))

    master = list(input(click.style('file_', fg='green')))
    json = add_file(master, genCode(), t, user)
    save_json(json)


@main.command()
@click.option('-t', default=None, help='file title')
def read(t):
    user = login()
    if t == None:
        t = input(click.style('file title_', fg='green'))

    print(read_file(t, user))
    click.pause()


@main.command()
@click.option('-t', default=None, help='file title')
def edit(t):
    user = login()
    if t == None:
        t = input(click.style('file title_', fg='green'))


    print(read_file(t, user))
    click.pause()
    newText = input('newfile_')
    edit_file(newText, t, user)


@main.command()
@click.option('-t', default=None, help='file title')
def delete(t):
    user = login()
    if t == None:
        t = input(click.style('file title_', fg='green'))


    print(read_file(t, user))
    if input('d_to_delete_') == 'd':
        edit_file('', t, user)


if __name__ == '__main__':
    main()
