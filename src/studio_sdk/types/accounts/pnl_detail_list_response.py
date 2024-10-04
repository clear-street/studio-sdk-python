# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PnlDetailListResponse", "Data"]


class Data(BaseModel):
    account_id: str
    """Account ID for the account."""

    asset_class: Literal["other", "equity", "option", "debt"]
    """The asset class of the symbol."""

    bought_quantity: str
    """Quantity of a given instrument bought."""

    buys: int
    """Total buys of a given instrument."""

    day_pnl: float
    """Profit and loss from intraday trading activities."""

    entity_id: str
    """Name of the legal entity."""

    gross_market_value: float
    """Absolute market value of long and short market values."""

    net_market_value: float
    """Market value net of long and short market values."""

    overnight_pnl: float
    """Profit and loss from previous trading date."""

    price: float
    """Price used in this pnl calculation."""

    quantity: str
    """String representation of quantity."""

    realized_pnl: float
    """Profit and loss realized from position closing trading activity."""

    sells: int
    """Total sells of a given instrument."""

    sod_market_value: float
    """Market value of a given instrument a the start of a trading day."""

    sod_price: float
    """Price at the start of a trading day."""

    sod_quantity: str
    """Quantity of a given instrument at the start of a trading day."""

    sold_quantity: str
    """Quantity of a given instrument sold."""

    symbol: str

    symbol_description: str
    """Description of the symbol."""

    timestamp: int
    """Milliseconds since epoch."""

    total_fees: float
    """Total fees incurred from trading activities."""

    total_pnl: float
    """`realized_pnl + unrealized_pnl`"""

    underlier: str
    """The underlying instrument."""

    unrealized_pnl: float
    """Profit and loss from market changes."""


class PnlDetailListResponse(BaseModel):
    data: List[Data]
