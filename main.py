
from service.features.decision import decision
from service.features.add import add
from service.features.read import read
from service.features.edit import edit
from service.json.managejson import *


def main():
    while True:

        choice = decision()

        match choice:

            case 'a':
                master = list(input('file_'))
                json = add(master)
                save_json(json)

            case 'r':
                key = input('key_')
                print(read(key))

            case 'e':
                key = input('key_')
                print(read(key))
                newText = input('newfile_')
                edit(newText, key)

            case 'd':
                key = input('key_')
                print(read(key))
                if input('d_to_delete_') == 'd':
                    edit('', key)

            case 'q':
                break


if __name__ == '__main__':
    main()
