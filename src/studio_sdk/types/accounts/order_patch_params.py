# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrderPatchParams"]


class OrderPatchParams(TypedDict, total=False):
    account_id: Required[str]
    """The account ID or account number to attempt to update the order for."""

    quantity: Required[str]
    """The maximum quantity to be executed."""

    price: str
    """The price to execute at-or-better for limit orders."""

    stop_price: str
    """The price at which stop orders become marketable."""
