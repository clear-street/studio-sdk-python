# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Instrument", "Symbol"]


class Symbol(BaseModel):
    symbol: Optional[str] = None

    symbol_format: Optional[Literal["cms", "osi"]] = None
    """Denotes the format of the provided `symbol` field."""


class Instrument(BaseModel):
    asset_class: Literal["other", "equity", "option", "debt"]
    """The asset class of the symbol."""

    description: str
    """A description of the instrument."""

    primary_exchange: str
    """The primary exchange for the instrument."""

    symbols: List[Symbol]
