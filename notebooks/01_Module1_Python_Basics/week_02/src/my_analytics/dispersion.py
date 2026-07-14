from __future__ import annotations
from .central_tendency import mean as _mean
import math


def variance(data: list[float], *, ddof: int = 1) -> float:
    """Return sample variance (ddof=1) or population variance (ddof=0)."""
    if len(data) < 2:
        raise ValueError("variance() requires at least 2 values")
    mu = _mean(*data)
    return sum((x - mu) ** 2 for x in data) / (len(data) - ddof)

# TODO: implement std, iqr, coefficient_of_variation