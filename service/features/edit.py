
from service.text.swap import swap
from service.text.splitKey import getKey
from service.json.managejson import *
from service.features.add import add


def edit(master, key):

    key = getKey(key)

    print(f'key_{key[0]}:{key[1]}_')

    json = add(master, key[1], key[0])
    
    save_json(json)
