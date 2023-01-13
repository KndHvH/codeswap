import itertools


class BinaryHelper():

    @staticmethod
    def code_to_binary(code) -> str:
        return ''.join(format(ord(i), '08b') for i in code)

    @staticmethod
    def binary_to_code(binary) -> str:
        binary_decoded = [binary[i:i+8] for i in range(0, len(binary), 8)]
        return "".join([chr(int(decoded, 2)) for decoded in binary_decoded])

    @staticmethod
    def count_to_binary(count) -> str:

        count = str(count).split('0')
        result = []

        for i, j in itertools.zip_longest(count[0], count[1]):
            result.append(int(i)*'0') if i != None else None
            result.append(int(j)*'1') if j != None else None

        return ''.join(result)

    @staticmethod
    def binary_to_count(binary) -> str:
        result = []

        byte = binary[0]
        count = 0
        try:
            for i, v in enumerate(binary):
                if v == byte:
                    count += 1
                else:
                    result.append(f'{count}{byte}')
                    byte = v
                    count = 1
                if v == binary[i+1]:
                    pass
        except IndexError:
            result.append(f'{count}{byte}')

        return BinaryHelper.group_binary_count(result)

    @staticmethod
    def group_binary_count(binary_data) -> str:
        zeros = []
        non_zeros = []

        for i in binary_data:
            if '0' == i[1]:
                zeros.append(i[0])
            else:
                non_zeros.append(i[0])

        grouped_zeros = ''.join(zeros)
        grouped_non_zeros = ''.join(non_zeros)

        return grouped_zeros + '0' + grouped_non_zeros
