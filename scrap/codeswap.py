
import re


def main():

    while True:

        choice = decision()

        match choice:

            case 'a':
                master = list(input('file_'))
                password = password_verif()

                master = swap(master, password)

                saveData(str(master))
            
            case 's':
                master = list(importData())
                password = input('password_')

                master = swap(master, password)

                print(master)

            case 'q':
                break
            


def decision() -> str:
    while True:
        try:
            print('a_ add | s_ swap')
            choice = input("_").lower()

            if choice != 'a' and choice != 's' and choice != 'q':
                raise ValueError

            return choice

        except ValueError:
            print("error!")


def password_verif() -> str:
    while True:
        try:
            password = input("password_").lower()

            if len(password) % 2 != 0:
                print('password size can\'t be even.')
                raise ValueError

            if len(password) < 4:
                print('password too small.')
                raise ValueError

            if re.search('\W', password):
                print('password can only contain letters.')
                raise ValueError

            if has_double(password):
                print('password can\'t have repeated letters.')
                raise ValueError

            upper = password.upper()
            password = password + upper
            return password

        except ValueError:
            print('error!')


def has_double(string: str) -> bool:
    stringlist = list(string)

    if len(stringlist) != len(set(stringlist)):
        return True
    return False


def swap(master: list, senha: list) -> list:
    step = int(len(senha)/4)

    for i, v in enumerate(master):
        for j, b in enumerate(senha):
            if v == b:
                if j < step or (j >= 2*step and j < 3*step):
                    master[i] = senha[j+step]
                else:
                    master[i] = senha[j-step]
    return master


def list_to_string(list: list) -> str:
    string = ""
    for i in list:
        string += i
    return string


def saveData(message: str):
    with open("coded.txt", "w") as file:
        file.write('message')


def importData() -> str:
    with open("coded.txt", "r") as file:
        return file


if __name__ == '__main__':
    main()
