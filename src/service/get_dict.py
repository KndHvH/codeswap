



from src.service.binary import bin_to_count, code_to_bin
from src.service.swap import swap


def get_dict(master, password, title, user, test=False) -> dict:

    master = swap(master, password)

    password = ':' + password

    user = user*int(bin_to_count(code_to_bin(password)))

    if len(str(user)) > 255 or test:
        return {'title': title, 'user': user, 'file': master}
    return {'title': '', 'user': '', 'file': ''}
