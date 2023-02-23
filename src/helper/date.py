import datetime


class DateHelper():

    @staticmethod
    def get_date():
        return datetime.datetime.now()

    @staticmethod
    def formate_date(date):
        return date.strftime("%H:%M:%S %d-%m-%Y")

    @staticmethod
    def remote_date_is_more_recent(local_date, remote_date) -> bool:
        return True if remote_date > local_date else False


today = DateHelper.get_date()
print(today)

old = datetime.datetime(2021, 1, 1, 11, 0, 12)
print(old)


today = DateHelper.formate_date(today)
print(today)

old = DateHelper.formate_date(old)
print(old)


print(DateHelper.remote_date_is_more_recent(old, today))
