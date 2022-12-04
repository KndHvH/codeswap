
from service.text.swap import swap
from service.text.splitKey import getKey
from service.json.managejson import *


def read(key):
    key = getKey(key)

    if key != None:
        file = read_json(key[0])

        body = file['code'][0]['file']

        master = swap(body, key[1])

        return master
