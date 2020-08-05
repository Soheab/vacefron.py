from io import BytesIO


class Image:

    def __init__(self, url: str, session) -> None:
        self.url = url
        self._session = session

    def __str__(self) -> str:
        return self.url if self.url is not None else ''

    async def read(self) -> BytesIO:
        _bytes = await (await self._session.get(str(self.url))).read()
        return BytesIO(_bytes)
