

def get_key(key):
    if ':' in key:
        key = key.split(':')

        if 'key_' in key[0]:
            key[0] = key[0][4:]

        if '_' in key[0]:
            key[0] = key[:-1]

        return key
    return None
