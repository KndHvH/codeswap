

def code_to_bin(code):
    return ''.join(format(ord(i), '08b') for i in code)


def bin_to_code(bin):
    # TODO
    pass


def bin_to_count(bin):

    result=[]
    byte = bin[0] #0
    count = 0
    try:    
        for i,v in enumerate(bin):
            if v == byte:
                count += 1
            else:
                result.append(f'{count}{byte}')
                byte = v
                count = 1
            if v == bin[i+1]:
                pass
    except IndexError:
        result.append(f'{count}{byte}')

    finally:
        a = []
        b = []
        for i in result:
            if '0' == i[1]:
                a.append(i[0])
            if '1' == i[1]:
                b.append(i[0])

        a = ''.join(a)
        b = ''.join(b)

        return a+'0'+b

def count_to_bin(count):
    # TODO
    pass