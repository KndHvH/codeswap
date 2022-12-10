
from service.text.swap import swap


def add(master, password, title):

    print(f'key_{title}:{password}_')

    master = swap(master, password)

    return {'title': title, 'file': master}
