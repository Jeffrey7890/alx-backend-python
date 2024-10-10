#!/usr/bin/env python3

""" make multiplier using callable """


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ multiply with multiplier """
    return (lambda x: x * multiplier)
