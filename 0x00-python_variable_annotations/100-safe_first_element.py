#!/usr/bin/env python3
"""
COntains an annotated function that takes a
sequence
"""
from typing import Sequence, Union, Any, NoneType


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, NoneType]:
    if lst:
        return lst[0]
    else:
        return None
