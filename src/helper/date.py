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
        return remote_date > local_date



# today = DateHelper.get_date()
# print(type(today))

# old = datetime.datetime(2021, 1, 1,11,0,12)
# print(old)


# today = DateHelper.formate_date(today)
# print(type(today))

# old = DateHelper.formate_date(old)
# print(old)


# print(DateHelper.remote_date_is_more_recent(old,today))

