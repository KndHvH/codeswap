

from src.service.listpool import gen_str_to_num_dict


def str_to_int(text: str) -> int:

    result = []

    pool = gen_str_to_num_dict()

    for letter in text:

        result.append(str(pool.get(letter, letter)))

    return ''.join(result)


