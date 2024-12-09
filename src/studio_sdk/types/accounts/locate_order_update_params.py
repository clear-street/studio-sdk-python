# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LocateOrderUpdateParams"]


class LocateOrderUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """The account ID or account number to update the locate order for."""

    accept: Required[bool]
    """Accept or decline the locate order."""
