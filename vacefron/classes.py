from enum import Enum
from io import BytesIO
from typing import Union, Optional

from aiohttp import ClientResponse


class Image:
    def __init__(self, url: str, response) -> None:
        self.url: str = url
        self._response: ClientResponse = response

    def __str__(self) -> str:
        return self.url if self.url is not None else ""

    async def read(self, bytesio = True) -> Union[bytes, BytesIO]:
        _bytes = await self._response.read()
        if bytesio is False:
            return _bytes

        return BytesIO(_bytes)


class RankCard:
    __slots__ = ("url", "_response", "_params", "username", "avatar", "current_xp", "next_level_xp", "previous_level_xp",
                 "level", "rank", "custom_background", "xp_color", "is_boosting", "circle_avatar")

    def __init__(self, url, response, params) -> None:
        self.url = url
        self._response: ClientResponse = response
        self._params: dict = params
        self.username: str = params.get("username")
        self.avatar: str = params.get("avatar")
        self.current_xp: int = params.get("currentxp")
        self.next_level_xp: int = params.get("nextlevelxp")
        self.previous_level_xp: int = params.get("previouslevelxp")
        self.level: Optional[int] = params.get("level", None)
        self.rank: Optional[int] = params.get("rank", None)
        self.custom_background: Optional[str] = params.get("custombg", None)
        self.xp_color: Optional[str] = params.get("xpcolor", None)
        self.is_boosting: bool = params.get("isboosting", False)
        self.circle_avatar: bool = params.get("circleavatar", False)

    def __str__(self) -> str:
        return str(Image(self.url, self._response))

    async def read(self, bytesio = True) -> Union[bytes, BytesIO]:
        return await (Image(self.url, self._response)).read(bytesio)


class CrewMateColors(Enum):
    BLACK = 1
    BLUE = 2
    BROWN = 3
    CYAN = 4
    DARKGREEN = 5
    DARK_GREEN = 5
    LIME = 6
    ORANGE = 7
    PINK = 8
    PURPLE = 9
    RED = 10
    WHITE = 11
    YELLOW = 12
    RANDOM = 13
