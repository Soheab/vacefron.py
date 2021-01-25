from asyncio import AbstractEventLoop
from asyncio import get_event_loop
from random import choice as choose
from re import search
from typing import Union
from urllib.parse import quote, urlencode

from aiohttp import ClientSession

from .classes import Image, RankCard, CrewMateColors
from .errors import BadRequest, HTTPException, InternalServerError, NotFound


async def _get_from_enum(enum_class, value: Union[str, int]):
    try:
        if isinstance(value, str):
            val = enum_class[str(value.upper())]
        elif isinstance(value, int):
            val = enum_class(int(value))
        else:
            val = value

        return val
    except (KeyError, ValueError):
        return None


class Client:
    __slots__ = ("session", "loop")

    def __init__(self, *, session: ClientSession = None, loop: AbstractEventLoop = None) -> None:
        self.session = ClientSession(loop = get_event_loop() or loop) or session

    async def _api_request(self, endpoint: str, params: dict = None):
        url = f"https://vacefron.nl/api/{endpoint}"
        if params:
            encoded_param = urlencode(params, quote_via = quote)
            url += f"?{encoded_param}"
        response = await self.session.get(str(url))

        if response.content_type == "application/json" and response.status == 200:
            return await response.json()
        elif response.status == 200:
            return response
        elif response.status == 400:
            raise BadRequest((await response.json()).get("message", "didn't return json..."))
        elif response.status == 404:
            raise NotFound((await response.json()).get("message", "didn't return json..."))
        elif response.status == 500:
            raise InternalServerError((await response.json()).get("message", "didn't return json..."))
        else:
            msg = (await response.json()).get("message", "didn't return json...")
            raise HTTPException(response, msg)

    # Json/URL

    async def discord_server(self, creator: bool = False) -> Union[str, tuple]:
        json_response = await self._api_request("")
        support_server = json_response.get("discord_server")
        if creator:
            return support_server, "https://discord.gg/yCzcfju"

        return support_server

    # Image

    async def batman_slap(self, text: str, text2: str, batman: str = None, robin: str = None) -> Image:
        params = {"text1": str(text), "text2": str(text2)}
        if batman:
            params["batman"] = str(batman)
        if robin:
            params["robin"] = str(robin)

        response = await self._api_request("batmanslap", params)
        return Image(str(response.url), response)

    async def distracted_bf(self, boyfriend: str, girlfriend: str, woman: str) -> Image:
        response = await self._api_request("distractedbf", {"boyfriend": str(boyfriend), "girlfriend": str(girlfriend),
                                                            "woman": str(woman)})
        return Image(str(response.url), response)

    async def dock_of_shame(self, user: str) -> Image:
        response = await self._api_request("dockofshame", {"user": str(user)})
        return Image(str(response.url), response)

    async def drip(self, user: str) -> Image:
        response = await self._api_request(
                "drip", {"user": str(user)})
        return Image(str(response.url), response)

    async def car_reverse(self, text: str) -> Image:
        response = await self._api_request("carreverse", {"text": str(text)})
        return Image(str(response.url), response)

    async def change_my_mind(self, text: str) -> Image:
        response = await self._api_request("changemymind", {"text": str(text)})
        return Image(str(response.url), response)

    async def emergency_meeting(self, text: str) -> Image:
        response = await self._api_request("emergencymeeting", {"text": str(text)})
        return Image(str(response.url), response)

    async def ejected(self, name: str, crewmate: Union[str, int, CrewMateColors] = CrewMateColors.RED,
                      impostor: bool = False, imposter: bool = False) -> Image:
        impostor = impostor or imposter
        get_color = await _get_from_enum(CrewMateColors, crewmate)
        if get_color is CrewMateColors.RANDOM or not get_color:
            crewmate = choose(list(CrewMateColors)).name
        else:
            crewmate = get_color.name

        response = await self._api_request(
                "ejected", {"name": str(name), "crewmate": str(crewmate.lower()), "impostor": bool(impostor)})
        return Image(str(response.url), response)

    async def first_time(self, user: str) -> Image:
        response = await self._api_request("firsttime", {"user": str(user)})
        return Image(str(response.url), response)

    async def grave(self, user: str) -> Image:
        response = await self._api_request("grave", {"user": str(user)})
        return Image(str(response.url), response)

    async def iam_speed(self, user: str) -> Image:
        response = await self._api_request("iamspeed", {"user": str(user)})
        return Image(str(response.url), response)

    async def i_can_milk_you(self, user: str, user2: str = None) -> Image:
        params = {"user1": str(user)}
        if user2:
            params["user2"] = str(user2)

        response = await self._api_request("icanmilkyou", params)
        return Image(str(response.url), response)

    async def heaven(self, user: str) -> Image:
        response = await self._api_request("heaven", {"user": str(user)})
        return Image(str(response.url), response)

    async def npc(self, text: str, text2: str) -> Image:
        response = await self._api_request("npc", {"text1": str(text), "text2": str(text2)})
        return Image(str(response.url), response)

    async def stonks(self, user: str, not_stonks = False) -> Image:
        params = {"user": str(user)}
        if not_stonks:
            params["notstonks"] = True

        response = await self._api_request("stonks", params)
        return Image(str(response.url), response)

    async def table_flip(self, user: str) -> Image:
        response = await self._api_request("tableflip", {"user": str(user)})
        return Image(str(response.url), response)

    async def water(self, text: str) -> Image:
        response = await self._api_request("water", {"text": str(text)})
        return Image(str(response.url), response)

    async def wide(self, image: str) -> Image:
        response = await self._api_request("wide", {"image": str(image)})
        return Image(str(response.url), response)

    async def wolverine(self, user: str) -> Image:
        response = await self._api_request("wolverine", {"user": str(user)})
        return Image(str(response.url), response)

    async def woman_yelling_at_cat(self, woman: str, cat: str) -> Image:
        response = await self._api_request("womanyellingatcat", {"woman": str(woman), "cat": str(cat)})
        return Image(str(response.url), response)

    async def rank_card(self, username: str, avatar: str, current_xp: int, next_level_xp: int, previous_level_xp: int,
                        *, level: int = None, rank: int = None, custom_background: str = None, xp_color: str = None,
                        is_boosting: bool = False, circle_avatar: bool = False) -> RankCard:

        params = {
            "username": str(username), "avatar": str(avatar), "currentxp": int(current_xp),
            "nextlevelxp": int(next_level_xp), "previouslevelxp": int(previous_level_xp)
            }

        if level:
            params['level'] = int(level)
        if rank:
            params['rank'] = int(rank)
        if custom_background:
            params['custombg'] = str(custom_background).strip("#")
        if xp_color:
            if not search(r"^(?:[0-9a-fA-F]{3}){1,2}$", str(xp_color).strip("#")):
                raise BadRequest(
                        "Invalid HEX value. You're only allowed to enter HEX (0-9 & A-F)"
                        )
            params['xpcolor'] = str(xp_color).replace("#", "")
        if is_boosting:
            params['isboosting'] = bool(is_boosting)
        if circle_avatar:
            params['circleavatar'] = bool(circle_avatar)

        response = await self._api_request("rankcard", params)
        return RankCard(str(response.url), response, params)

    async def close(self) -> None:
        if not self.session.closed:
            await self.session.close()

    # Aliases
    womanyellingatcat = woman_yelling_at_cat
    icanmilkyou = i_can_milk_you
    iamspeed = iam_speed
    emergencymeeting = emergency_meeting
    changemymind = change_my_mind
    carreverse = car_reverse
    dockofshame = dock_of_shame
    distractedbf = distracted_bf
    batmanslap = batman_slap
    firsttime = first_time
    rankcard = rank_card
