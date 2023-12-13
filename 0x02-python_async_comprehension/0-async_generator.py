#!/usr/bin/env python3
'''Async Generator task 0
'''
import asyncio
import random
import typing


async def async_generator()->typing.Generator[float, None, None]:
    '''coroutine loop asynchronously with
    wait 1 second then yield a random number between 0 and 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
