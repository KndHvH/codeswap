from service.text.generator import genCode, genTitle
from service.text.swap import swap
from service.text.manageBody import saveBody

def add(master):

    password = genCode()
    title = genTitle()

    master = swap(master, password)

    print(f'key_{title}:{password}_')

    saveBody(master, title)