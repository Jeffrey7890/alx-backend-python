#!/usr/bin/env python3

""" annotate a given function """


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ annotating a function """
    return [(i, len(i)) for i in lst]
