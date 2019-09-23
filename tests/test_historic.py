from datetime import date, datetime, timedelta

import allure
import pytest

from framework.client import Client
from framework.verification import error_handlers as check_error
from framework.verification.response_handlers import response_handler


@allure.story('Historic data')
@pytest.mark.parametrize('response_date', [date.today() - timedelta(1),
                                           date.today()],
                         ids=['yesterday', 'today'])
def test_historic(response_date):
    response = Client(str(response_date)).get()
    response_handler(response, response_date=response_date)


@allure.story('Historic data with symbols filter')
def test_symbols_historic():
    response_date = '2000-01-01'
    response = Client(response_date).get({'symbols': 'RUB'})
    response_handler(response, symbols=['RUB'], response_date=response_date)


@allure.story('Historic filtered by symbol with no data')
def test_historic_symbol_not_presents():
    response = Client('2000-01-01').get({'symbols': 'AOA'})
    check_error.no_rates_available(response)


@allure.story('Historic data by invalid date')
@pytest.mark.parametrize('response_date', [date.today() + timedelta(1),
                                           datetime.now(),
                                           date.today().strftime('%Y/%m/%d')],
                         ids=['future date', 'datetime', 'invalid format'])
def test_invalid_date(response_date):
    response = Client(str(response_date)).get()
    check_error.invalid_date(response)


@allure.story('Historic by date without any data')
def test_no_rates_available():
    response = Client(str(date.fromtimestamp(0))).get()
    check_error.no_rates_available(response)
