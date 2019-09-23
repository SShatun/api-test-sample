from datetime import date


def response_handler(response, symbols: list = None, response_date=None, base='EUR'):
    if not response_date:
        response_date = str(date.today())
    if not isinstance(response_date, str):
        response_date = str(response_date)
    assert response['success']
    assert response['base'] == base
    assert response['date'] == str(response_date)
    assert response['timestamp']
    if symbols:
        assert set(response['rates']) == set(symbols)
    for _, value in response['rates'].items():
        assert value > 0
