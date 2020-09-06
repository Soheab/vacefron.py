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
All available endpoints you can use.

### Rank card

---
#### await vac_api.rank_card(username, avatar, level, rank, current_xp, next_level_xp, previous_level_xp, custom_background, xp_color, is_boosting)
Generate a Rank card for Discord bots!

**Parameters**:
- username `string` | The user's name.
- avatar `string` | The user's avatar
- level `int` | The user's current level.
- rank `int` | The user's position on the board.
- current_xp `int` | The user's current XP amount.
- next_level_xp `int` | The user's next XP amount.
- previous_level_xp `int` | The user's previous XP amount.
- custom_background `string` | An optional background for the rank card.
- xp_color `string` | The color for the XP bar. Defaults to #FCBA41.
- is_boosting `bool` | If True, a boost badge will be displayed next to user's name. Defaults to False.

**Return type**: [Image](docs.md#image "Image object attributes")

---
### await vac_api.distracted_bf(boyfriend, girlfriend, woman)
Generate that "distracted boyfriend" meme with your images.

**Parameters**:
- boyfriend `string` | Avatar of user.
- girlfriend `string` | Avatar of user.
- woman `string` | Avatar of user.

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
### await vac_api.i_can_milk_you(user, user2)
Generate that "I can milk you" meme from Markiplier with someone's avatar.

**Parameters**:
- user `string` | Avatar of user. ~~on Markiplier~~
- user1 `string` | Avatar of user. ~~on the Cow~~

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
### await vac_api.stonks(user)
Generate that "Stonks 〽" meme with someone's avatar.
  
**Parameters**:
- user `string` | Avatar of user.

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
### await vac_api.change_my_mind(text)
Generate that "change my mind" meme with your own text.
  
**Parameters**:
- text `string` | Your text.

**Return type:** [Image](docs.md#image "Image object attributes")

---
### await vac_api.wide(text)
Make someone's avatar a *little* bit wider.
  
**Parameters**:
- user `string` | Avatar of user.

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

bot = commands.Bot(command_prefix="!")
vac_api = vacefron.Client()

@bot.command()
async def rank(ctx, member: discord.Member = None):
    member = member or ctx.author
    with open("ranks.json") as f:
        ranks = json.load(f)

    info = ranks[str(member.id)]
    boosting = True if member.premium_since else False
    gen_card = await vac_api.rank_card(
        username = str(member),
        avatar = member.avatar_url_as(format="png"), # converting avatar to .png, including .gif
        level = int(info['level']),
        rank = int(info['rank']),
        current_xp = int(info['current_xp']),
        next_level_xp = 500,
        previous_level_xp = 50,
        xp_color = "123456", # optional
        is_boosting = boosting # optional
        )
    rank_image = discord.File(fp = await gen_card.read(), filename = f"{member.name}_rank.png")
    await ctx.send(f"{member.name}'s rank in {ctx.guild.name}", file = rank_image)

# custom_background, is_boosting and xp_color are optional, see more in the docs.
```

##### [I can milk you meme](docs.md#await-vac_apii_can_milk_youuser-user2) with [discord.py](https://github.com/Rapptz/discord.py):
```python
import vacefron
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
vac_api = vacefron.Client()

@bot.command()
async def icanmilkyou(ctx, face: discord.Member, cow: discord.Member):
    meme = await vac_api.i_can_milk_you(face.avatar_url, cow.avatar_url)
    meme_image = discord.File(fp = await meme.read(), filename = "let_me_milk_you.png")
    await ctx.send(file=meme_image)
```

# Objects
Here is explained what attributes the returned objects have

## Image
This object gets returned from every endpoint.
    
#### Image.url
The url of the image

#### await Image.read()
This will return a BytesIO object, which can be passed to discord.File() with a filename 
for [discord.py](https://github.com/Rapptz/discord.py):
```py
npc_meme = await vac_api.npc("ah yes", "no u")
npc_bytes = await npc_meme.read() # <_io.BytesIO object at 0x0438DFC8> - BytesIO object.
await ctx.send(file=discord.File(npc_bytes, filename="npc.png"))
```

## RankCard
This object gets returned from `.rank_card()`
    
#### RankCard.url
The url of the card

#### await RankCard.read()
This will return a BytesIO object, which can be passed to discord.File() with a filename 
for [discord.py](https://github.com/Rapptz/discord.py):
```py
card = await vac_api.rank_card(....)
card_bytes = await card.read() # <_io.BytesIO object at 0x0438DFC8> - BytesIO object.
await ctx.send(file=discord.File(card_bytes, filename="rank_card.png"))
```

#### RankCard.username
The user's username, you provided but `#` replaced with `%23`

#### RankCard.avatar
The user's avatar, you provided

#### RankCard.level
The user's current level you provided

#### RankCard.rank
The user's position, you provided

#### RankCard.current_xp
The user's current XP amount, you provided

#### RankCard.next_level_xp
The user's next XP amount, you provided

#### RankCard.previous_level_xp
The user's previous XP amount, you provided

#### RankCard.custom_background
An optional background for the rank card, if you provided one else None

#### RankCard.xp_color
The color for the XP bar but `#` replaced with `%23`, if you provided one else None

#### RankCard.is_boosting
Bool, True if you set it to True else False