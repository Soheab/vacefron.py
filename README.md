[![PyPi Version](https://img.shields.io/pypi/v/vacefron.py.svg)](https://pypi.python.org/pypi/vacefron.py/)
[![Downloads](https://pepy.tech/badge/vacefron-py)](https://pepy.tech/project/vacefron-py)
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

# VACEfron.py
A Wrapper for [vacefron.nl/api](https://vacefron.nl/api/) written in Python.


# Requirements
- Python 3.6 or above
- aiohttp (python3 -m pip install -U aiohttp)

# Documentation
See the full and detailed [docs here](https://github.com/Soheab/vacefron.py/blob/master/docs.md)

# Installation
Install the package by doing one of the following commands:

##### Using pip (recommended):
- pip install vacefron.py -U
- python -m pip install vacefron.py -U

# Changelog
See the changelog for each [version here](https://github.com/Soheab/vacefron.py/blob/master/changelog.md)

# Examples

Generate a [Rank card](docs.md#rank-card) with [discord.py](https://github.com/Rapptz/discord.py):
```python
import vacefron
import json
import discord

from discord.ext import commands

bot = commands.Bot(command_prefix="!")
vac_api = vacefron.Client()

@bot.command()
async def rank(ctx, member: discord.Member):
    member = member or ctx.author
    with open("ranks.json") as f:
        ranks = json.load(f)

    info = ranks[str(member.id)]
    boosting = True if member.premium_since else False
    gen_card = await vac_api.rank_card(
        username = member,
        avatar = member.avatar_url_as(format="png"), # converting everything to png.
        level = int(info['level']),
        rank = int(info['rank']),
        current_xp = int(info['current_xp']),
        next_level_xp = 500,
        previous_level_xp = 50,
        xp_color = "123456", # optional
        is_boosting = boosting # optional
        )
    rank_image = discord.File(fp = await gen_card.read(), filename = f"{ctx.author}_rank.png")
    await ctx.send(f"{ctx.author.name}'s rank in {ctx.guild.name}", file = rank_image)

# custom_background, is_boosting and xp_color are optional, see more in the docs.
```

[I can milk you meme](docs.md#await-vac_apii_can_milk_youuser-user2) with [discord.py](https://github.com/Rapptz/discord.py):
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

# Made by

This wrapper is made by **Soheab#6240**, DM me on Discord or [join my Server](https://discord.gg/yCzcfju) for anything 
related to this wrapper.
 
You can join VAC Efron's [server here](https://discord.gg/xJ2HRxZ) to suggests something for the API.
