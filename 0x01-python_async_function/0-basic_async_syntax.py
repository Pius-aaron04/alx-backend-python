#!/usr/bin/env python3
"""
0-basic_async_syntax.py
Basic async syntax
"""

import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random
    """
    return random.uniform(0, max_delay)
