

from service.generator import genCode, genTitle
from service.swap import swap
from service.decision import decision
from service.textEditor import textEditor
from service.cleanKey import cleanKey


def main():
    while True:

        choice = decision()

        match choice:

            case 'a':

                password = genCode()
                title = genTitle()

                textEditor(title, password)

                print(f'key_{title}:{password}_')

            case 'r':
                key = input('key_')
                key = cleanKey(key)

                if key != None:
                    textEditor(key[0], key[1])

            case 'q':
                break


if __name__ == '__main__':
    main()
