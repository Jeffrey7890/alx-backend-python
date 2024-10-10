#!/usr/bin/env python3

""" sum floats and int list """


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ sums a list of floats and ints """
    return (float(sum(mxd_lst)))
