
import click

from service.text.generator import genCode
from service.features.add import add
from service.features.read import read
from service.features.edit import edit
from service.login import login
from service.managejson import save_json


@click.group()
def main():
    pass


@main.command()
def a():
    user = login()

    click.clear()
    master = list(input(click.style('file_', fg='green')))
    title = input(click.style('file title_', fg='green'))
    json = add(master, genCode(), title, user)
    save_json(json)


@main.command()
def r():
    user = login()

    title = input('title_')
    print(read(title, user))
    click.pause()


@main.command()
def e():
    user = login()
    title = input('title_')
    print(read(title, user))
    click.pause()
    newText = input('newfile_')
    edit(newText, title, user)


@main.command()
def d():
    user = login()
    title = input('title_')
    print(read(title, user))
    if input('d_to_delete_') == 'd':
        edit('', title, user)



if __name__ == '__main__':
   main()