## VACEfron.py | Changelog

See here what changed or broke each version.

---

## v2.0.2 - December 30, 2022

- Added support for following new badges: ACTIVE_DEVELOPER, CERTIFIED_MODERATOR and SERVER_OWNER.
- Added alias `Badge` to `Badges`.

## v2.0.1 - November 12, 2022

- Fix a bug where /models and /types weren't in the package
- Remove some not used code
- Cleaned up the code
- Remove leftover debug code
- Corrected `__license__` to MLP-2.0 and `__author__` to Soheab

## v2.0.0 - November 11, 2022
Big rewrite with lots of changes. See the commit on GitHub for more details: https://github.com/Soheab/vacefron.py
Might write logs later idk.

- Add support for new endpoint: `/peeposign`
- Add fixes for `/rankcard` with badges and more.
- Rewritten the docs to be more readable and easier to understand... i think.

### v1.6.3 - December 12, 2021

- Added support for a new endpoint: [.adios()](docs.md#await-vac_apiadiosuser). See more in the docs.

### v1.6.2 - March 10, 2021

- Little fix for `.rank_card()` returned a BadRequest in some cases when avatar had a specific size.
  
### v1.6.1 - January 25, 2021

- Changes for [.rank_card()](docs.md#rank-card): rank and level are now optional and are now kwargs (KeyWordArguments), 
  same for custom_background, xp_color, is_boosting and circle_avatar

### v1.6.0 - January 9, 2021

- Added support for a new endpoint: [.drip()](docs.md#await-vac_apidripuser). See more in the docs.
- Fixed hyperlinks to docs and others for PyPi's description.

### v1.5.1 - January 8, 2021

- Added support for `circle_avatar` arg in [.rank_card()](docs.md#rank-card). See more in the docs.
- Added one alias: `rankcard()` -> [`.rank_card()`](docs.md#rank-card)

### v1.5.0 - January 5, 2021

- Added support for new endpoints:
  [.dock_of_shame()](docs.md#await-vac_apidock_of_shameuser) and
  [.woman_yelling_at_cat()](docs.md#await-vac_apiwoman_yelling_at_catwoman-cat) . See more in the docs.
- Added some aliases:
    - `womanyellingatcat()` -> [`.woman_yelling_at_cat()`](docs.md#await-vac_apiwoman_yelling_at_catwoman-cat)
    - `icanmilkyou()` -> [`.i_can_milk_you()`](docs.md#await-vac_apii_can_milk_youuser-user2--none)
    - `iamspeed()` -> [`.iam_speed()`](docs.md#await-vac_apiiam_speeduser)
    - `emergencymeeting()` -> [`.emergency_meeting()`](docs.md#await-vac_apiemergency_meetingtext)
    - `changemymind()` -> [`.change_my_mind()`](docs.md#await-vac_apichange_my_mindtext)
    - `carreverse()` -> [`.car_reverse()`](docs.md#await-vac_apicar_reversetext)
    - `dockofshame()` -> [`.dock_of_shame()`](docs.md#await-vac_apidock_of_shameuser)
    - `distractedbf()` -> [`.distracted_bf()`](docs.md#await-vac_apidistracted_bfboyfriend-girlfriend-woman)
    - `batmanslap()` -> [`.batman_slap()`](docs.md#await-vac_apibatman_slaptext-text2-batmannone-robinnone)
    - `firsttime()` -> [`.first_time()`](docs.md#await-vac_apifirst_timeuser)

### v1.4.0 - December 9, 2020

- Added support for new endpoints:
  [.batman_slap()](docs.md#await-vac_apibatman_slaptext-text2-batmannone-robinnone) and
  [.wolverine()](docs.md#await-vac_apiwolverineuser) . See more in the docs.

### v1.3.0 - October 25, 2020

- Added support for `not_stonks` for `.stonks()` endpoint. See more
  in [docs](docs.md#await-vac_apistonksuser-not_stonks).
- Added [CrewMateColors enum](docs.md#crewmatecolors) for `.ejected()`
- Added an optional `loop` param to `vacefron.Client()`

### v1.2.2 - October 9, 2020

- Fix TypeError from `urllib.parse.quote()`.
- Stop using `urllib.parse.quote()` on an image url.
- Fix `.npc()`.
- `str()` everything.

### v1.2.1 - October 6, 2020

- changed param `imposter` of `.ejected()` to `impostor`, imposter still exists but use new one instead.
- `custom_background` param of `.rank_card()`  can now accept a hex value instead of an image.

### v1.2.0 - October 1, 2020

- Added support for new endpoints:
  [.emergency_meeting()](docs.md#await-vac_apiemergency_meetingtext) and
  [.ejected()](docs.md#await-alex_apiejectedname-crewmate-impostor) .
- Better README.md.
- Added examples to docs.md.
- Added dates to changelog.md.
- Now using urllib.parse to parse text.
- Added `bytesio=True` to `Image.read()` set it to False if you want the bytes returned instead of an io.BytesIO object.

### v1.1.1 - September 3, 2020

- `.rank_card()` now returns a [RankCard](docs.md#rankcard) object, so you can access the provided attributes, see them
  in the [docs](docs.md). `.read()` should still work the same.

### v1.1.0 - August 18, 2020

- Added support for new endpoint `.distracted_bf()`. See
  the [Docs](docs.md#await-vac_apidistracted_bfboyfriend-girlfriend-woman) for it.
- Renamed `image.py` to `classes.py`
- Added a RankCard class, nothing interesting, keep using `.rank_card()`
- You can now easily get the version by doing `.__version__`

### v1.0.2 - August 12, 2020

- docs.md and README.md improvements. New version to update it on PyPi

### v1.0.1 - August 8, 2020

- Added an optional `session` param to `vacefron.Client()`
- Renamed `_session` to `session`

### v1.0.0 - August 6, 2020

First release, yes.