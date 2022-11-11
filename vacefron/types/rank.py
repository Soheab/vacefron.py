from typing import TYPE_CHECKING, TypedDict, Literal

if TYPE_CHECKING:
    from typing_extensions import NotRequired


Badges = Literal[
    "boost", "bravery", "brilliance", "bughunter", "developer", "earlysupporter", "events", "nitro", "partner", "staff"
]


class Rankcard(TypedDict, total=False):
    username: str
    avatar: str
    currentXp: int
    nextLevelXp: int
    previousLevelXp: int
    level: NotRequired[int]
    rank: NotRequired[int]
    customBg: NotRequired[str]
    textShadowColor: NotRequired[str]
    xpColor: NotRequired[str]
    circleAvatar: NotRequired[bool]
    badges: NotRequired[Badges]
