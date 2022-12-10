
from service.text.swap import swap
from service.text.get_key import get_key
from service.managejson import *


def read(title, user):
    key = get_key(title, user)
    if key != None:
        file = get_file(title)

        master = swap(file, key)

        return master
