# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["BulkOrderCreateParams", "Order", "OrderStrategy", "OrderStrategyBaseStrategy"]


class BulkOrderCreateParams(TypedDict, total=False):
    orders: Required[Iterable[Order]]
    """An array of orders to create."""


class OrderStrategyBaseStrategy(TypedDict, total=False):
    type: Required[Literal["sor", "dark", "ap", "pov", "twap", "vwap"]]
    """The type of strategy. This must be set to the respective strategy type."""

    end_at: int
    """The timestamp to stop routing, defaults to market close."""

    start_at: int
    """The timestamp to start routing, defaults to now."""

    urgency: Literal["super-passive", "passive", "moderate", "aggressive", "super-aggressive"]
    """The urgency associated with the execution strategy."""


class OrderStrategyBaseStrategy(TypedDict, total=False):
    type: Required[Literal["sor", "dark", "ap", "pov", "twap", "vwap"]]
    """The type of strategy. This must be set to the respective strategy type."""

    end_at: int
    """The timestamp to stop routing, defaults to market close."""

    start_at: int
    """The timestamp to start routing, defaults to now."""

    urgency: Literal["super-passive", "passive", "moderate", "aggressive", "super-aggressive"]
    """The urgency associated with the execution strategy."""


class OrderStrategyBaseStrategy(TypedDict, total=False):
    type: Required[Literal["sor", "dark", "ap", "pov", "twap", "vwap"]]
    """The type of strategy. This must be set to the respective strategy type."""

    end_at: int
    """The timestamp to stop routing, defaults to market close."""

    start_at: int
    """The timestamp to start routing, defaults to now."""

    urgency: Literal["super-passive", "passive", "moderate", "aggressive", "super-aggressive"]
    """The urgency associated with the execution strategy."""


class OrderStrategyBaseStrategy(TypedDict, total=False):
    type: Required[Literal["sor", "dark", "ap", "pov", "twap", "vwap"]]
    """The type of strategy. This must be set to the respective strategy type."""

    end_at: int
    """The timestamp to stop routing, defaults to market close."""

    start_at: int
    """The timestamp to start routing, defaults to now."""

    urgency: Literal["super-passive", "passive", "moderate", "aggressive", "super-aggressive"]
    """The urgency associated with the execution strategy."""


class OrderStrategyBaseStrategy(TypedDict, total=False):
    type: Required[Literal["sor", "dark", "ap", "pov", "twap", "vwap"]]
    """The type of strategy. This must be set to the respective strategy type."""

    end_at: int
    """The timestamp to stop routing, defaults to market close."""

    start_at: int
    """The timestamp to start routing, defaults to now."""

    urgency: Literal["super-passive", "passive", "moderate", "aggressive", "super-aggressive"]
    """The urgency associated with the execution strategy."""


class OrderStrategyBaseStrategy(TypedDict, total=False):
    type: Required[Literal["sor", "dark", "ap", "pov", "twap", "vwap"]]
    """The type of strategy. This must be set to the respective strategy type."""

    end_at: int
    """The timestamp to stop routing, defaults to market close."""

    start_at: int
    """The timestamp to start routing, defaults to now."""

    urgency: Literal["super-passive", "passive", "moderate", "aggressive", "super-aggressive"]
    """The urgency associated with the execution strategy."""


OrderStrategy: TypeAlias = Union[
    OrderStrategyBaseStrategy,
    OrderStrategyBaseStrategy,
    OrderStrategyBaseStrategy,
    OrderStrategyBaseStrategy,
    OrderStrategyBaseStrategy,
    OrderStrategyBaseStrategy,
]


class Order(TypedDict, total=False):
    order_type: Required[Literal["limit", "market", "stop"]]
    """The type of order, can be one of the following:

    - `limit`: A limit order will execute at-or-better than the limit price you
      specify
    - `market`: An order that will execute at the prevailing market prices
    - `stop`: A stop order will result in a market order when the market price
      reaches the specified stop price
    """

    quantity: Required[str]
    """The maximum quantity to be executed."""

    side: Required[Literal["buy", "sell", "sell-short"]]
    """Buy, sell, sell-short indicator."""

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
    """
    If you're short-selling and using an away broker for a locate, provide the
    broker name here.
    """

    price: str
    """The price to execute at-or-better for limit orders."""

    reference_id: str
    """An ID that you provide."""

    stop_price: str
    """The price at which stop orders become marketable."""

    strategy: OrderStrategy
    """The execution strategy to use for this order.

    If not provided, our smart order-router will handle execution for your order.
    """

    symbol_format: Literal["cms", "osi"]
    """Denotes the format of the provided `symbol` field."""
