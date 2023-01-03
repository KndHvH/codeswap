

from src.service.get_key import get_key
from src.service.manage_json import get_file
from src.service.swap import swap


def get_file_text(title, user):
    key = get_key(title, user)
    if key != None:

        file = get_file(title)

        return swap(file, key)
