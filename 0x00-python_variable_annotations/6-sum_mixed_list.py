#!/usr/bin/env python3
"""
Defines a function that returns the sum of all integers and floats in a list
"""
from typing import Union, List


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Finds the sum of all integers and floats in a list
    """

    return sum(mxd_list)
