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

### Rank card

---

#### await vac_api.rank_card(username, avatar, level, rank, current_xp, next_level_xp, previous_level_xp, custom_background = None, xp_color = None, is_boosting = False)

Generate a Rank card for Discord bots!

**Parameters**:

- username `string` | The user's name.
- avatar `string` | The user's avatar
- level `int` | The user's current level.
- rank `int` | The user's position on the board.
- current_xp `int` | The user's current XP amount.
- next_level_xp `int` | The user's next XP amount.
- previous_level_xp `int` | The user's previous XP amount.
- custom_background `string` | An optional image url or hex color for the background.
- xp_color `string` | The hex color for the XP bar. Defaults to #FCBA41.
- is_boosting `bool` | If True, a boost badge will be displayed next to user's name. Defaults to False.
- circle_avatar `bool` | If True, the avatar will be rounded instead of a square. Defaults to False.

**Return type**: [RankCard](docs.md#rankcard "RankCard object attributes")

---

### await vac_api.batman_slap(text, text2, batman=None, robin=None)

Generate that batman slapping meme with custom texts and images.

**Parameters**:

- text `string` | Text 1.
- text2 `string` | Text 2.
- batman `string` | Optional avatar for Batman.
- robin `string` | Optional avatar for Robin.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.distracted_bf(boyfriend, girlfriend, woman)

Generate that "distracted boyfriend" meme with your images.

**Parameters**:

- boyfriend `string` | Avatar of user.
- girlfriend `string` | Avatar of user.
- woman `string` | Avatar of user.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.dock_of_shame(user)

Generate that "dock of shame" meme with your avatar.

**Parameters**:

- user `string` | Avatar of user.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.drip(user)

For your own Goku drip memes :)

**Parameters**:

- user `string` | Avatar of user.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.car_reverse(text)

Generate that "car reverse" meme with your own text.

**Parameters**:

- text `string` | Your text.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.change_my_mind(text)

Generate that "change my mind" meme with your own text.

**Parameters**:

- text `string` | Your text.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.emergency_meeting(text)

Generate your own Among Us "Emergency Meeting" Meme!

**Parameters**:

- text `string` | The reason to call an emergency meeting.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.ejected(name, crewmate = CrewMateColors.RED, impostor = False)

Create your own custom Among Us "... Was ~~not~~ The impostor" image!

