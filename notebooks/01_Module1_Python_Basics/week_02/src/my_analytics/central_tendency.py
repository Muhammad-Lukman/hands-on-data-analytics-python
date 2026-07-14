from __future__ import annotations

def mean(*values: float) -> float:
    """Return the arithmetic mean of any number of numeric values.

    Parameters
    ----------
    *values : float
        One or more numeric values.

    Returns
    -------
    float
        Arithmetic mean.

    Raises
    ------
    ValueError
        If no values are provided.

    Examples
    --------
    >>> mean(1, 2, 3, 4, 5)
    3.0
    >>> mean(10, 20)
    15.0
    """
    if not values:
        raise ValueError("mean() requires at least one value")
    return sum(values) / len(values)


def median(data: list[float]) -> float:
    """Return the median of a sorted or unsorted list.

    Parameters
    ----------
    data : list of float
        Input data.

    Returns
    -------
    float
        Median value.

    Raises
    ------
    ValueError
        If data is empty.
    """
    if not data:
        raise ValueError("median() requires at least one value")
    srt = sorted(data)
    n   = len(srt)
    mid = n // 2
    return srt[mid] if n % 2 else (srt[mid - 1] + srt[mid]) / 2


def mode(data: list) -> list:
    """Return the mode(s) of a list (may be multimodal).

    Parameters
    ----------
    data : list
        Input data (any comparable type).

    Returns
    -------
    list
        List of most frequent value(s).
    """
    if not data:
        raise ValueError("mode() requires at least one value")
    freq     = {v: data.count(v) for v in set(data)}
    max_freq = max(freq.values())
    return [v for v, c in freq.items() if c == max_freq]