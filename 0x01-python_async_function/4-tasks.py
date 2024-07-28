#!/usr/bin/env python3

"""
1-concurrent_coroutines.py
Concurrent coroutines with async and await
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n
    runs n coroutines concurrently with async
    """

    coroutines = [task_wait_random(max_delay) for _ in range(n)]

    delays = await asyncio.gather(*coroutines)
    for i in range(len(delays)):
        for j in range(i, len(delays)):
            if delays[i] > delays[j]:
                delays[i], delays[j] = delays[j], delays[i]
    return delays
