
import random
import os


scriptPath = os.path.dirname(__file__)


def main():
    while True:

        choice = decision()

        match choice:

            case 'a':

                master = list(input('file_'))
                password = genCode()
                title = genTitle()

                master = swap(master, password)

                print(f'key_{title}:{password}')

                saveBody(master, title)

            case 'r':
                key = input('key_')
                master = 'None'

                if ':' in key:
                    key = key.split(':')

                    if 'key_' in key[0]:
                        key[0] = key[0][4:]

                    body = getBody(key[0])

                    master = swap(body, key[1])

                print(master)

            case 'q':
                break


def genCode() -> str:
    alphPool = 'abcdefghijklmnopqrstuvwxyz'  # 26
    numPool = '0123456789!@#$%^&*\-,.? '  # 24
    upperPool = alphPool.upper()  # 26

    pool = list(alphPool + upperPool + numPool)

    random.shuffle(pool)

    pool = ''.join(pool)

    return pool


def genTitle() -> str:

    while True:
        pool = ['ba', 'be', 'bi', 'bo', 'bu',
                'ca', 'ce', 'ci', 'co', 'cu'
                'da', 'de', 'di', 'do', 'du'
                'fa', 'fe', 'fi', 'fo', 'fu'
                'ga', 'ge', 'gi', 'go', 'gu'
                'la', 'le', 'li', 'lo', 'lu'
                'ma', 'me', 'mi', 'mo', 'mu'
                'pa', 'pe', 'pi', 'po', 'pu'
                'sa', 'se', 'si', 'so', 'su'
                'ta', 'te', 'ti', 'to', 'tu']

        random.shuffle(pool)

        pool = pool[0:5]

        pool = ''.join(pool)

        if titleVerif(pool):
            return pool


def titleVerif(title: str) -> bool:
    try:
        relPath = 'database/'+title+'.txt'
        filepath = os.path.join(scriptPath, relPath)
        with open(filepath, "r") as file:
            body = file.read()
        return False
    
    except FileNotFoundError:
        return True


def swap(body: str, password: str) -> str:
    master = list(body)

    step = int(len(password)/4)

    for i, v in enumerate(master):
        for j, b in enumerate(password):
            if v == b:
                if j < step or (j >= 2*step and j < 3*step):
                    master[i] = password[j+step]
                else:
                    master[i] = password[j-step]

    master = ''.join(master)
    return master


def saveBody(body: str, title: str):
    relPath = 'database/'+title+'.txt'
    filepath = os.path.join(scriptPath, relPath)
    with open(filepath, "w") as file:
        file.write(body)


def decision() -> str:
    while True:
        try:
            print('a_ add | r_ read')
            choice = input("_").lower()

            if choice != 'a' and choice != 'r' and choice != 'q':
                raise ValueError

            return choice

        except ValueError:
            print("error!")


def getBody(key) -> str:
    try:
        relPath = 'database/'+key+'.txt'
        filepath = os.path.join(scriptPath, relPath)
        with open(filepath, "r") as file:
            body = file.read()
        return body
    
    except FileNotFoundError:
        return 'None'


if __name__ == '__main__':
    main()
