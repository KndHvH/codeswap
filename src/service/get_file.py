


from src.service import swap
from src.service.get_key import get_key


def get_file(title, user):
    key = get_key(title, user)
    if key != None:

        file = get_file(title)

        return swap(file, key)
