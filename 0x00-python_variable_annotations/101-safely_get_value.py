#!/usr/bin/env python3
"""
Contains a function that gets a value from a dictionary
"""

from typing import Mapping, NoneType, Union, Any


def safely_get_values(dct: Mapping, key: Any,
                      default: NoneType = None) -> Union[Any, NoneType]:
    """
    Safely gets the value of a key in a dictionary
    """

    if key in dct:
        return dct[key]
    else:
        return default