**Available colors:** `black`, `blue`, `brown`, `cyan`, `darkgreen`, `lime`,
`orange`, `pink`, `purple`, `red`, `white`, `yellow`, `random`,
[CrewMateColors enum](docs.md#crewmatecolors), number from 1 to 13.

**Parameters**:

- name `string` | Name of the person that got ejected.
- crewmate `string` | Color of the person that got ejected, see Available colors. This is optional and defaults to color
  red
- impostor `string` | Determine if the person was the impostor or not. This is optional and defaults to False

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.first_time(user)

Generate that "first time" meme with someone's avatar.

**Parameters**:

- user `string` | Avatar of user.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.grave(user)

Generate a Grave stone with someone's avatar.

**Parameters**:

- user `string` | Avatar of user.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.iam_speed(user)

Generate that "I am speed" meme with someone's avatar.

**Parameters**:

- user `string` | Avatar of user.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.i_can_milk_you(user, user2 = None)

Generate that "I can milk you" meme from Markiplier with someone's avatar.

**Parameters**:

- user `string` | Avatar of user. ~~on Markiplier~~
- user1 `string` | Optional Avatar of user. ~~on the Cow~~

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.heaven(user)

Generate that heaven meme with someone's avatar.

**Parameters**:

- user `string` | Avatar of user.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.npc(text, text2)

Generate that "npc" meme with your own text.

**Parameters**:

- text `string` | Your text.
- text2 `string` | Your text.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.stonks(user, not_stonks)

Generate that "Stonks 〽" meme with someone's avatar.

**Parameters**:

- user `string` | Avatar of user.
- not_stonks `bool` | Determine if it was Stonks or Not Stonks. Defaults to False.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.table_flip(user)

Generate that "Table flip" meme with someone's avatar.

**Parameters**:

- user `string` | Avatar of user.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.water(user)

Generate that "water" meme with your own text.

**Parameters**:

- text `string` | Your Text

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.wide(text)

Make someone's avatar a *little* bit wider.

**Parameters**:

- user `string` | Avatar of user.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.wolverine(user)

Generate that "wolverine looking at a picture" meme with your own avatar.

**Parameters**:

- user `string` | Avatar of user.

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.woman_yelling_at_cat(woman, cat)

Generate that "woman yelling at cat" meme with your images.

**Parameters**:

- woman `string` | Avatar of user. ~~For woman.~~
- cat `string` | Avatar of user. ~~For cat.~~

**Return type:** [Image](docs.md#image "Image object attributes")

---

### await vac_api.discord_server(creator)

Get an invitation to the VAC Efron's server (or and the creator of this wrapper.)

**Parameters**:

- creator `boolean` | To also get an invitation to the server of creator of this wrapper.

**Return type**: string or tuple when `creator` is True

# Examples

See here some examples

##### Generate a [Rank card](docs.md#rank-card) with [discord.py](https://github.com/Rapptz/discord.py):

```python
import vacefron
import json
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix = "!")
vac_api = vacefron.Client()


@bot.command()
async def rank(ctx, member: discord.Member = None):
    member = member or ctx.author
    with open('rank_stuff.json') as json_file:
        data = json.load(json_file)

    user_rank = data[str(member.id)]  # dict
    gen_card = await vac_api.rank_card(
            username = str(member),  # wrapper will handle the #
            avatar = member.avatar_url_as(format = "png"),  # converting avatar to .png, including .gif
            level = int(user_rank['level']), # optional level int on the xp bar.
            rank = int(user_rank['rank']), # optional #int on the card.
            current_xp = int(user_rank['current_xp']),
            next_level_xp = 500,  # you will need calculate this according the current_xp.
            previous_level_xp = 50,  # you will need calculate this according the current_xp.
            custom_background = str(user_rank["background"]),  # optional custom background.
            xp_color = str(user_rank["bar_color"]),  # optional progress bar color. Defaults to #fcba41. 
            is_boosting = bool(member.premium_since),  # optional server boost icon next to username.
            circle_avatar = True  # optional circle avatar instead of a square.
            )
    rank_image = discord.File(fp = await gen_card.read(), filename = f"{member.name}_rank.png")
    await ctx.send(f"{member.name}'s rank in {ctx.guild.name}", file = rank_image)

# level, rank, custom_background, is_boosting, xp_color and circle_avatar are optional, see more in the docs.
```

##### [ejected](docs.md#await-vac_apiejectedname-crewmate--crewmatecolorsred-impostor--false) with [discord.py](https://github.com/Rapptz/discord.py):

```python
import vacefron
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!")
vac_api = vacefron.Client()


@bot.command()
async def eject(ctx, name, crewmate, impostor):
    image = await vac_api.ejected(name, crewmate, impostor)
    image_out = discord.File(fp = await image.read(), filename = "ejected.png")
    await ctx.send(file = image_out)
```

# Objects

Here is explained what attributes the returned objects have

## Image

This object gets returned from every endpoint.

#### Image.url

[str](https://docs.python.org/3/library/stdtypes.html#str ) - The url of the image

#### await Image.read()

This will return a [io.BytesIO](https://docs.python.org/3/library/io.html#binary-i-o) object, which can be passed to
discord.File() with a filename for [discord.py](https://github.com/Rapptz/discord.py):

```py
npc_meme = await vac_api.npc("ah yes", "no u")
npc_bytes = await npc_meme.read()  # <_io.BytesIO object at 0x0438DFC8> - BytesIO object.
await ctx.send(file = discord.File(npc_bytes, filename = "npc.png"))
```

\
You can set `bytesio` to `False` if you want the bytes instead of an `io.BytesIO` object.

## RankCard

This object gets returned from `.rank_card()`

#### RankCard.url

[str](https://docs.python.org/3/library/stdtypes.html#str ) - The url of the card

#### await RankCard.read()

This will return a [io.BytesIO](https://docs.python.org/3/library/io.html#binary-i-o) object, which can be passed to
discord.File() with a filename for [discord.py](https://github.com/Rapptz/discord.py):

```py
card = await vac_api.rank_card(....)
card_bytes = await card.read()  # <_io.BytesIO object at 0x0438DFC8> - BytesIO object.
await Messageable.send(file = discord.File(card_bytes, filename = "rank_card.png"))
```

\
You can set `bytesio` to `False` if you want the bytes instead of an `io.BytesIO` object.

#### RankCard.username

[str](https://docs.python.org/3/library/stdtypes.html#str ) - The user's username, you provided but `#` replaced with `%23`

#### RankCard.avatar

[str](https://docs.python.org/3/library/stdtypes.html#str ) - The user's avatar, you provided

#### RankCard.current_xp

[int](https://docs.python.org/3/library/functions.html#int ) - The user's XP amount, you provided

#### RankCard.next_level_xp

[int](https://docs.python.org/3/library/functions.html#int ) - The user's next XP amount, you provided

#### RankCard.previous_level_xp

[int](https://docs.python.org/3/library/functions.html#int ) - The user's previous XP amount, you provided

#### RankCard.level

Optional[[int](https://docs.python.org/3/library/functions.html#int )] - The user's level you provided

#### RankCard.rank

Optional[[int](https://docs.python.org/3/library/functions.html#int )] - The user's position, you provided

#### RankCard.custom_background

Optional[[str](https://docs.python.org/3/library/stdtypes.html#str )] - An optional background for the rank card, you provided

#### RankCard.xp_color

Optional[[str](https://docs.python.org/3/library/stdtypes.html#str )] - The color for the XP bar, you provided

#### RankCard.is_boosting

[bool](https://docs.python.org/3/library/functions.html#bool )

#### RankCard.circle_avatar

[bool](https://docs.python.org/3/library/functions.html#bool )

## CrewMateColors

Enum for `.ejected()`.

### 1 or black

Black color for the crewmate.

#### 2 or blue

Black color for the crewmate.

#### 3 or brown

Brown color for the crewmate.

#### 4 or cyan

Cyan color for the crewmate.

#### 5 or darkgreen (or dark_green)

Dark green color for the crewmate.

#### 6 or lime

Lime color for the crewmate.

#### 7 or orange

Orange color for the crewmate.

#### 8 or pink

Pink color for the crewmate.

#### 9 or purple

Purple color for the crewmate.

#### 10 or red

Red color for the crewmate.

#### 11 or white

White color for the crewmate.

#### 12 or yellow

Yellow color for the crewmate.

#### 13 or random

Random color from above for the crewmate.
