from service.text.generator import genCode, genTitle
from service.text.swap import swap


def add(master, password=genCode(), title=genTitle()):

    print(f'key_{title}:{password}_')

    master = swap(master, password)

    return {'code': [{'title': title, 'file': master}]}
