from __future__ import annotations
import math


def minmax(data: list[float],
           feature_range: tuple[float, float] = (0.0, 1.0)) -> list[float]:
    """Scale data to a specified feature range using min-max normalisation.

    Parameters
    ----------
    data : list of float
        Input data.
    feature_range : tuple of float, keyword-only
        Target (min, max) range. Default is (0.0, 1.0).

    Returns
    -------
    list of float
        Scaled values.

    Raises
    ------
    ValueError
        If all values are identical (zero range).
    """
    lo_data, hi_data = min(data), max(data)
    if lo_data == hi_data:
        raise ValueError("Cannot scale data with zero variance (all values identical)")
    lo_target, hi_target = feature_range
    scale = (hi_target - lo_target) / (hi_data - lo_data)
    return [round((x - lo_data) * scale + lo_target, 6) for x in data]


def zscore(data: list[float], *, ddof: int = 1) -> list[float]:
    """Standardise data using z-score (subtract mean, divide by std).

    Parameters
    ----------
    data : list of float
        Input data.
    ddof : int, keyword-only
        Delta degrees of freedom. 0 = population std, 1 = sample std.

    Returns
    -------
    list of float
        Standardised values with mean ~ 0 and std ~ 1.
    """
    n    = len(data)
    mu   = sum(data) / n
    std  = math.sqrt(sum((x - mu) ** 2 for x in data) / (n - ddof))
    if std == 0:
        return [0.0] * n
    return [round((x - mu) / std, 6) for x in data]