
from src.service.text.swap import swap
from src.service.text.get_key import get_key
from src.service.text.manage_json import *


def read_file(title, user):
    key = get_key(title, user)
    if key != None:

        file = get_file(title)

        return swap(file, key)
