from __future__ import annotations
from typing import Dict, List, TypedDict, TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from typing_extensions import NotRequired

CrewMate = Literal[
    "black",
    "blue",
    "brown",
    "cyan",
    "darkgreen",
    "lime",
    "orange",
    "pink",
    "purple",
    "red",
    "white",
    "yellow",
]


class Wrapper(TypedDict):
    source: str
    package: NotRequired[str]


class Raw(TypedDict):
    discord_server: str
    patreon: str
    readme: str
    endpoints: List[str]
    wrappers: Dict[str, Wrapper]


class WithUser(TypedDict):
    user: str


class WithText(TypedDict):
    text: str


class WithTwoTexts(TypedDict):
    text1: str
    text2: str


class WithImage(TypedDict):
    image: str


class ICanMilkYou(TypedDict):
    user1: str
    user2: NotRequired[str]


class BatmanSlap(TypedDict):
    text1: str
    text2: str
    batman: str
    robin: str


class DistractedBf(TypedDict):
    boyfriend: str
    girlfriend: str
    woman: str


class Ejected(TypedDict):
    name: str
    crewmate: CrewMate
    impostor: bool


class Stonks(TypedDict):
    user: str
    notStonks: NotRequired[bool]


class WomanYellingAtCat(TypedDict):
    woman: str
    cat: str


class Texts(WithText, WithTwoTexts):
    ...


class Users(WithUser, ICanMilkYou):
    ...
