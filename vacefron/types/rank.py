from typing import TYPE_CHECKING, TypedDict, List

if TYPE_CHECKING:
    from typing_extensions import NotRequired


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
    badges: NotRequired[List[str]]
