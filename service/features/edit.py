
from service.text.swap import swap
from service.text.manageBody import saveBody
from service.text.splitKey import getKey

def edit(master, key):

    key = getKey(key)

    master = swap(master, key[1])

    print(f'key_{key[0]}:{key[1]}_')

    saveBody(master, key[0])