
from service.features.decision import decision
from service.features.add import add
from service.features.read import read
from service.features.edit import edit


def main():
    while True:

        choice = decision()

        match choice:

            case 'a':
                master = list(input('file_'))
                add(master)

            case 'r':
                key = input('key_')
                read(key)

            case 'e':
                key = input('key_')
                read(key)
                newText = input('newfile_')
                edit(newText,key)

            case 'd':
                #TODO delete
                pass

            case 'q':
                break


if __name__ == '__main__':
    main()
