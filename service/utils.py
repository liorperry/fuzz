import json

from flask import make_response

from model.ProgUnderTestStatus import ProgUnderTestStatus

JSON_MIME_TYPE = 'application/json'


def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ProgUnderTestStatus):
            return obj.toJSON()
        return json.JSONEncoder.default(self, obj)
