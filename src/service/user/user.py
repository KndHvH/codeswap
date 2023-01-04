


from src.service.manage_json import get_json


def is_new_user():
    file = get_json()['code']

    if file == []:
        return True
    return False