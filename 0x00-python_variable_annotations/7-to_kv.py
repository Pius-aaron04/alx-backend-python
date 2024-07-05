#!/usr/bin/env python3
"""
Defines a function that a tuple
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns a tuple of key and value
    """
    return (k, v**2)
