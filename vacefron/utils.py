from typing import Any, Dict, Tuple

from inspect import signature

from .models.rank import Rankcard


def _convert_rankcard_kwargs(**kwargs: Any) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    rankcard_init_signature = signature(Rankcard.__init__)
    invalid_kwargs = {}
    valid_kwargs = {}
    invalid_kwargs_conversions = {
        "name": "username",
        "avatar": "avatar_url",
        "custom_background": "background",
    }
    for key, value in kwargs.items():
        if key in rankcard_init_signature.parameters:
            valid_kwargs[key] = value
        else:
            maybe_valid_key = invalid_kwargs_conversions.get(key)
            if not maybe_valid_key:
                invalid_kwargs[key] = "Invalid!"
            else:
                invalid_kwargs[key] = maybe_valid_key
                valid_kwargs[maybe_valid_key] = value

    return valid_kwargs, invalid_kwargs
