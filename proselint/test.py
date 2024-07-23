from __future__ import annotations

from math import ceil
from typing import Any


def pack_into_bins(data: list[Any], limit: int) -> list[list[Any]]:
    """
    Pack `data` into equally sized bins, with a given size `limit`.

    Note that for small sets of `data`, bin size and quantity will be similar.
    """
    if (size := len(data)) <= limit:
        return [data]
    num_bins = ceil(size / limit)
    bin_size = ceil(size / num_bins)
    return [data[i * bin_size : (i + 1) * bin_size] for i in range(num_bins)]
