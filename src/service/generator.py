import random

from src.service.listpool import get_letter_str_upper, get_symbol_str

def genCode() -> str:

    pool = list(get_letter_str_upper() + get_symbol_str())

    random.shuffle(pool)

    pool = ''.join(pool)

    return pool
