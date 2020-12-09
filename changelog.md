## VACEfron.py | Changelog

See here what changed or broke each version.

---

### v1.2.0 - October 1, 2020

- Added support for new endpoints:
  [.batman_slap()](docs.md#await-vac_apibatman_slaptext-text2-batmannone-robinnone) and
  [.wolverine()](docs.md#await-vac_apiwolverineuser) .

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