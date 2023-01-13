

class AppHelper():

    def __init__(self) -> None:
        self.__version = '1.2.1'
        self.__db_path = '../../database/db.json'
        self.__db_foulder_path = '../../database'
        self.__db_file_name = 'db.json'

    @property
    def version(self):
        return self.__version

    @property
    def db_path(self):
        return self.__db_path

    @property
    def db_foulder_path(self):
        return self.__db_foulder_path

    @property
    def db_file_name(self):
        return self.__db_file_name
