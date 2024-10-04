# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["BaseStrategy"]


class BaseStrategy(BaseModel):
    type: Literal["sor", "dark", "ap", "pov", "twap", "vwap", "dma"]
    """The type of strategy. This must be set to the respective strategy type."""

    end_at: Optional[int] = None
    """The timestamp to stop routing, defaults to market close."""

    start_at: Optional[int] = None
    """The timestamp to start routing, defaults to now."""

    urgency: Optional[Literal["super-passive", "passive", "moderate", "aggressive", "super-aggressive"]] = None
    """The urgency associated with the execution strategy."""
