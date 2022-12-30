# VACEfron.py | Docs

A Wrapper for [vacefron.nl/api](https://vacefron.nl/api) written in Python.\
For any questions and support, you can join [VAC Efron's server](https://discord.gg/xJ2HRxZ)

## Getting Started:

To begin with, you'll have to install the package by doing one of the following commands:

- `pip install -U vacefron.py`
- `python -m pip -U install vacefron.py`

After that, you will have to create the client:

```python
import vacefron

vac_api = vacefron.Client()
```

For future reference in this documentation: when referring to 'vac_api' we refer to that above.

## Using the wrapper:

All available endpoints you can use.

## Rankcard
Generate a Rank card for Discord bots!

## await vac_api.rankcard(rankcard: [Rankcard]) -> [Rankcard]:
Validates and returns the Rankcard object with state.
### Parameters
- rankcard: [Rankcard] - The Rankcard object to validate.
### Example
See [here](#example-1)
## User
---
## await vac_api.adios(user: str) -> [Image]:
Returns an image of meme: "Adios".
#### Parameters:
- user ([str]) - The avatar of the user to use.

## await vac_api.dock_of_shame(user: str) -> [Image]:
Returns an image of meme: "Dock of Shame".
#### Parameters:
- user ([str]) - The avatar of the user to use.

## await vac_api.drip(user: str) -> [Image]:
Returns an image of meme: "Drip".
#### Parameters:
- user ([str]) - The avatar of the user to use.

## await vac_api.wolverine(user: str) -> [Image]:
Returns an image of meme: "Wolverine".
#### Parameters:
- user ([str]) - The avatar of the user to use.

## await vac_api.first_time(user: str) -> [Image]:
Returns an image of meme: "First Time".
#### Parameters:
- user ([str]) - The avatar of the user to use.

## await vac_api.first_time(user: str) -> [Image]:
Returns an image of meme: "First Time".
#### Parameters:
- user ([str]) - The avatar of the user to use.

## await vac_api.iam_speed(user: str) -> [Image]:
Returns an image of meme: "I am Speed".
#### Parameters:
- user ([str]) - The avatar of the user to use.

## await vac_api.i_can_milk_you(user: str, user2: Optional\[[str]]) -> [Image]:
Returns an image of meme: "I can milk you".
#### Parameters:
- user ([str]) - The avatar of the user to use.
- user2 (Optional\[[str]]) - The avatar of the user to use. This is optional.

## await vac_api.heaven(user: str) -> [Image]:
Returns an image of meme: "Heaven".
#### Parameters:
- user ([str]) - The avatar of the user to use.

## await vac_api.table_flip(user: str) -> [Image]:
Returns an image of meme: "Table Flip".
#### Parameters:
- user ([str]) - The avatar of the user to use.

## Text
---

## await vac_api.car_reverse(text: str) -> [Image]:
Returns an image of meme: "Car Reverse".
#### Parameters:
- text ([str]) - The text to use.

## await vac_api.change_my_mind(text: str) -> [Image]:
Returns an image of meme: "Change My Mind".
#### Parameters:
- text ([str]) - The text to use.

## await vac_api.emergency_meeting(text: str) -> [Image]:
Returns an image of meme: "Emergency Meeting".
#### Parameters:
- text ([str]) - The text to use.

## await vac_api.npc(text: str, text2: str) -> [Image]:
Returns an image of meme: "NPC".
#### Parameters:
- text ([str]) - The text to use.
- text2 ([str]) - The text to use.

## await vac_api.water(text: str) -> [Image]:
Returns an image of meme: "Water".
#### Parameters:
- text ([str]) - The text to use.

## await vac_api.peepo_sign(text: str) -> [Image]:
Returns an image of meme: "Peepo Sign".
#### Parameters:
- text ([str]) - The text to use.

## Image
---

## await vac_api.wide(image: str) -> [Image]:
Returns an image of meme: "Wide".
#### Parameters:
- image ([str]) - The image url to use.

## Other
---

## await vac_api.batman_slap(text: str, text2: str, *, batman: Optional\[[str]], robin:  Optional\[[str]]) -> [Image]:
Returns an image of meme: "Batman Slapping robin".
#### Parameters:
- text ([str]) - The text to use.
- text2 ([str]) - The text to use.
- batman (Optional\[[str]]) - The avatar of the user to use. This is optional.
- robin (Optional\[[str]]) - The avatar of the user to use. This is optional.

## await vac_api.distracted_bf(*, boyfriend: str, girlfriend: str, woman: str) -> [Image]:
Returns an image of meme: "Distracted Boyfriend".
#### Parameters:
- boyfriend ([str]) - The avatar of the user to use.
- girlfriend ([str]) - The avatar of the user to use.
- woman ([str]) - The avatar of the user to use.

## await vac_api.stonks(user: str, *, stonks: bool = True) -> [Image]:
Returns an image of meme: "Stonks".
#### Parameters:
- user ([str]) - The avatar of the user to use.
- stonks ([bool]) - Whether it's stonks or not. Defaults to True.

## await vac_api.ejected(name: str, crewmate: [Union]\[[str], [int], [CrewmateColour]], impostor: bool = False) -> [Image]:
Returns an image of amogus meme: "Ejected".
#### Parameters:
- name ([str]) - The name of the user to use.
- crewmate ([Union]\[[str], [int], [CrewmateColour]]) - \
The crewmate colour to use. This can be a string (same as [CrewmateColour] attributes), int (1 to 13) or CrewmateColour enum. 
Defaults to [CrewmateColour].RED.

- impostor ([bool]) - Whether the user is an impostor or not. Defaults to False.

## await vac_api.woman_yelling_at_cat(woman: str, cat: st) -> [Image]:
Returns an image of meme: "Woman Yelling At Cat".
#### Parameters:
- woman ([str]) - The avatar of the user to use.
- cat ([str]) - The avatar of the user to use.


## Models
---

## Enums
---
## CrewmateColour
Represents the crewmate colour. This is used in the [ejected] endpoint.
#### Attributes: `BLACK`, `BLUE`, `BROWN`, `CYAN`, `DARK_GREEN`, `LIME`, `ORANGE`, `PINK`, `PURPLE`, `RED`, `WHITE`, `YELLOW`, `RANDOM`
### Badge
Represents rankcard badges. This is used in the [rankcard] endpoint.
**Aliases**: `Badges`
#### Attributes:
- `ACTIVE_DEVELOPER`
- `BOOST` // `BOOSTER` (alias)
- `BRAVERY` // `HYPESQUAD_BRAVERY` (alias)
- `BALANCE` // `HYPESQUAD_BALANCE` (alias)
- `BRILLIANCE` // `HYPESQUAD_BRILLIANCE` (alias)
- `BUG_HUNTER`
- `CERTIFIED_MODERATOR` // `DISCORD_CERTIFIED_MODERATOR` (alias)
- `DEVELOPER` // `EARLY_VERIFIED_BOT_DEVELOPER` (alias) // `VERIFIED_BOT_DEVELOPER` (alias)
- `EARLY_SUPPORTER`
- `EVENTS` // `HYPESQUAD_EVENTS` (alias)
- `NITRO`
- `PARTNER` // `PARTNERED` (alias)
- `SERVER_OWNER`
- `STAFF` // `DISCORD_EMPLOYEE` (alias)
#### Methods:
- .from_public_flags(flags: [Union]\[ValueAttribute, [int], [str]], *, extras: [Optional]\[List]\[[Union]\[[Badge], ``UnknownBadge``]]] = None) -> [List]\[[Badge]] -
Returns a list of [Badge]s from the public flags. This can be used with discord.py.
This can also take an object with a ``.value`` attribute. The  ``extras`` kwarg can be used to add extra badges to the output list. 
i.e. ``Badge.NITRO`` is not included in the public flags, so you would need to add it manually.
\
Example:
    ```py
    from vacefron import Badge

    user = ctx.author # or any other user object like interaction.user
    badges = Badge.from_public_flags(user.public_flags)
    # but prefferably:
    badges = Badge.from_public_flags(user.public_flags.value)

    # does user have nitro? add it to the list via extras=
    badges = Bagde.from_public_flags(user.public_flags.value, extras=[Badge.NITRO])
    ```

- .maybe_unknown_badge(cls, value: [str]) -> [Union][[Badge], UnknownBadge] -
Converts a string to a badge. This is useful for badges that are not supported by this library yet (e.g. new badges) but are by the API.

---
## Image
Represents an image object. This is returned by almost all the methods.
#### Attributes:
- .url ([str]) - The url of the image.
#### Methods:
- .read(bytesio: [bool] = True) -> [Union]\[bytes, [io.BytesIO]] -
Returns the image in bytes or BytesIO.

- .file(cls: FileLike, filename: [str] = "image.png") -> FileLike - 
Converts the image to a file-like object. This can be used with discord.py.
Example:
    ```py
    from discord import File

    image = await vac_api.wide("https://example.com/image.png")
    await ctx.send(file=image.file(File))
    ```
---
## Rankcard
Represents a rankcard object. This is used to create a rankcard and is returned by the [rankcard] endpoint.
#### Parameters:
All are keyword-only.
- username ([str]) - The name of the user to view on the card.
- avatar_url ([str]) - 
        The avatar url of the user.
- current_xp ([int]) - 
        The current xp of the user.
- next_level_xp ([int]) - 
        The xp required to level up.
- previous_level_xp ([int]) - 
        The xp required to level down.
- level Optional\[[int]] - 
        The level of the user. Defaults to `None`.
- rank Optional\[[int]] - 
        The rank of the user. Defaults to `None`.
- background Optional\[[str]] - 
        The background of the rankcard. This can be a hex value or a url to an image. Defaults to `None`.
- text_shadow_color Optional\[[str]] - 
        The shadow color of the username as hex value. Defaults to `None`.
- xp_colour Optional\[[str]] - 
        The colour of the xp bar as hex value. Defaults to `None`.
- circle_avatar [bool] - 
        Whether the avatar should be a circle or not. Defaults to `False`.
- badges: [List]\[[Union]\[[Badge], ``UnknownBadge``]]
        The badges to add to the rankcard.
        E.g. ``[Badgex.NITRO, Badgex.BOOST]``. ``UnknownBadge`` can be used to add badges that are not in the [Badge] enum. ``UnknownBadge("name")`` or use ``Badge.maybe_unknown_badge("name")``. \
        Defaults to an empty list.
#### Attributes:
- .url ([str]) - The full url of the rankcard.
- all_badges: [List]\[Union]\[[Badge], ``UnknownBadge``]]
All badges that are added to the rankcard.
- badges: [List]\[[Badge]]
All valid badges supported by this library that are added to the rankcard.
- unknown_badges: [List][``UnknownBadge``]
Returns a list of unknown badges that are added to the rankcard.

These are badges that are not in the [Badge] enum because they are possibly not added to this library yet.
The api does nothing if unknown badges are passed to it.

The objects returned have  a ``name`` attribute which is the name of the badge.
#### Methods:
- .read(bytesio: [bool] = True) -> [Union]\[bytes, [io.BytesIO]] -
Returns the image in bytes or BytesIO.

- .file(cls: FileLike, filename: [str] = "image.png") -> FileLike - 
Converts the image to a file-like object. This can be used with discord.py.
Example:
    ```py
    from discord import File

    image = await vac_api.wide("https://example.com/image.png")
    await ctx.send(file=image.file(File))
    ```

- .add_badge(badge: [Union]\[[str], [Badge], ``UnknownBadge``]) -> None
Adds a badge to the rankcard. This can be used to add badges that are not in the [Badge] enum.

- .remove_badge(badge: [Union]\[[str], [Badge], ``UnknownBadge``]) -> None
Removes a badge from the rankcard. This can be used to remove badges that are not in the [Badge] enum.

- .add_badges_from_public_flags(public_flags: [int], /, *, extras: [Optional]\[List]\[Union]\[[Badge], ``UnknownBadge``]]] = None) -> None -
Adds badges from a user's public flags. The ``extras`` parameter can be used to add badges that are not included in the public flags like nitro. See [Badge].from_public_flags for more info.
#### Example:
```py
from vacefron import Rankcard

rank_card = Rankcard(
    username = "Vacefron",
    avatar_url = "https://cdn.discordapp.com/avatars/123456789012345678/123456789012345678.png",
    current_xp = 100,
    next_level_xp = 200,
    previous_level_xp = 0,
    level = 1,
    rank = 1,
    ...
)
card = await vac_api.rankcard(rank_card)
print(card.name, card.url)
```

[str]: https://docs.python.org/3/library/stdtypes.html#str
[int]: https://docs.python.org/3/library/functions.html#int
[bool]: https://docs.python.org/3/library/functions.html#bool
[discord.py]: https://github.com/Rapptz/discord.py
[io.BytesIO]: https://docs.python.org/3/library/io.html#binary-i-o
[Union]: https://docs.python.org/3/library/typing.html#typing.Union
[List]: https://docs.python.org/3/library/stdtypes.html#list
[tuple]: https://docs.python.org/3/library/stdtypes.html?highlight=tuple#tuple
[Image]: #image-1
[Badge]: #badge
[Rankcard]: #rankcard-1
[CrewmateColour]: #crewmatecolour
[ejected]: #await-vac_apiejectedname-str-crewmate-unionstr-int-crewmatecolour-impostor-bool--false---image