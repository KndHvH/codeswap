
from service.text.swap import swap
from service.text.manageBody import getBody
from service.text.splitKey import getKey


def read(key):

    key = getKey(key)

    if key != None:

        body = getBody(key[0])

        master = swap(body, key[1])

        print(master)
