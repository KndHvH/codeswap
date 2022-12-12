
from text.swap import swap
from text.get_key import get_key
from text.manage_json import *


def read_file(title, user):
    key = get_key(title, user)
    if key != None:
        file = get_file(title)

        master = swap(file, key)

        return master
