# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["BulkOrderCreateParams", "Order"]


class BulkOrderCreateParams(TypedDict, total=False):
    orders: Required[Iterable[Order]]
    """An array of orders to create."""


class Order(TypedDict, total=False):
    order_type: Required[Literal["limit", "market"]]
    """The type of order, can be one of the following:

    - `limit`: A limit order will execute at-or-better than the limit price you
      specify
    - `market`: An order that will execute at the prevailing market prices
    """

    quantity: Required[str]
    """The maximum quantity to be executed."""

    side: Required[Literal["buy", "sell", "sell-short"]]
    """Buy, sell, sell-short indicator."""

    strategy_type: Required[Literal["sor", "dark", "ap", "pov", "twap", "vwap"]]
    """Strategy type used for execution, can be one of below.

    Note, we use sensible defaults for strategy parameters at the moment. In future,
    we will provide a way to provide specify these parameters.

    - `sor`: Smart order router
    - `dark`: Dark pool
    - `ap`: Arrival price
    - `pov`: Percentage of volume
    - `twap`: Time weighted average price
    - `vwap`: Volume weighted average price

    For more information on these strategies, please refer to our
    [documentation](https://docs.clearstreet.io/studio/docs/execution-strategies).
    """

    symbol: Required[str]
    """The symbol this order is for. See `symbol_format` for supported symbol formats."""

    time_in_force: Required[Literal["day", "ioc", "day-plus", "at-open", "at-close"]]
    """The lifecycle enforcement of this order.

    - `day`: The order will exist for the duration of the current trading session
    - `ioc`: The order will immediately be executed or cancelled
    - `day-plus`: The order will exist only for the duration the current trading
      session plus extended hours, if applicable
    - `at-open`: The order will exist only for the opening auction of the next
      session
    - `at-close`: The order will exist only for the closing auction of the current
      session
    """

    locate_broker: str
    """Name of the broker that provided you inventory for a short-sale.

    Required if `side` is `sell-short`. If you procured inventory through us, you
    can use `CLST`.
    """

    price: str
    """The price to execute at-or-better."""

    reference_id: str
    """An ID that you provide."""

    symbol_format: Literal["cms", "osi"]
    """Denotes the format of the provided `symbol` field."""
