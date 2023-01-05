from __future__ import annotations
from typing import Optional, Tuple, TYPE_CHECKING, List, Union, NamedTuple

from enum import Enum

if TYPE_CHECKING:
    from typing_extensions import Self

    from typing import Protocol

    class ValueAttribute(Protocol):

        value: Union[str, int]


class _BaseEnum(Enum):
    def __str__(self) -> str:
        return self.value if isinstance(self.value, str) else self.name

    def __int__(self) -> int:
        return self.value if isinstance(self.value, int) else 0


class CrewmateColour(_BaseEnum):
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

# aliases
CrewmateColor = CrewmateColour


class UnknownEnum(NamedTuple):
    """Represents an unknown enum value.

    This is used when an enum is not known to the library.
    """

    value: Union[str, int]

    @property
    def name(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return str(self.value)


class UnknownBadge(UnknownEnum):
    """Represents an unknown badge.

    This is used when a badge is not known to the library.
    """

    @property
    def name(self) -> str:
        name = super().name
        return name.lower().replace("_", "").replace("hypersquad", "")


class Badge(_BaseEnum):
    ACTIVE_DEVELOPER = "activedeveloper"
    BOOST = "boost"
    BRAVERY = "bravery"
    BALANCE = "balance"
    BRILLIANCE = "brilliance"
    BUG_HUNTER = "bughunter"
    CERTIFIED_MODERATOR = "certifiedmoderator"
    DEVELOPER = "developer"
    EARLY_SUPPORTER = "earlysupporter"
    EVENTS = "events"
    NITRO = "nitro"
    PARTNER = "partner"
    SERVER_OWNER = "serverowner"
    STAFF = "staff"

    # aliases
    BOOSTER = BOOST
    DISCORD_EMPLOYEE = STAFF
    DISCORD_PARTNER = PARTNER
    DISCORD_CERTIFIED_MODERATOR = CERTIFIED_MODERATOR
    HYPESQUAD_EVENTS = EVENTS
    HYPESQUAD_BRAVERY = BRAVERY
    HYPESQUAD_BRILLIANCE = BRILLIANCE
    HYPESQUAD_BALANCE = BALANCE
    EARLY_VERIFIED_BOT_DEVELOPER = DEVELOPER
    VERIFIED_BOT_DEVELOPER = DEVELOPER

    @classmethod
    def from_public_flags(
        cls, value: Union[ValueAttribute, str, int], /, *, extras: Optional[List[Union[Badge, UnknownBadge]]] = None
    ) -> List[Union[Badge, UnknownBadge]]:
        """Converts a public flags value to a list of badges. More info: https://discord.com/developers/docs/resources/user#user-object-user-flags

        Examples
        --------
        .. code-block:: python3
            from vacefron import Badge

            # discord.py: <user>.public_flags -> <discord.PublicUserFlags> can be passed to this method
            badges = Badge.from_public_flags(131072)
            print(badges)
            # [<Badge.DEVELOPER: 'developer'>]

        Parameters
        ----------
        value: Union[ValueAttribute, str, int]
            The public flags value to convert. This can be either a class with a ``value`` attribute, a string or an integer.
            This is usually returned from the user endpoint as ``public_flags`` (https://discord.com/developers/docs/resources/user#user-object).
        extras: Optional[List[Union[Badge, UnknownBadge]]]
            A list of extra badges to add to the list. i.e. ``Badge.NITRO`` is not included in the public flags, so you would need to add it manually.

        Returns
        -------
        List[Union[Badge, UnknownBadge]]
            A list of badges. If a badge is not known to the library, it will be returned as an :class:`UnknownBadge`.
        """
        _value = value.value if not isinstance(value, (str, int)) else value
        if not isinstance(_value, int):
            raise TypeError(f"Expected int, got {type(_value)}")

        res = [
            cls.maybe_unknown_badge(flag.name)
            for flag in DiscordPublicUserFlags.__members__.values()
            if (_value & flag.value) == flag.value
        ]
        if extras:
            res.extend(extras)
        return res

    @classmethod
    def maybe_unknown_badge(cls, value: str) -> Union[Badge, UnknownBadge]:
        """Converts a string to a badge. This is useful for badges that are not supported by this library yet (e.g. new badges) but are by the API."""
        try:
            return cls[value]
        except KeyError:
            return UnknownBadge(value)


# aliases
Badges = Badge


__all__: Tuple[str, ...] = (
    "CrewmateColour",
    "CrewmateColor",
    "Badge",
    "UnknownBadge",
    "Badges",
)

# discord api docs - https://discord.com/developers/docs/resources/user#user-object-user-flags
# inspired by discord.py - https://github.com/Rapptz/discord.py/blob/7863418ddb09ba60016f48b7e7c5ea52c93c24da/discord/enums.py#L465-L485
class DiscordPublicUserFlags(Enum):
    ACTIVE_DEVELOPER = 4194304
    BRAVERY = 64
    BALANCE = 256
    BRILLIANCE = 128
    BUG_HUNTER = 8
    CERTIFIED_MODERATOR = 262144
    DEVELOPER = 131072
    EARLY_SUPPORTER = 512
    EVENTS = 4
    PARTNER = 2
    STAFF = 1

    # not supported by vacefron api
    VERIFIED_BOT = 65536
    BUG_HUNTER_LEVEL_2 = 16384


class AllEndpoints(_BaseEnum):
    ADIOS = "/adios"
    BATMANSLAP = "/batmanslap"
    CARREVERSE = "/carreverse"
    CHANGEMYMIND = "/changemymind"
    DISTRACTEDBF = "/distractedbf"
    DOCKOFSHAME = "/dockofshame"
    DRIP = "/drip"
    EJECTED = "/ejected"
    EMERGENCYMEETING = "/emergencymeeting"
    FIRSTTIME = "firsttime"
    GRAVE = "/grave"
    HEAVEN = "/heaven"
    IAMSPEED = "/iamspeed"
    ICANMILKYOU = "/icanmilkyou"
    NPC = "/npc"
    PEEPOSIGN = "/peeposign"
    RANKCARD = "/rankcard"
    STONKS = "/stonks"
    TABLEFLIP = "/tableflip"
    WATER = "/water"
    WIDE = "/wide"
    WOLVERINE = "/wolverine"
    WOMANYELLINGATCAT = "/womanyellingatcat"


class TextEndpoints(_BaseEnum):
    CARREVERSE = "/carreverse"
    CHANGEMYMIND = "/changemymind"
    EMERGENCYMEETING = "/emergencymeeting"
    NPC = "/npc"
    PEEPOSIGN = "/peeposign"
    WATER = "/water"


class UserEndpoints(_BaseEnum):
    ADIOS = "/adios"
    DOCKOFSHAME = "/dockofshame"
    DRIP = "/drip"
    FIRSTTIME = "/firsttime"
    GRAVE = "/grave"
    IAMSPEED = "/iamspeed"
    ICANMILKYOU = "/icanmilkyou"
    HEAVEN = "/heaven"
    TABLEFLIP = "/tableflip"
    WOLVERINE = "/wolverine"


class ImageEndpoints(_BaseEnum):
    WIDE = "/wide"


class OtherEndpoints(_BaseEnum):
    BATMANSLAP = "/batmanslap"
    DISTRACTEDBF = "/distractedbf"
    EJECTED = "/ejected"
    RANKCARD = "/rankcard"
    STONKS = "/stonks"
    WIDE = "/wide"
    WOMANYELLINGATCAT = "/womanyellingatcat"
