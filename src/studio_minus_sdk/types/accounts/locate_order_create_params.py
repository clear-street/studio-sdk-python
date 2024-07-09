# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LocateOrderCreateParams"]


class LocateOrderCreateParams(TypedDict, total=False):
    mpid: Required[str]
    """The market participant where the locate will be sent."""

    quantity: Required[str]
    """String representation of quantity."""

    reference_id: Required[str]
    """Your unique ID for this locate order."""

    symbol: Required[str]

    comments: str
    """Any additional comments for the locate request."""
