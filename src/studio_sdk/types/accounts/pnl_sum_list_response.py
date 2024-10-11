# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PnlSumListResponse", "Data"]


class Data(BaseModel):
    asset_class: Optional[Literal["other", "currency", "equity", "option", "debt", "fund"]] = None
    """The asset class of the symbol."""

    bought_notional: Optional[float] = None
    """Sum of the notional bought."""

    bought_quantity: Optional[str] = None
    """Sum of quantity bought."""

    day_pnl: Optional[float] = None
    """
    Sum of profit and loss from intraday trading activities for the given date range
    """

    position_pnl: Optional[float] = None
    """Sum of profit and loss from previous trading date."""

    realized_pnl: Optional[float] = None
    """Sum of profit and loss realized from position closing trading activity."""

    sold_notional: Optional[float] = None
    """Sum of the notional sold."""

    sold_quantity: Optional[str] = None
    """Sum of quantity sold."""

    symbol: Optional[str] = None

    total_pnl: Optional[float] = None
    """`realized_pnl + unrealized_pnl`"""

    unrealized_pnl: Optional[float] = None
    """Sum of profit and loss from market changes."""


class PnlSumListResponse(BaseModel):
    account_id: Optional[str] = None
    """Account ID for the account."""

    data: Optional[List[Data]] = None

    day_pnl: Optional[float] = None
    """
    Sum of profit and loss from intraday trading activities for the given date range
    across all symbols.
    """

    ending_date: Optional[int] = None
    """Echoed back from the provided query param."""

    ending_equity: Optional[float] = None
    """The equity at the end of the date range.

    End of day equity of the ending date in the date range.
    """

    entity_id: Optional[str] = None
    """Entity ID for the legal entity."""

    position_pnl: Optional[float] = None
    """Sum of profit and loss from previous trading date across all symbols."""

    realized_pnl: Optional[float] = None
    """
    Sum of profit and loss realized from position closing trading activity across
    all symbols.
    """

    starting_date: Optional[int] = None
    """Echoed back from the provided query param."""

    starting_equity: Optional[float] = None
    """The equity at the start of the date range.

    Start of day equity of the starting date in the date range.
    """

    symbol: Optional[str] = None
    """Echoed back from the provided query param."""

    total_pnl: Optional[float] = None
    """`realized_pnl + unrealized_pnl`"""

    underlying_symbol: Optional[str] = None
    """Echoed back from the provided query param."""

    unrealized_pnl: Optional[float] = None
    """Sum of profit and loss from market changes across all symbols."""
