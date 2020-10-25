from enum import Enum
from io import BytesIO
from re import search
from typing import Union

from aiohttp import ClientSession

from .errors import BadRequest


class Image:
    def __init__(self, url: str, session) -> None:
        self.url: str = url
        self.session: ClientSession = session

    def __str__(self) -> str:
        return self.url if self.url is not None else ""

    async def read(self, bytesio = True) -> Union[bytes, BytesIO]:
        _bytes = await (await self.session.get(str(self.url))).read()
        if bytesio is False:
            return _bytes

        return BytesIO(_bytes)


class RankCard:
    __slots__ = (
        "_session",
        "username",
        "avatar",
        "level",
        "rank",
        "current_xp",
        "next_level_xp",
        "previous_level_xp",
        "custom_background",
        "xp_color",
        "is_boosting",
        )

    def __init__(
            self,
            _session: ClientSession,
            username: str,
            avatar: str,
            level: int,
            rank: int,
            current_xp: int,
            next_level_xp: int,
            previous_level_xp: int,
            custom_background: str = None,
            xp_color: str = None,
            is_boosting: bool = False,
            ) -> None:
        self._session: ClientSession = _session
        self.username: str = username
        self.avatar: str = avatar
        self.level: int = level
        self.rank: int = rank
        self.current_xp: int = current_xp
        self.next_level_xp: int = next_level_xp
        self.previous_level_xp: int = previous_level_xp
        self.custom_background: str = custom_background
        self.xp_color: str = xp_color
        self.is_boosting: bool = is_boosting

    def __str__(self) -> str:
        return f"https://vacefron.nl/api/rankcard{self.create_rank_card}"

    async def read(self, bytesio = True) -> Union[bytes, BytesIO]:
        _bytes = await (await self._session.get(str(self))).read()
        if bytesio is False:
            return _bytes

        return BytesIO(_bytes)

    @property
    def create_rank_card(self) -> str:
        params = (
            f"?username={self.username}"
            f"&avatar={self.avatar}"
            f"&level={self.level}"
            f"&rank={self.rank}"
            f"&currentxp={self.current_xp}"
            f"&nextlevelxp={self.next_level_xp}"
            f"&previouslevelxp={self.previous_level_xp}"
        )

        if self.custom_background is not None:
            params += f"&custombg={self.custom_background}"

        if self.xp_color is not None:
            if not search(r"^(?:[0-9a-fA-F]{3}){1,2}$", str(self.xp_color)):
                raise BadRequest(
                        "Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)"
                        )
            else:
                params += f"&xpcolor={self.xp_color}"

        if self.is_boosting:
            params += f"&isboosting=true"

        return params


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
