# VACEfron.py | Changelog
See here what changed or broke each version.

## 1.1.1
- `.rank_card()` now returns a [RankCard](docs.md#rankcard) object, so you can access the provided attributes, see
 them in the [docs](docs.md). `.read()` should still work.

## v1.1.0
- Added support for new endpoint `.distracted_bf()`. See the [Docs](docs.md#await-vac_apidistracted_bfboyfriend-girlfriend-woman) for it.
- Renamed `image.py` to `classes.py`
- Added a RankCard class, nothing interesting, keep using `.rank_card()`.
- You can now easily get the version by doing `.__version__`.

## v1.0.2
- docs.md and README.md improvements. New version to update it on PyPi.

## v1.0.1
- Added an optional `session` param to `vacefron.Client()`.
- Renamed `_session` to `session`

## v1.0.0
First release, yes.