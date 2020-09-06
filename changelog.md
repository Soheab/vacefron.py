## VACEfron.py | Changelog
See here what changed or broke each version.

---

### v1.1.2 - September 6, 2020
- Added "User-Agent"
- Better README.md
- Added examples to docs.md
- Added dates to changelog.md

### v1.1.1 - September 3, 2020
- `.rank_card()` now returns a [RankCard](docs.md#rankcard) object, so you can access the provided attributes, see
 them in the [docs](docs.md). `.read()` should still work the same

### v1.1.0 - August 18, 2020
- Added support for new endpoint `.distracted_bf()`. See the [Docs](docs.md#await-vac_apidistracted_bfboyfriend-girlfriend-woman) for it.
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