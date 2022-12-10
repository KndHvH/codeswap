
from service.decision import decision
from service.features.add import add
from service.features.read import read
from service.features.edit import edit
from service.managejson import *
from service.text.generator import genCode
from service.login import login


def main():
    user = login()
    while True:

        choice = decision()

        match choice:

            case 'a':
                master = list(input('file_'))
                title = input('file title_')
                json = add(master, genCode(), title, user)
                save_json(json)

            case 'r':
                title = input('title_')
                print(read(title, user))

            case 'e':
                title = input('title_')
                print(read(title, user))
                newText = input('newfile_')
                edit(newText, title, user)

            case 'd':
                title = input('title_')
                print(read(title, user))
                if input('d_to_delete_') == 'd':
                    edit('', title, user)

            case 'q':
                break


if __name__ == '__main__':
    main()
