
from service.text.swap import swap
from service.text.splitKey import getKey
from service.json.managejson import *


def read(key):
    key = getKey(key)

    if key != None:
        file = get_file(key[0])

        master = swap(file, key[1])

        return master
