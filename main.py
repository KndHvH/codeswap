
import click

from service.decision import decision
from service.features.add import add_menu_option
from service.features.read import read
from service.features.edit import edit
from service.login import login

@click.command()
def main():
    user = login()
    while True:
        choice = decision()

        match choice:

            case 'a':
                add_menu_option(user)

            case 'r':
                title = input('title_')
                print(read(title, user))
                click.pause()

            case 'e':
                title = input('title_')
                print(read(title, user))
                click.pause()
                newText = input('newfile_')
                edit(newText, title, user)

            case 'd':
                title = input('title_')
                print(read(title, user))
                if input('d_to_delete_') == 'd':
                    edit('', title, user)

            case 'q':
                break


@click.command()
def a():
    print('test')
    add_menu_option()


if __name__ == '__main__':
    main()
