from service.text.generator import genCode, genTitle
from service.text.swap import swap


def add(master, password=genCode(), title=genTitle()):

    master = swap(master, password)

    return {'code': [{'title': title, 'file': master}]}
