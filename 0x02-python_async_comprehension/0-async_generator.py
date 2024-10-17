#!/usr/bin/env python3


""" Asynchronouse generators """

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """ async generator yield 0-10 """
    for i in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
