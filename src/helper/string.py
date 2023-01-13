

import string
import random


class StringHelper():

    @staticmethod
    def get_symbol_str():
        return '0123456789!@#$%^&*\-,.?:;<>+_\'\"()\n/ '

    @staticmethod
    def convert_str_to_dict() -> dict:
        return {v: i for i, v in enumerate(string.ascii_letters)}

    @staticmethod
    def str_to_int(text: str) -> int:
        converted_string = []
        pool = StringHelper.convert_str_to_dict()

        for letter in text:
            converted_string.append(str(pool.get(letter, letter)))

        return int(''.join(converted_string))

    @staticmethod
    def swap(body: str, password: str) -> str:
        master = list(body)

        step = int(len(password)/4)

        for i, v in enumerate(master):
            for j, b in enumerate(password):
                if v == b:
                    if j < step or (j >= 2*step and j < 3*step):
                        master[i] = password[j+step]
                    else:
                        master[i] = password[j-step]

        master = ''.join(master)

        return master

    @staticmethod
    def genCode() -> str:

        pool = list(string.ascii_letters +
                    StringHelper.get_symbol_str())

        random.shuffle(pool)

        pool = ''.join(pool)

        return pool
