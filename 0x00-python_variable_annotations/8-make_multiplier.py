#!/usr/bin/env python3
"""
Defines a function that returns a function that multiplies
a multiplier by another float
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function
    """

    def multiply(num: float) -> float:
        """
        multiplies num by multiplier
        """

        return num * multiplier

    return multiply
