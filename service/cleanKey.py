def cleanKey(key: str) -> list:

    if ':' in key:
        key = key.split(':')

        if 'key_' in key[0]:
            key[0] = key[0][4:]

        if '_' in key[0]:
            key[0] = key[:-1]

        return key
    return None
