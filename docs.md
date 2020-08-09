# VACEfron.py | Docs
A Wrapper for [vacefron.nl/api](https://vacefron.nl/api) written in Python.\
For any questions and support, you can join [VAC Efron's server](https://discord.gg/xJ2HRxZ)

## Getting Started:

To begin with, you'll have
===============================
 to install the package by doing one of the following commands:
- `pip install -U vacefron.py`
- `python -m pip -U install vacefron.py`
 
After that, you will have to create the client:

```python
import vacefron

vac_api = vacefron.Client()
```
For future reference in this documentation: when referring to 'vac_api' we refer to that above!
 
  
## Using the wrapper:
All available endpoints you can use.

### await vac_api.rank_card(username, avatar,  level, rank, current_xp, next_level_xp, previous_level_xp, custom_bg, xp_color, is_boosting)
Generate a custom Rank card for Discord bots!

**Parameters**:
- username `string` | The user's name.
- avatar `string` | The user's avatar
- level `int` | The user's current level.
- rank `int` | The user's position on the board.
- current_xp `int` | The user's current XP amount.
- next_level_xp `int` | The user's next XP amount.
- previous_level_xp `int` | The user's previous XP amount.
- custom_bg `string` | A optional background for the rank card.
- xp_color `string` | The color for the XP bar. Default to #FCBA41.
- is_boosting `bool` | If True, a boost badge will be displayed next to user's name

**Return type**: [Image](docs.md#image "Image object attributes")

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
Get an invitation to the Vacefron's server (or and the creator of this wrapper.)

**Parameters**:
- creator `boolean` | To also get an invitation to the server of creator of this wrapper.

**Return type**: string or tuple

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
