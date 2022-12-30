from __future__ import annotations
from typing import Coroutine, Optional, Tuple, ClassVar, Union, Any, TYPE_CHECKING

import aiohttp
import urllib.parse

from .errors import *
from .models.image import Image
from .enums import OtherEndpoints

if TYPE_CHECKING:
    from aiohttp import ClientResponse
    from typing_extensions import Unpack

    from .client import Client
    from .models import Rankcard
    from .enums import TextEndpoints, UserEndpoints, ImageEndpoints
    from .types.http import (
        Raw,
        BatmanSlap as BatmanSlapData,
        DistractedBf as DistractedBfData,
        Ejected as EjectedData,
        Stonks as StonksData,
        WomanYellingAtCat as WomanYellingAtCatData,
    )

    Response = Coroutine[Any, Any, ClientResponse]
    ValidEndpoint = Union[TextEndpoints, UserEndpoints, OtherEndpoints, ImageEndpoints]


class HTTPClient:
    BASE_URL: ClassVar[str] = "https://vacefron.nl/api"

    __slots__: Tuple[str, ...] = (
        "_client",
        "__session",
    )

    def __init__(self, client: Client, session: Optional[aiohttp.ClientSession] = None) -> None:
        self._client: Client = client
        self.__session: Optional[aiohttp.ClientSession] = session

    async def initiate_session(self) -> None:
        if not self.__session or self.__session.closed:
            self.__session = aiohttp.ClientSession()

    async def request(self, endpoint: Optional[ValidEndpoint] = None, **params: Any) -> ClientResponse:
        url = f"{self.BASE_URL}"
        return_json = False
        if endpoint:
            url = f"{self.BASE_URL}{str(endpoint)}"
        else:
            return_json = True
        if params:
            encoded_param = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
            url += f"?{str(encoded_param)}"

        await self.initiate_session()
        # Gets rid of the linter warning.
        if not self.__session:
            raise RuntimeError("Session is not initialized. This should never happen.")

        async with self.__session.get(url) as response:
            if response.status == 200:
                if return_json:
                    return await response.json()
                return response

            elif response.status == 400:
                raise BadRequest(await response.text())
            elif response.status == 403:
                raise Forbidden(await response.text())
            elif response.status == 404:
                raise NotFound(await response.text())
            elif response.status == 500:
                raise InternalServerError(await response.text())
            else:
                raise HTTPException(response, await response.text())

    def _handle_image(self, response: ClientResponse) -> Image:
        # Gets rid of the linter warning.
        if not self.__session:
            raise RuntimeError("Session is not initialized. This should never happen.")

        return Image(str(response.url), self.__session)

    def with_users(self, endpoint: UserEndpoints, *users: Union[str, None]) -> Response:
        if len(users) == 1:
            return self.request(endpoint, user=users[0])

        payload = {}
        for i, user in enumerate(users, start=1):
            if user is not None:
                payload[f"user{i}"] = user

        return self.request(endpoint, **payload)

    def with_text(self, endpoint: TextEndpoints, *texts: Union[str, None]) -> Response:
        if len(texts) == 1:
            return self.request(endpoint, text=texts[0])

        payload = {}
        for i, text in enumerate(texts, start=1):
            if text is not None:
                payload[f"text{i}"] = text

        return self.request(endpoint, **payload)

    def with_image(self, endpoint: ImageEndpoints, *images: Union[str, None]) -> Response:
        if len(images) == 1:
            return self.request(endpoint, image=images[0])

        payload = {}
        for i, image in enumerate(images, start=1):
            if image is not None:
                payload[f"image{i}"] = image

        return self.request(endpoint, **payload)

    async def rankcard(self, obj: Rankcard) -> Rankcard:
        res = await self.request(OtherEndpoints.RANKCARD, **obj.to_dict())
        obj._image = self._handle_image(res)
        return obj

    def batman_slap(self, **options: Unpack[BatmanSlapData]) -> Response:
        return self.request(OtherEndpoints.BATMANSLAP, **options)

    def distracted_bf(self, **options: Unpack[DistractedBfData]) -> Response:
        return self.request(OtherEndpoints.DISTRACTEDBF, **options)

    def stonks(self, **options: Unpack[StonksData]) -> Response:
        return self.request(OtherEndpoints.STONKS, **options)

    def woman_yelling_at_woman(self, **options: Unpack[WomanYellingAtCatData]) -> Response:
        return self.request(OtherEndpoints.WOMANYELLINGATCAT, **options)

    def ejected(self, **options: Unpack[EjectedData]) -> Response:
        return self.request(OtherEndpoints.EJECTED, **options)

    def base_page(self) -> Coroutine[Any, Any, Raw]:
        return self.request()  # type: ignore

    async def close(self) -> None:
        if self.__session and not self.__session.closed:
            await self.__session.close()

        self.__session = None
