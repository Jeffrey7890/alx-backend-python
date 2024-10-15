#!/usr/bin/env python3

""" concurrent coroutine """

import asyncio
import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


def insert_sorted(sorted_list: List[float], item: float) -> None:
    """ helper for sorting list """
    for idx, value in enumerate(sorted_list):
        if item < value:
            sorted_list.insert(idx, item)
            return
    sorted_list.append(item)


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait_n concurrent coroutine """
    task = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*task)
    sorted_list: List[float] = []
    for result in results:
        insert_sorted(sorted_list, result)
    return sorted_list
