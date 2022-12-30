from typing import Tuple
from enum import Enum


class _BaseEnum(Enum):
    def __str__(self) -> str:
        return self.value if isinstance(self.value, str) else ""

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


class Badges(_BaseEnum):
    BOOST = "boost"
    BRAVERY = "bravery"
    BRILLIANCE = "brilliance"
    BUG_HUNTER = "bughunter"
    DEVELOPER = "developer"
    EARLY_SUPPORTER = "earlysupporter"
    EVENTS = "events"
    NITRO = "nitro"
    PARTNER = "partner"
    STAFF = "staff"


__all__: Tuple[str, ...] = (
    "CrewmateColour",
    "Badges",
)


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
