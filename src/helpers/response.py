import json

__all__ = ['response']


def response(data={}, status_code=200, headers={}):
    return json.dumps(data), status_code, {'Content-Type': 'application/json', **headers}
