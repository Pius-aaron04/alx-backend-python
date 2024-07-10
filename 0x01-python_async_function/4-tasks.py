#!/usr/bin/env python3

"""
1-concurrent_coroutines.py
Concurrent coroutines with async and await
"""
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    wait_n
    runs n coroutines concurrently with async
    """

    coroutines = [task_wait_random(max_delay) for _ in range(n)]

    return sorted(await asyncio.gather(*coroutines))
