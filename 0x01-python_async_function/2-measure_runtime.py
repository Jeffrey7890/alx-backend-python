#!/usr/bin/env python3

""" measuring the runtime of funcitons """

import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measring wait_n(n, max_delay) """

    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop: float = time.perf_counter()
    total_time: float = stop - start

    return (total_time / n)
