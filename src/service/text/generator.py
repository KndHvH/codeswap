import random
from src.service.text.title_checker import title_verif


def genCode() -> str:
    alphPool = 'abcdefghijklmnopqrstuvwxyz'  # 26
    numPool = '0123456789!@#$%^&*\-,.?:;<>+_\'\"()\n/ '  # 32
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

        pool = pool[0:3]

        pool = ''.join(pool)

        if title_verif(pool):
            return pool
