# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["LocateOrderUpdateParams"]


class LocateOrderUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID for the account."""

    accept: Required[bool]
    """Accept or decline the locate order."""
