import random
import os


scriptPath = os.path.dirname(__file__)


class Code:

    def __init__(self, body, password) -> None:

        self.__id = self.__generateId()
        self.__title = self.__generateTitle()
        self.__body = self.swap(body, password)

    def __str__(self) -> str:
        return f'{self.__body}'

    def __generateId(self):
        with open(os.path.join(scriptPath, 'service/id.txt'), "r+") as file:
            id = int(file.read())
            file.seek(0)
            file.write(str(id+1))
            file.truncate()
        return id

    def __generateTitle(self):
        return random.randint(10000000, 99999999)

    def __generateFileName(self, name):

        name += self.__title

        relPath = 'database/'+str(name)+'.txt'
        return (os.path.join(scriptPath, relPath))

    def swap(self, body: str, password: str) -> str:
        master = list(body)

        step = int(len(password)/4)

        for i, v in enumerate(master):
            for j, b in enumerate(password):
                if v == b:
                    if j < step or (j >= 2*step and j < 3*step):
                        master[i] = password[j+step]
                    else:
                        master[i] = password[j-step]
        return listToString(master)

    def saveBody(self):

        title = input('file title_')
        titleNumber = letterToNumber(title)
        filename = self.__generateFileName(titleNumber)
        filepath = os.path.join(scriptPath, filename)
        with open(filepath, "w") as file:
            file.write(str(self))

        self.saveHead(titleNumber)

    def saveHead(self, titleNumber):
        filepath = os.path.join(scriptPath, 'service/titles.txt')

        try:
            with open(filepath, "r") as file:
                file_list = []
                for line in file:
                    file_list.append(line)

        except FileNotFoundError:
            file_list = []

        file_list.append(titleNumber)
        with open(filepath, "w") as file:
            for line in file_list:

                line = str(line)

                file.write(f'{line}\n')


def main():

    while True:

        choice = decision()

        match choice:

            case 'a':

                master = list(input('file_'))
                password = passwordVerif()

                code = Code(master, password)

                code.saveBody()

            case 'r':
                filename = input('filename_')

                filename = letterToNumber(filename)

                masterList = importData(filename+)
                password = input('password_')

                message = Code.swap(masterList, password)

                print(master)

            case 'q':
                break


def decision() -> str:
    while True:
        try:
            print('a_ add | r_ read')
            choice = input("_").lower()

            if choice != 'a' and choice != 'r' and choice != 'q':
                raise ValueError

            return choice

        except ValueError:
            print("error!")


def passwordVerif() -> str:
    while True:
        try:
            password = input("password_").lower()

            if len(password) % 2 != 0:
                print('password size can\'t be even.')
                raise ValueError

            if len(password) < 4:
                print('password too small.')
                raise ValueError

            if hasDouble(password):
                print('password can\'t have repeated chars.')
                raise ValueError    

            upper = password.upper()
            password = password + upper
            return password

        except ValueError:
            print('error!')


def hasDouble(string: str) -> bool:
    stringlist = list(string)

    if len(stringlist) != len(set(stringlist)):
        return True
    return False


def listToString(list: list) -> str:
    string = ""
    for i in list:
        string += i
    return string


def importData(title) -> list:
    try:
        with open('database/' + title + '.txt', "r") as db:
            dbList = []
            for line in db:
                dbList.append(eval(line))

    except FileNotFoundError:
        print('file not found')
        dbList = []

    return dbList


def letterToNumber(name: str) -> int:

    equiv = {'a': '01', 'b': '02', 'c': '03', 'd': '04', 'e': '05', 'f': '06', 'g': '07', 'h': '08', 'i': '09', 'j': '10',
             'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20',
             'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25', 'z': '26'}

    number = []

    for letter in name:
        number.append(equiv.get(letter))

    return int(listToString(number))


if __name__ == '__main__':
    main()
