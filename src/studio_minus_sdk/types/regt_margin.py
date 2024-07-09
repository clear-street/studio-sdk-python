# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RegtMargin", "Group", "GroupMember"]


class GroupMember(BaseModel):
    asset_class: Literal["other", "equity", "option", "debt"]
    """The asset class of the symbol."""

    market_value: float
    """Market value of the instrument."""

    market_value_percent: float
    """
    The percentage market value of the instrument in terms of the total
    `net_market_value` of all positions held. Formula:
    `market_value / net_market_value`
    """

    quantity: str
    """The quantity held for this instrument."""

    symbol: str
    """The symbol for the instrument."""


class Group(BaseModel):
    effective_requirement: float
    """The enforced margin requirement in effect for the symbol group."""

    exchange_requirement: float
    """Margin requirements based on regulatory rules for the symbol group."""

    house_requirement: float
    """
    Margin requirements based on Clear Street's house margin methodology for the
    symbol group.
    """

    margin_percent: float
    """
    The percentage effective margin requirement in terms of the symbol group market
    value. Formula: `(effective_requirement / net_market_value)`
    """

    margin_percent_contribution: float
    """
    The percentage effective margin requirement in terms of the total effective
    requirement. Formula: `(effective_requirement / sum(effective_requirement))`
    """

    market_value: float
    """The aggregated market value of all instruments for the symbol group."""

    market_value_percent: float
    """
    The percentage market value of the symbol group in terms of the total
    net_market_value of all positions. Formula: `(market_value / net_market_value)`
    """

    members: List[GroupMember]
    """A list of securities that comprise this group."""

    name: str
    """Unique name of the group, typically the symbol of the underlier."""


class RegtMargin(BaseModel):
    day_trade_buying_power: float
    """
    The remaining amount of start_of_day_buying_power that captures any day-trading
    activity.
    """

    effective_requirement: float
    """The enforced margin requirement in effect."""

    exchange_requirement: float
    """Margin requirements based on regulatory rules."""

    groups: List[Group]
    """Reg-T margin groups"""

    house_excess: float
    """
    The margin amount by taking the difference between total equity and the house
    requirement. A negative number reflects a house margin deficit.
    """

    house_requirement: float
    """Margin requirements based on Clear Street's house margin methodology."""

    net_market_value: float
    """Market value net of long and short market values."""

    overnight_buying_power: float
    """
    The limit, or "up-to" amount, of securities value that can be purchased and held
    overnight.
    """

    sma: float
    """Special Memorandum Account (SMA).

    The regulatory line of credit amount for margin trading based on market value,
    trading activity, and available cash.
    """

    sod_buying_power: float
    """
    The limit, or "up-to" amount, of securities value that can be day-traded for a
    given trading day.
    """

    timestamp: int
    """Timestamp of when this margin was calculated."""

    version: str
    """Unique identifier for this margin calculation."""

    effective_excess: Optional[float] = None
    """
    The maring amount by taking the difference between total equity and the
    effective requirement. A negative number reflects an effective margin deficit.
    """

    exchange_excess: Optional[float] = None
    """
    The margin amount by taking the difference between total equity and the exchange
    requirement. A negative number reflects an regulatory margin deficit.
    """
