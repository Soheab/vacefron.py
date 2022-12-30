from __future__ import annotations
from typing import TYPE_CHECKING, Literal, Union, overload, Optional, Tuple

from io import BytesIO

if TYPE_CHECKING:
    from typing_extensions import Self
    from typing import Any, Protocol
    from io import BufferedIOBase
    from os import PathLike
    from aiohttp import ClientSession

    class FileLike(Protocol):
        def __call__(
            self,
            fp: Union[str, bytes, PathLike[Any], BufferedIOBase],
            filename: Optional[str] = None,
            **kwargs: Any,
        ) -> Self:
            ...


__all__: Tuple[str, ...] = ("Image",)


class Image:
    def __init__(self, url: str, session: ClientSession) -> None:
        self.url = url
        self._session = session

    def __str__(self) -> str:
        return self.url

    @overload
    async def read(self, bytesio: Literal[True] = ...) -> BytesIO:
        ...

    @overload
    async def read(self, bytesio: Literal[False] = ...) -> bytes:
        ...

    async def read(self, bytesio: bool = True) -> Union[bytes, BytesIO]:
        async with self._session.get(self.url) as response:
            if bytesio:
                return BytesIO(await response.read())
            else:
                return await response.read()

    async def file(self, cls: FileLike, filename: str = "image.png", **kwargs) -> FileLike:
        """Converts the image to a file-like object.

        Parameters
        ----------
        cls: Any
            The file-like object to convert the image to.
            E,g, `discord.File`
        filename: str
            The filename to uswe.
        """
        return cls(await self.read(bytesio=False), filename=filename, **kwargs)
