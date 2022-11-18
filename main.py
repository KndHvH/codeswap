

from service.generator import genCode, genTitle
from service.swap import swap
from service.decision import decision
from service.manageBody import saveBody, getBody


def main():
    while True:

        choice = decision()

        match choice:

            case 'a':

                master = list(input('file_'))
                password = genCode()
                title = genTitle()

                master = swap(master, password)

                print(f'key_{title}:{password}_')

                saveBody(master, title)

            case 'r':
                key = input('key_')
                master = 'None'

                if ':' in key:
                    key = key.split(':')

                    if 'key_' in key[0]:
                        key[0] = key[0][4:]

                    if '_' in key[0]:
                        key[0] = key[:-1]

                    body = getBody(key[0])

                    master = swap(body, key[1])

                print(master)

            case 'q':
                break


if __name__ == '__main__':
    main()
