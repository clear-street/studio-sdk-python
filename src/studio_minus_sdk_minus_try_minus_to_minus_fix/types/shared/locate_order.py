# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["LocateOrder"]


class LocateOrder(BaseModel):
    account_id: str
    """Account ID for the account."""

    locate_order_id: str
    """Unique locate ID assigned by us."""

    mpid: str
    """Unique MPID assigned by us."""

    requested_at: int
    """The timestamp indicating when the locate order was requested."""

    requested_quantity: str
    """String representation of quantity."""

    status: Literal["pending", "offered", "filled", "rejected", "declined", "expired", "cancelled"]
    """The status of the locate order."""

    symbol: str

    updated_at: int
    """The timestamp indicating when the locate order was last updated."""

    borrow_rate: Optional[str] = None
    """The rate charged if the instrument is held overnight."""

    desk_comment: Optional[str] = None
    """Comment from the desk."""

    expires_at: Optional[int] = None
    """The timestamp indicating when the locate-order will expire."""

    locate_id: Optional[str] = None
    """The locate ID, available once the locate order has been offered"""

    located_at: Optional[int] = None
    """The timestamp indicating when the locate-order was located."""

    located_quantity: Optional[str] = None
    """The quantity that has been located."""

    reference_id: Optional[str] = None
    """The reference ID provided by you."""

    total_cost: Optional[str] = None
    """The total cost of the locate."""

    trader_comment: Optional[str] = None
    """Comment from the trader."""
