from __future__ import annotations
from typing import (
    TYPE_CHECKING,
    ClassVar,
    Dict,
    List,
    Optional,
    Tuple,
)


from ..enums import Badge, UnknownBadge

if TYPE_CHECKING:
    from .image import Image
    from ..types.rank import Rankcard as RankcardData

__all__: Tuple[str, ...] = ("Rankcard",)


class Rankcard:
    """Represents a rankcard.

    Parameters
    ----------
    username: :class:`str`
        The name of the user.
    avatar_url: :class:`str`
        The avatar url of the user.
    current_xp: :class:`int`
        The current XP of the user.
    next_level_xp: :class:`int`
        The XP required to level up.
    previous_level_xp: :class:`int`
        The XP required to level down.
    level: Optional[:class:`int`]
        The level of the user. Defaults to ``None``.
    rank: Optional[:class:`int`]
        The rank of the user. Defaults to ``None``.
    background: Optional[:class:`str`]
        The background of the rankcard. This can be a hex value or a url to an image.

        Defaults to ``None``.
    text_shadow_color: Optional[:class:`str`]
        The shadow color of the username as hex value. Defaults to ``None``.
    xp_colour: Optional[:class:`str`]
        The colour of the XP bar as hex value. Defaults to ``None``.
    circle_avatar: :class:`bool`
        Whether the avatar should be a circle or not. Defaults to ``False``.
    badges: List[:class:`Badges`]
        The badges to add to the rankcard.
        E.g. ``[Badges.NITRO, Badges.BOOST]``

        Defaults to an empty list.

    Attributes
    ----------
    Every parameter is also an attribute.

    url: :class:`str`
        The full url of the rankcard.
    unknown_badges: List[:class:`UnknownBadge`]
        Returns a list of unknown badges.
        
        These are badges that are not in the :class:`Badge` enum because they are possibly not added to this library yet.
        The api does nothing if unknown badges are passed to it.

        The objects returned have  a ``name`` attribute which is the name of the badge.
    """

    FRIENDLY_ATTR_NAMES: ClassVar[Dict[str, str]] = {
        "avatar": "avatar_url",
        "currentXp": "current_xp",
        "nextLevelXp": "next_level_xp",
        "previousLevelXp": "previous_level_xp",
        "customBg": "background",
        "textShadowColor": "text_shadow_color",
        "xpColor": "xp_color",
        "circleAvatar": "circle_avatar",
    }

    __slots__: Tuple[str, ...] = (
        "_image",
        "username",
        "avatar_url",
        "current_xp",
        "next_level_xp",
        "previous_level_xp",
        "level",
        "rank",
        "background",
        "text_shadow_colour",
        "xp_colour",
        "circle_avatar",
        "badges",
        "unknown_badges",
    )

    def __init__(
        self,
        *,
        username: str,
        avatar_url: str,
        current_xp: int,
        next_level_xp: int,
        previous_level_xp: int,
        level: Optional[int] = None,
        rank: Optional[int] = None,
        background: Optional[str] = None,
        text_shadow_colour: Optional[str] = None,
        text_shadow_color: Optional[str] = None,
        xp_colour: Optional[str] = None,
        xp_color: Optional[str] = None,
        circle_avatar: bool = False,
        badges: Optional[List[Badge]] = None,
    ) -> None:
        self._image: Optional[Image] = None

        self.text_shadow_colour: Optional[str] = (
            text_shadow_colour if text_shadow_colour is not None else text_shadow_color
        )
        self.xp_colour: Optional[str] = xp_colour if xp_colour is not None else xp_color

        self.username: str = username
        self.avatar_url: str = avatar_url
        self.current_xp: int = current_xp
        self.next_level_xp: int = next_level_xp
        self.previous_level_xp: int = previous_level_xp
        self.level: Optional[int] = level
        self.rank: Optional[int] = rank
        self.background: Optional[str] = background
        self.circle_avatar: bool = circle_avatar
        if not badges:
            badges = []

        self.badges: List[Badge] = badges
        self.unknown_badges: List[UnknownBadge] = [badge for badge in self.badges if isinstance(badge, UnknownBadge)]


    def copy(self) -> Rankcard:
        """:class:`Rankcard`: Returns a copy of this object."""
        inst = self.__class__.from_dict(self.to_dict())
        inst._image = self._image
        return inst

    def to_dict(self) -> RankcardData:
        """:class: `dict`: Converts the rankcard to a dict with the correct keys."""
        base = {
            "username": self.username,
            "avatar": self.avatar_url,
            "currentXp": self.current_xp,
            "nextLevelXp": self.next_level_xp,
            "previousLevelXp": self.previous_level_xp,
        }
        if self.badges:
            base["badges"] = "|".join(map(str, self.badges))

        optional_fields = {
            "level": self.level,
            "rank": self.rank,
            "customBg": self.background,
            "textShadowColor": self.text_shadow_colour,
            "xpColor": self.xp_colour,
            "circleAvatar": self.circle_avatar,
        }
        for key, value in optional_fields.items():
            if value is not None:
                base[key] = value

        return base  # type: ignore

    @classmethod
    def from_dict(cls, data: RankcardData) -> Rankcard:
        """Creates a rankcard from a dict.

        Parameters
        ----------
        data: :class:`dict`
            The dict to create the rankcard from with the correct keys.

        Returns
        -------
        :class:`Rankcard`
            The rankcard created from the dict.
        """
        parsed_data = {}
        for key, value in data.items():
            if key == "badges":
                parsed_data[key] = list(map(Badges, value.split("|")))  # type: ignore
            else:
                value = int(value) if hasattr(value, "isdigit") and value.isdigit() else value  # type: ignore
                parsed_data[cls.FRIENDLY_ATTR_NAMES.get(key, key)] = value

        return cls(**parsed_data)

    @property
    def url(self) -> str:
        """:class:`str`: The url of the rankcard."""
        if not self._image:
            # return unparsed url if not state
            base = "https://vacefron.nl/api/rankcard?"
            return base + "&".join(
                f"{key}={value}" for key, value in self.to_dict().items()
            )

        return self._image.url

    if TYPE_CHECKING:
        read = Image.read
        file = Image.file
    else:

        async def read(self, bytesio: bool = False):
            if not self._image:
                raise RuntimeError(
                    (
                        "No session was set. Did you construct this object yourself and not pass it to Client.rankcard? "
                    )
                )
            return await self._image.read(bytesio=bytesio)

        async def file(self, cls, filename: str = "image.png"):
            if not self._image:
                raise RuntimeError(
                    (
                        "No session was set. Did you construct this object yourself and not pass it to Client.rankcard? "
                    )
                )
            return await self._image.file(cls, filename=filename)
