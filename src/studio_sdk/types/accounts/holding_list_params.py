# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["HoldingListParams"]


class HoldingListParams(TypedDict, total=False):
    date: int
    """The historical date to get holdings for.

    If omitted, current real-time holdings will be returned.
    """
