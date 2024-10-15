#!/usr/bin/env python3

""" implement the basics """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ basic async syntax """
    n = random.uniform(0, max_delay)

    await asyncio.sleep(n)
    return n
