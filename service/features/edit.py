
from service.text.get_key import get_key
from service.managejson import *
from service.features.add import add


def edit(master, key):

    key = get_key(key)

    json = add(master, key[1], key[0])

    save_json(json)