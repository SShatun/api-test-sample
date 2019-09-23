import allure
import pytest

from framework.client import Client
from framework.verification import error_handlers as check_error
from framework.verification.response_handlers import response_handler


@allure.story('Request with base parameter. Valid access key')
@pytest.mark.skip('Don\'t have valid access key')
def test_base_with_access():
    base = 'USD'
    response = Client('/latest').get({'base': base})
    response_handler(response, base=base)


@allure.story('Request with base parameter. Restricted access key')
def test_base_restricted_access():
    response = Client('/latest').get({'base': 'USD'})
    check_error.access_restricted(response)


@allure.story('Invalid access key')
def test_invalid_access_key():
    response = Client('/latest', access_key='invalid').get()
    check_error.invalid_access_key(response)


@allure.story('Without access key')
def test_without_access_key():
    client = Client('/latest')
    client.access_key = None
    response = client.get()
    check_error.missing_access_key(response)
