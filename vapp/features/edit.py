
from service.text.get_key import get_key
from service.text.manage_json import *
from service.features.add import add_file


def edit_file(master, title, user):

    key = get_key(title, user)

    json = add_file(master, key, title, user)

    save_json(json, replace=True)
