import datetime


class DateHelper():

    @staticmethod
    def get_date():
        return datetime.datetime.now()
        # 2023-02-22 13:21:51.475524

    @staticmethod
    def formate_date(date):
        return date.strftime("%H:%M:%S %d-%m-%Y")
        # 13:21:51 22-02-2023

    @staticmethod
    def remote_date_is_more_recent(local_date, remote_date) -> bool:
        if isinstance(local_date, str):
            local_date = DateHelper.str_to_datetime(local_date)

        if isinstance(remote_date, str):
            remote_date = DateHelper.str_to_datetime(remote_date)

        return remote_date > local_date

    @staticmethod
    def str_to_datetime(date_str: str) -> datetime.datetime:
        return datetime.datetime.strptime(date_str, '%H:%M:%S %d-%m-%Y')

        

