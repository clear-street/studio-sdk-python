# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RegtMarginSimulationCreateParams", "Price", "Trade"]


class RegtMarginSimulationCreateParams(TypedDict, total=False):
    name: Required[str]
    """A name for this simulation for reference."""

    ignore_existing: bool
    """
    If true, the simulation will ignore any existing positions and balances in the
    account. Set to true if you want to simulate from a clean slate, i.e. an empty
    account.
    """

    prices: Iterable[Price]
    """List of prices to use in the simulation, i.e.

    fair-market-values you specify for each symbol. If this is not provided, current
    market prices will be used, if they are available.
    """

    trades: Iterable[Trade]
    """List of hypothetical trades to include in the simulation, if any."""


class Price(TypedDict, total=False):
    price: Required[str]
    """The price to use in the simulation."""

    symbol: Required[str]
    """The symbol for the instrument."""

    symbol_format: Literal["cms", "osi"]
    """Denotes the format of the provided `symbol` field."""


class Trade(TypedDict, total=False):
    price: Required[str]
    """The price of the simulated trade."""

    quantity: Required[str]
    """The quantity of the simulated trade."""

    side: Required[Literal["buy", "sell"]]
    """The side of the simulated trade."""

    symbol: Required[str]
    """The symbol for the instrument."""

    symbol_format: Literal["cms", "osi"]
    """Denotes the format of the provided `symbol` field."""
