from __future__ import annotations
from typing import TYPE_CHECKING, Literal, Optional, Tuple, Union, overload

from random import choice as choose

from aiohttp import ClientSession

from . import utils as _utils
from .models.rank import Rankcard
from .errors import *
from .http import HTTPClient as _HTTPClient
from .enums import ImageEndpoints, TextEndpoints, UserEndpoints, CrewmateColour

if TYPE_CHECKING:
    from aiohttp import ClientSession
    from .models.image import Image

__all__: Tuple[str, ...] = ("Client",)


class Client:
    """Represents a Client for the Vacefron API.

    Parameters
    ----------
    session: Optional[:class:`aiohtttp.ClientSession`]
        The session to use for the HTTPClient. If not provided, a new one will be created.
    """

    __slots__: Tuple[str, ...] = ("__http",)

    def __init__(self, *, session: Optional[ClientSession] = None) -> None:
        self.__http: _HTTPClient = _HTTPClient(self, session=session)

    # Json/URL

    @overload
    async def discord_server(self, *, creator: Literal[False] = ...) -> str:
        ...

    @overload
    async def discord_server(self, *, creator: Literal[True] = ...) -> Tuple[str, str]:
        ...

    async def discord_server(self, *, creator: bool = False) -> Union[str, Tuple[str, str]]:
        """Returns an invite to the API's support server.

        Parameters
        ----------
        creator: Optional[:class:`bool`]
            Whether to also return the wrapper creator's support server invite.

        Returns
        -------
        Union[:class:`str`, :class:`Tuple[:class:`str`, :class:`str`]`]
            The invites.
        """
        data = await self.__http.base_page()
        support_server = data["discord_server"]
        if creator is True:
            return support_server, "https://discord.gg/yCzcfju"

        return support_server

    async def readme(self) -> str:
        """:class:`str`: Returns the readme of the API."""
        data = await self.__http.base_page()
        return data["readme"]

    # User

    async def adios(self, user: str) -> Image:
        """Returns an image of meme: "adios".

        Parameters
        ----------
        user: :class:`str`
            The avatar of the user to use on the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_users(UserEndpoints.ADIOS, user)
        return self.__http._handle_image(response)

    async def dock_of_shame(self, user: str) -> Image:
        """Returns an image of meme: "dock of shame".

        Parameters
        ----------
        user: :class:`str`
            The user avatar to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_users(UserEndpoints.DOCKOFSHAME, user)
        return self.__http._handle_image(response)

    async def drip(self, user: str) -> Image:
        """Returns an image of meme: "drip".

        Parameters
        ----------
        user: :class:`str`
            The user avatar to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_users(UserEndpoints.DRIP, user)
        return self.__http._handle_image(response)

    async def wolverine(self, user: str) -> Image:
        """Returns an image of meme: "wolverine".

        Parameters
        ----------
        user: :class:`str`
            The user avatar to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_users(UserEndpoints.WOLVERINE, user)
        return self.__http._handle_image(response)

    async def first_time(self, user: str) -> Image:
        """Returns an image of meme: "first time".

        Parameters
        ----------
        user: :class:`str`
            The user avatar to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_users(UserEndpoints.FIRSTTIME, user)
        return self.__http._handle_image(response)

    async def grave(self, user: str) -> Image:
        """Returns an image of meme: "grave".

        Parameters
        ----------
        user: :class:`str`
            The user avatar to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_users(UserEndpoints.GRAVE, user)
        return self.__http._handle_image(response)

    async def iam_speed(self, user: str) -> Image:
        """Returns an image of meme: "i am speed".

        Parameters
        ----------
        user: :class:`str`
            The user avatar to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_users(UserEndpoints.IAMSPEED, user)
        return self.__http._handle_image(response)

    async def i_can_milk_you(self, user: str, user2: Optional[str] = None) -> Image:
        """Returns an image of meme: "i can milk you".

        Parameters
        ----------
        user: :class:`str`
            The user avatar to use in the image.
        user2: Optional[:class:`str`]
            The user avatar to use in the image. This is optional.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_users(UserEndpoints.ICANMILKYOU, user, user2)
        return self.__http._handle_image(response)

    async def heaven(self, user: str) -> Image:
        """Returns an image of meme: "heaven".

        Parameters
        ----------
        user: :class:`str`
            The user avatar to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_users(UserEndpoints.HEAVEN, user)
        return self.__http._handle_image(response)

    async def table_flip(self, user: str) -> Image:
        """Returns an image of meme: "table flip".

        Parameters
        ----------
        user: :class:`str`
            The user avatar to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_users(UserEndpoints.TABLEFLIP, user)
        return self.__http._handle_image(response)

    # Text

    async def car_reverse(self, text: str) -> Image:
        """Returns an image of meme: "car reverse"

        Parameters
        ----------
        text: :class:`str`
            The text to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_text(TextEndpoints.CARREVERSE, text)
        return self.__http._handle_image(response)

    async def change_my_mind(self, text: str) -> Image:
        """Returns an image of meme: "change my mind"

        Parameters
        ----------
        text: :class:`str`
            The text to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_text(TextEndpoints.CHANGEMYMIND, text)
        return self.__http._handle_image(response)

    async def emergency_meeting(self, text: str) -> Image:
        """Returns an image of meme: "emergency meeting"

        Parameters
        ----------
        text: :class:`str`
            The text to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_text(TextEndpoints.EMERGENCYMEETING, text)
        return self.__http._handle_image(response)

    async def npc(self, text: str, text2: str) -> Image:
        """Returns an image of meme: "npc"

        Parameters
        ----------
        text: :class:`str`
            The text to use in the image.
        text2: :class:`str`
            The text to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_text(TextEndpoints.NPC, text, text2)
        return self.__http._handle_image(response)

    async def water(self, text: str) -> Image:
        """Returns an image of text: "water"

        Parameters
        ----------
        text: :class:`str`
            The text to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_text(TextEndpoints.WATER, text)
        return self.__http._handle_image(response)

    async def peepo_sign(self, text: str) -> Image:
        """Returns an image of text: "peepo sign"

        Parameters
        ----------
        text: :class:`str`
            The text to use in the image.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_text(TextEndpoints.PEEPOSIGN, text)
        return self.__http._handle_image(response)

    # Image

    async def wide(self, image: str) -> Image:
        """Returns an image of meme: "wide"

        Parameters
        ----------
        image: :class:`str`
            The image to use.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        response = await self.__http.with_image(ImageEndpoints.WIDE, image)
        return self.__http._handle_image(response)

    # Other

    async def batman_slap(
        self,
        text: str,
        text2: str,
        *,
        batman: Optional[str] = None,
        robin: Optional[str] = None,
    ) -> Image:
        """Returns an image of meme: "batman slap"

        Parameters
        ----------
        text: :class:`str`
            The text to use in the image.
        text2: Optional[:class:`str`]
            The text to use in the image. This is optional.
        batman: Optional[:class:`str`]
            The user avatar to use in the image. This is optional.
        robin: Optional[:class:`str`]
            The user avatar to use in the image. This is optional.

        Returns
        -------
        :class:`Image`
            An Image object representing the generated image.
        """
        extras = {}
        if batman:
            extras["batman"] = batman
        if robin:
            extras["robin"] = robin
        response = await self.__http.batman_slap(text1=text, text2=text2, **extras)
        return self.__http._handle_image(response)

    async def distracted_bf(self, *, boyfriend: str, girlfriend: str, woman: str) -> Image:
        """Returns an image of meme: "distracted bf"

        Parameters
        ----------
        boyfriend: :class:`str`
            The user avatar to use in the image.
        girlfriend: :class:`str`
            The user avatar to use in the image.
        woman: :class:`str`
            The user avatar to use in the image.
        """
        response = await self.__http.distracted_bf(boyfriend=boyfriend, girlfriend=girlfriend, woman=woman)
        return self.__http._handle_image(response)

    async def stonks(self, user: str, *, stonks: bool = True) -> Image:
        """Returns an image of meme: "stonks"

        Parameters
        ----------
        user: :class:`str`
            The user avatar to use in the image.
        stonks: :class:`bool`
            Whether it's stonks or not. Defaults to True.
        """
        response = await self.__http.stonks(user=user, notStonks=not stonks)
        return self.__http._handle_image(response)

    async def ejected(
        self,
        name: str,
        crewmate: Union[str, int, CrewmateColour] = CrewmateColour.RED,
        impostor: bool = False,
        imposter: bool = False,
    ) -> Image:
        """Returns an image of meme: "ejected"

        Parameters
        ----------
        name: :class:`str`
            The name to use in the image.
        crewmate: Union[:class:`str`, :class:`int`, :class:`CrewmateColour`]
            The crewmate colour to use in the image.
            E,g CrewmateColour.RED

            Defaults to CrewmateColour.RED.
        impostor: :class:`bool`
            Whether the crewmate is an impostor. Defaults to False.
        imposter: :class:`bool`
            Alias for impostor.
        """
        impostor = impostor or imposter
        val = crewmate  # type: ignore
        if not isinstance(crewmate, CrewmateColour):
            try:
                if isinstance(crewmate, str):
                    val = CrewmateColour[str(crewmate.upper())]
                elif isinstance(crewmate, int):
                    val = CrewmateColour(int(crewmate))
            except (KeyError, ValueError):
                pass
            else:
                # [:-1] to remove the random option
                val = choose(list(CrewmateColour)[:-1])

        val: CrewmateColour
        response = await self.__http.ejected(name=name, impostor=imposter, crewmate=val.name.lower())  # type: ignore
        return self.__http._handle_image(response)

    async def woman_yelling_at_cat(self, woman: str, cat: str) -> Image:
        """Returns an image of meme: "Woman Yelling at Cat"

        Parameters
        ----------
        woman: :class:`str`
            The user avatar to use in the image.
        cat: :class:`str`
            The user avatar to use in the image.
        """
        response = await self.__http.woman_yelling_at_woman(woman=woman, cat=cat)
        return self.__http._handle_image(response)

    async def rankcard(
        self,
        rankcard: Rankcard,
        **kwargs,
    ) -> Rankcard:
        """Validates and returns the Rankcard object with state.

        Parameters
        ----------
        rankcard: :class:`Rankcard`
            The Rankcard object to validate.
        """
        if not isinstance(rankcard, Rankcard):
            base = f"'rankcard=' must be a Rankcard object. got {rankcard.__class__.__name__!r} instead."
            if kwargs:
                valid_kwargs, invalid_kwargs = _utils._convert_rankcard_kwargs(**kwargs)
                join_kwargs = ", ".join(f"{k}={v!r}" for k, v in valid_kwargs.items())
                converted_signature = f"Rankcard({join_kwargs})"

                base += (
                    "\nI see that you are using keyword arguments, that is not supported anymore since version 2.0! "
                    "You must use construct a Rankcard object and pass it as the first argument now. "
                    "See the documentation for more information but here is an example of how to convert your code:\n"
                    f"I have converted your keyword arguments to a Rankcard object for you: {converted_signature}."
                )
                if invalid_kwargs:
                    invalid_kwargs = ", ".join(f"{k} -> {v!r}" for k, v in invalid_kwargs.items())
                    base += f"\n\nI did find some invalid keyword arguments, here is what I converted them to and the ones I couldn't convert: {invalid_kwargs}."

                support_server = await self.discord_server(creator=True)
                base += "\nIf you are still having issues, please join the {support_server} and ask for help there."
                base += "\n\n!!! This detailed error will be removed in the future !!! please update your code."

            raise TypeError(base)

        rankcard = rankcard.copy()
        return await self.__http.rankcard(rankcard)

    async def close(self) -> None:
        await self.__http.close()

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
    rank_card = rankcard
    peeposign = peepo_sign
