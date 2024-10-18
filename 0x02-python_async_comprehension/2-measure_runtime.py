#!/usr/bin/env python3


""" measuring asychronous operations """

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measuring runtime of 10 corutines with async comprehension"""
    start: float = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    stop: float = time.perf_counter()

    return (stop - start)
