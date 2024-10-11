# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PnlSumListParams"]


class PnlSumListParams(TypedDict, total=False):
    ending_date: Required[int]
    """The ending date to accumulate PNL data for, inclusive."""

    starting_date: Required[int]
    """The starting date to accumulate PNL data for."""

    symbol: str
    """Filters for a specific symbol."""

    underlying_symbol: str
    """Filters for a specific underlying symbol, e.g.

    all options for a particular underlying.
    """
