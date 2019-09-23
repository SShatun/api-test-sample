def invalid_date(response):
    assert not response['success']
    assert response['error']['code'] == 302
    assert response['error']['type'] == 'invalid_date'


def access_restricted(response):
    assert not response['success']
    assert response['error']['code'] == 105
    assert response['error']['type'] == 'base_currency_access_restricted'


def invalid_currency_codes(response):
    assert not response['success']
    assert response['error']['code'] == 202
    assert response['error']['type'] == 'invalid_currency_codes'


def invalid_access_key(response):
    assert not response['success']
    assert response['error']['code'] == 101
    assert response['error']['type'] == 'invalid_access_key'


def missing_access_key(response):
    assert not response['success']
    assert response['error']['code'] == 101
    assert response['error']['type'] == 'missing_access_key'


def no_rates_available(response):
    assert not response['success']
    assert response['error']['code'] == 106
    assert response['error']['type'] == 'no_rates_available'
