from asyncio import get_event_loop
from random import choice as choose
from typing import Tuple, Union
from urllib.parse import quote

from aiohttp import ClientSession

from .classes import Image, RankCard
from .errors import BadRequest, HTTPException, InternalServerError, NotFound


class Client:

    def __init__(self, session: ClientSession = None) -> None:
        self.session = ClientSession(loop = get_event_loop()) or session
        self._api_url = "https://vacefron.nl/api"

    async def _check_url(self, url: str):
        url = str(url)
        response = await self.session.get(url = url)
        if response.status == 200:
            return url
        elif response.status == 400:
            raise BadRequest((await response.json()).get("message"))
        elif response.status == 404:
            raise NotFound((await response.json()).get("message"))
        elif response.status == 500:
            raise InternalServerError((await response.json()).get("message"))
        else:
            raise HTTPException(response, (await response.json()).get("message"))

    # Json/URL

    async def discord_server(self, creator: bool = False) -> Union[str, Tuple]:
        api = await self.session.get(self._api_url)
        support_server = (await api.json()).get("discord_server")
        if creator:
            return support_server, "https://discord.gg/yCzcfju"

        return support_server

    # Image

    async def distracted_bf(self, boyfriend: str, girlfriend: str, woman: str) -> Image:
        url = f"{self._api_url}/distractedbf" \
              f"?boyfriend={str(boyfriend)}" \
              f"&girlfriend={str(girlfriend)}" \
              f"&woman={str(woman)}"

        url = await self._check_url(url)
        return Image(url, self.session)

    async def car_reverse(self, text: str) -> Image:
        url = await self._check_url(f"{self._api_url}/carreverse?text={quote(str(text))}")
        return Image(url, self.session)

    async def change_my_mind(self, text: str) -> Image:
        url = await self._check_url(f"{self._api_url}/changemymind?text={quote(str(text))}")
        return Image(url, self.session)

    async def emergency_meeting(self, text: str) -> Image:
        url = await self._check_url(f"{self._api_url}/emergencymeeting?text={quote(str(text))}")
        return Image(url, self.session)

    async def ejected(self, name: str, crewmate: str = "red",
                      impostor: bool = False, imposter: bool = False) -> Image:
        if imposter is True:
            impostor = True
        if imposter is False:
            impostor = False
        crewmate_colors = [
            'black', 'blue', 'brown', 'cyan', 'darkgreen', 'lime',
            'orange', 'pink', 'purple', 'red', 'white', 'yellow',
            'random'
            ]
        if crewmate.lower() == "random":
            crewmate = choose(crewmate_colors)
        url = await self._check_url(
                f"{self._api_url}/ejected"
                f"?name={quote(str(name))}"
                f"&crewmate={crewmate.lower()}"
                f"&impostor={impostor}"
                )
        return Image(url, self.session)

    async def first_time(self, user: str) -> Image:
        url = await self._check_url(f"{self._api_url}/firsttime?user={str(user)}")
        return Image(url, self.session)

    async def grave(self, user: str) -> Image:
        url = await self._check_url(f"{self._api_url}/grave?user={str(user)}")
        return Image(url, self.session)

    async def iam_speed(self, user: str) -> Image:
        url = await self._check_url(f"{self._api_url}/iamspeed?user={str(user)}")
        return Image(url, self.session)

    async def i_can_milk_you(self, user: str, user2: str = None) -> Image:
        url = f"{self._api_url}/icanmilkyou?user1={str(user)}"
        if user2 is not None:
            url += f"&user2={str(user)}"

        url = await self._check_url(url)
        return Image(url, self.session)

    async def heaven(self, user: str) -> Image:
        url = await self._check_url(f"{self._api_url}/heaven?user={str(user)}")
        return Image(url, self.session)

    async def npc(self, text: str, text2: str) -> Image:
        url = await self._check_url(f"{self._api_url}/npc?text1={quote(str(text))}&text2={quote(str(text2))}")
        return Image(url, self.session)

    async def stonks(self, user: str) -> Image:
        url = await self._check_url(f"{self._api_url}/stonks?user={str(user)}")
        return Image(url, self.session)

    async def table_flip(self, user: str) -> Image:
        url = await self._check_url(f"{self._api_url}/tableflip?user={str(user)}")
        return Image(url, self.session)

    async def water(self, text: str) -> Image:
        url = await self._check_url(f"{self._api_url}/water?text={quote(str(text))}")
        return Image(url, self.session)

    async def wide(self, image: str) -> Image:
        url = await self._check_url(f"{self._api_url}/wide?image={str(image)}")
        return Image(url, self.session)

    async def rank_card(
            self, username: str, avatar: str, level: int, rank: int, current_xp: int,
            next_level_xp: int, previous_level_xp: int, custom_background: str = None,
            xp_color: str = None, is_boosting: bool = False) -> RankCard:

        custom_background = str(custom_background).replace("#", "") if custom_background else None
        xp_color = str(xp_color).replace("#", "") if xp_color else None

        card = RankCard(
                self.session,
                quote(str(username)), str(avatar), level, rank, current_xp,
                next_level_xp, previous_level_xp, custom_background, xp_color, is_boosting
                )

        await self._check_url(str(card))
        return card

    async def close(self) -> None:
        if not self.session.closed:
            await self.session.close()
