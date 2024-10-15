#!/usr/bin/env python3

""" changing wait_n to task_wait_random"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


def insert_sorted(sorted_list: List[float], item: float) -> None:
    """ helper for sorting list """
    for idx, value in enumerate(sorted_list):
        if item < value:
            sorted_list.insert(idx, item)
            return
    sorted_list.append(item)


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ altering wait_n"""
    task = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*task)
    sorted_list: List[float] = []
    for result in results:
        insert_sorted(sorted_list, result)
    return sorted_list
