# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HoldingListResponse", "Data"]


class Data(BaseModel):
    asset_class: Literal["other", "currency", "equity", "option", "debt", "fund"]
    """The asset class of the symbol."""

    quantity: str
    """The quantity held for the given symbol.

    This is an EOD quantity if querying historically, else the current real-time
    quantity for the current date.
    """

    sod_quantity: str
    """The quantity held for the given symbol at the start of the day."""

    symbol: str

    symbol_description: Optional[str] = None
    """Description of the symbol."""


class HoldingListResponse(BaseModel):
    account_id: str
    """Account ID for the account."""

    data: List[Data]

    date: int
    """Integer in YYYYMMDD representing a date."""

    sod_equity: float
    """Start of day equity."""

    eod_equity: Optional[float] = None
    """For historical holdings, the end of day equity. Omitted for real-time holdings."""

    timestamp: Optional[int] = None
    """
    For real-time holdings, the timestamp reflecting the last update made to the
    holdings data. Omitted for historical holdings.
    """
