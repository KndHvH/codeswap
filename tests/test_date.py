from src.helper import *

import pytest
import datetime

from src.service.database.repository import Repository
from src.helper.date import DateHelper


class TestClass:

    def test_remote_date_is_recent(self):

        expect = True

        remote = Repository.gen_dict('', '', 'test-1', str(200*'2'))
        # today

        local = Repository.gen_dict('', '', 'test-1', str(200*'2'), '14:45:41 22-02-2023')
        # old date

        # print(local)
        # print(type(local))
        # print(local['date'])
        # print(type(local['date']))
        # print('---')
        # print(remote)
        # print(type(remote))
        # print(remote['date'])
        # print(type(remote['date']))

        

        assert DateHelper.remote_date_is_more_recent(local['date'],remote['date'])

    def test_remote_date_is_older(self):


        local = Repository.gen_dict('', '', 'test-1', str(200*'2'),'14:45:41 22-02-2023')
        # recent

        remote = Repository.gen_dict('', '', 'test-1', str(200*'2'), '15:59:41 24-12-2000')
        # old date


        assert not DateHelper.remote_date_is_more_recent(local['date'],remote['date'])


    def test_get_date_formated(self):

        date = DateHelper.formate_date(datetime.datetime(2021, 1, 1,11,0,12))
        

        assert date == '11:00:12 01-01-2021'

    def test_get_date(self):

        date = DateHelper.get_date()

        assert isinstance(date, datetime.datetime)