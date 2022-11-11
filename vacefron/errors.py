from __future__ import annotations
from typing import TYPE_CHECKING, Any, Tuple

if TYPE_CHECKING:
    from aiohttp import ClientResponse


__all__: Tuple[str, ...] = (
    "VacEfronException",
    "BadRequest",
    "NotFound",
    "InternalServerError",
    "Forbidden",
    "HTTPException",
)


class VacEfronException(Exception):
    pass


class BadRequest(VacEfronException):
    pass


class NotFound(VacEfronException):
    pass


class Forbidden(VacEfronException):
    pass


class InternalServerError(VacEfronException):
    pass


class HTTPException(VacEfronException):
    def __init__(self, response: ClientResponse, message: Any):
        self.response = response
        self.status = response.status
        self.message = message
