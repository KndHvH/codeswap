
from service.text.swap import swap
from service.bin import *


def add(master, password, title, user):
    
    master = swap(master, password)

    password = ':' + password

    return {'title': title, 'user': user*int(bin_to_count(code_to_bin(password))),'file': master}
