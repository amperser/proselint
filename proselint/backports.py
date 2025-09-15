"""Backport features for older versions of Python."""

from __future__ import annotations

from itertools import islice
from sys import version_info
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from collections.abc import Generator, Iterable

T = TypeVar("T")

if version_info >= (3, 13):
    from itertools import batched
else:

    def batched(
        iterable: Iterable[T], n: int, *, strict: bool = False
    ) -> Generator[tuple[T, ...]]:
        """Batch data from the `iterable` into `n`-tuples."""
        if n < 0:
            raise ValueError("n must be at least one")
        iterator = iter(iterable)
        while batch := tuple(islice(iterator, n)):
            if strict and len(batch) != n:
                raise ValueError("batched(): incomplete batch")
            yield batch


__all__ = ("batched",)
