import json
from http import HTTPStatus

import requests
from allure_commons._allure import step, attach
from allure_commons.types import AttachmentType
from requests import Response as RequestsResponse
from vyper import v as config


def _dump(obj):
    return json.dumps(obj, indent=4, sort_keys=True, ensure_ascii=False)


def _dump_headers(headers):
    dict_headers = dict(headers.items())
    return _dump(dict_headers)


def _attach_response(response: RequestsResponse):
    response_json = None
    try:
        response_json = response.json()
    except ValueError:
        pass
    with step(f"{response.request.method}: {response.request.url}"):
        attach(_dump_headers(response.request.headers), 'request.headers', AttachmentType.TEXT)

    with step(f"response → {response.status_code}"):
        if response_json:
            attach(_dump(response_json), 'response.json', AttachmentType.JSON)
        if response.text:
            attach(response.text, 'response.text', AttachmentType.TEXT)
        attach(_dump_headers(response.headers), 'response.headers', AttachmentType.JSON)


class Client:

    def __init__(self, path='latest', access_key: str = None):
        self.headers = {}
        self.path = path
        self.host = config.get('host')
        self.access_key = access_key or config.get('access_key')

    def get(self, params: dict = None, status_code: int = HTTPStatus.OK, **kwargs):
        """Base GET request method"""
        url = f'{self.host}{self.path}'
        if params is None:
            params = {}
        params['access_key'] = self.access_key
        response = requests.get(url, params=params, **kwargs)
        _attach_response(response)
        assert response.status_code == status_code
        if status_code == HTTPStatus.OK:
            return response.json()
        else:
            return response

    def post(self):
        """Base POST request method"""
