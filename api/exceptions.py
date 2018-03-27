from flask import jsonify


class BaseException(Exception):
    status_code = 500

    def __init__(self, message, payload=None):
        Exception.__init__(self)
        self.message = message
        self.payload = payload

    def to_json(self):
        return jsonify(self.message)


class BadRequest(BaseException):
    status_code = 400


class Unauthorized(BaseException):
    status_code = 401


class Forbidden(BaseException):
    status_code = 403


class NotFound(BaseException):
    status_code = 404


class BusinesError(BaseException):
    status_code = 422
