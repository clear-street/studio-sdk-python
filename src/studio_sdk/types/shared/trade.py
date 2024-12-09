# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Trade"]


class Trade(BaseModel):
    created_at: int
    """When this trade happened in milliseconds since epoch."""

    order_id: str
    """The order ID of the order this trade occurred on."""

    price: str
    """The traded price."""

    quantity: str
    """The amount that was traded."""

    running_position: str
    """The position quantity at the time of this trade."""

    side: Literal["buy", "sell", "sell-short"]
    """The side this trade occurred on."""

    trade_id: str
    """Unique trade ID assigned by us."""

    account_id: Optional[str] = None
    """Account ID for the account."""

    account_number: Optional[str] = None
    """Account number for the account."""

    symbol: Optional[str] = None
    """The symbol this trade was for."""
