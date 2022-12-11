
from service.text.get_key import get_key
from service.managejson import *
from service.features.add import add


def edit(master, title, user):
    
    key = get_key(title, user)

    json = add(master, key, title, user)

    save_json(json, replace=True)
