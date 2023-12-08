#!/usr/bin/env python3
'''create multiplier Complex functions
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a multiplier function.
    '''
    return lambda x: x * multiplier
