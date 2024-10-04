# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BaseStrategy"]


class BaseStrategy(TypedDict, total=False):
    type: Required[Literal["sor", "dark", "ap", "pov", "twap", "vwap", "dma"]]
    """The type of strategy. This must be set to the respective strategy type."""

    end_at: int
    """The timestamp to stop routing, defaults to market close."""

    start_at: int
    """The timestamp to start routing, defaults to now."""

    urgency: Literal["super-passive", "passive", "moderate", "aggressive", "super-aggressive"]
    """The urgency associated with the execution strategy."""
