import itertools
import typing
from typing import Tuple, Generator


def generate_sublists(gen: typing.Iterable, n: int, truncate: bool = False) -> Generator[Tuple, None, None]:
    iterations = [iter(gen)] * n
    sublister = itertools.zip_longest(*iterations)
    if truncate:
        for sublist in sublister:
            yield tuple(x for x in sublist if x is not None)
    else:
        yield from sublister
