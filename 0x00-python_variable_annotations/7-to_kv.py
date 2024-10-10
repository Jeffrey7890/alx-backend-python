#!/usr/bin/env python3

""" complex types -strings and int /float to tuple """


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """  string and square of k and v """
    return (k, float(v * v))
