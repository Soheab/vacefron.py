# source: https://github.com/BlistBotList/blist-wrapper/blob/bc0c0fe9afbea39993ccfa8b6d633c2b5be634c8/blist/errors.py


class VacEfronException(Exception):
    pass


class BadRequest(VacEfronException):
    pass


class NotFound(VacEfronException):
    pass


class InternalServerError(VacEfronException):
    pass


class HTTPException(VacEfronException):
    def __init__(self, response, message):
        self.response = response
        self.status = response.status
        self.message = message
