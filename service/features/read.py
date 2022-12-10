
from service.text.swap import swap
from service.text.get_key import get_key
from service.managejson import *


def read(key):
    key = get_key(key)

    if key != None:
        file = get_file(key[0])

        master = swap(file, key[1])

        return master
