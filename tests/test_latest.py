import allure
import pytest

from framework.client import Client
from framework.verification import error_handlers as check_error
from framework.verification.response_handlers import response_handler


@allure.story('Latest without filers')
def test_latest():
    response = Client('/latest').get()
    response_handler(response)


@allure.story('Latest with currency code filers')
@pytest.mark.parametrize('symbols', ['RUB,USD', 'RUB,  USD', 'rub,usd'])
def test_symbols(symbols):
    response = Client('/latest').get({'symbols': symbols})
    response_handler(response, symbols=['RUB', 'USD'])


@allure.story('Latest with invalid currency codes')
@pytest.mark.parametrize('symbols', ['OMS', 'OMS, ACC', ','])
def test_invalid_symbols(symbols):
    response = Client('/latest').get({'symbols': symbols})
    check_error.invalid_currency_codes(response)


@allure.story('Latest with one valid and one invalid currency codes')
def test_valid_and_invalid_symbols():
    response = Client('/latest').get({'symbols': 'OMS,RUB'})
    response_handler(response, symbols=['RUB'])


@allure.story('Latest with one valid and one invalid currency codes')
def test_empty_symbols():
    response = Client('/latest').get({'symbols': ''})
    response_handler(response)


@allure.story('Latest with empty currency code filer')
def test_invalid_access_key():
    response = Client('/latest', access_key='invalid').get()
    check_error.invalid_access_key(response)


def test_without_access_key():
    client = Client('/latest')
    client.access_key = None
    response = client.get()
    check_error.missing_access_key(response)
