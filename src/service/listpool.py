

def get_letter_str():
    return 'abcdefghijklmnopqrstuvwxyz'


def get_letter_str_upper():
    return get_letter_str() + get_letter_str().upper()


def get_symbol_str():
    return '0123456789!@#$%^&*\-,.?:;<>+_\'\"()\n/ '


def gen_str_to_num_dict():

    dict = {}

    for index, value in enumerate(list(get_letter_str_upper())):

        dict[value] = index
    
    return dict


