# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PortfolioMargin", "Group", "GroupMember"]


class GroupMember(BaseModel):
    asset_class: Optional[Literal["other", "equity", "option", "debt"]] = None
    """The asset class of the symbol."""

    market_value: Optional[float] = None
    """Market value of the instrument."""

    market_value_percent: Optional[float] = None
    """
    The percentage market value of the instrument in terms of the total
    `net_market_value` of all positions held. Formula:
    `market_value / net_market_value`
    """

    quantity: Optional[str] = None
    """The quantity held for this instrument."""

    shocks: Optional[Dict[str, float]] = None
    """Maps shock scenarios to their resulting pnl."""

    symbol: Optional[str] = None
    """The symbol for the instrument."""


class Group(BaseModel):
    effective_requirement: float
    """The enforced margin requirement in effect for the group."""

    margin_percent: float
    """
    The percentage effective margin requirement in terms of the group market value.
    Formula: `(effective_requirement / net_market_value)`
    """

    margin_percent_contribution: float
    """
    The percentage effective margin requirement in terms of the total effective
    requirement. Formula: `(effective_requirement / sum(effective_requirement))`
    """

    market_value: float
    """The aggregated market value of all instruments for the group."""

    market_value_percent: float
    """
    The percentage market value of the group in terms of the total net_market_value
    of all positions. Formula: `(market_value / net_market_value)`
    """

    members: List[GroupMember]
    """A list of securities that comprise this group."""

    name: str
    """Unique name of the group, typically the symbol of the underlier."""

    concentration_requirement: Optional[float] = None
    """
    A component margin requirement that captures risk for the group based on gross
    exposure to total equity
    """

    discretionary_requirement: Optional[float] = None
    """
    A component margin requirement that captures miscellaneous risk factors for the
    group.
    """

    liquidity_requirement: Optional[float] = None
    """
    A component margin requirement that captures risk for the group based on
    liquidity, Market Cap, and Average Daily Volume factors.
    """

    non_marginable_requirement: Optional[float] = None
    """
    A component margin requirement that captures risk for the group that are not
    margin eligible.
    """

    regulatory_requirement: Optional[float] = None
    """Margin requirements based on OCC TIMS regulatory margin methodology"""

    risk_based_requirement: Optional[float] = None
    """
    A component margin requirement that captures base-case risk for the group under
    house margin methodology
    """

    shocks: Optional[Dict[str, float]] = None
    """Maps shock scenarios to their resulting pnl."""

    var_requirement: Optional[float] = None
    """
    Margin requirements based on value-at-risk over any 5-day period in a 2 year
    historic lookback
    """


class PortfolioMargin(BaseModel):
    add_on_requirement: Optional[float] = None
    """
    Sum of add-on margin requirements. Formula:
    `liquidity_add_on + concentration_add_on + discretionary_requirement`
    """

    add_on_requirement_percent: Optional[float] = None
    """
    The percentage add-on margin requirements in terms of total house requirement.
    Formula: `add_on_requirement / house_requirement`
    """

    concentration_add_on: Optional[float] = None
    """
    A component margin requirement that captures risk based on gross exposure to
    total equity.
    """

    concentration_add_on_percent: Optional[float] = None
    """
    The percentage concentration add-on margin requirements in terms of total house
    requirement. Formula: `concentration_add_on / house_requirement`
    """

    discretionary_requirement: Optional[float] = None
    """A component margin requirement that captures miscellaneous risk factors."""

    discretionary_requirement_percent: Optional[float] = None
    """
    The percentage discretionary margin requirements in terms of total house
    requirement Formula: `discretionary_requirement / house_requirement`
    """

    effecive_excess: Optional[float] = None
    """
    The maring amount by taking the difference between total equity and the
    effective requirement. A negative number reflects an effective margin deficit.
    """

    effective_requirement: Optional[float] = None
    """The enforced margin requirement in effect."""

    groups: Optional[List[Group]] = None
    """Portfolio margin groups"""

    house_excess: Optional[float] = None
    """
    The margin amount by taking the difference between total equity and the house
    requirement. A negative number reflects a house margin deficit.
    """

    house_requirement: Optional[float] = None
    """Margin requirements based on Clear Street's house margin methodology."""

    liquidity_add_on: Optional[float] = None
    """
    A component margin requirement that captures risk based on liquidity, Market
    Cap, and Average Daily Volume factors.
    """

    liquidity_add_on_percent: Optional[float] = None
    """
    The percentage liquidity add-on margin requirements in terms of total house
    requirement. Formula: `liquidity_add_on / house_requirement`
    """

    net_market_value: Optional[float] = None
    """Sum of market values across all positions."""

    non_marginable_requirement: Optional[float] = None
    """
    A component margin requirement that captures risk for security instruments that
    are not margin eligible.
    """

    non_marginable_requirement_percent: Optional[float] = None
    """
    The percentage non-marginable requirement in terms of total house requirement
    Formula: `non_marginable_requirement / house_requirement`
    """

    risk_based_requirement: Optional[float] = None
    """
    A component margin requirement that captures base-case risk under house margin
    methodology.
    """

    risk_based_requirement_percent: Optional[float] = None
    """
    The percentage risk_base margin requirement in terms of total house requirement
    Formula: `risk_based_requirement / house_requirement`
    """

    timestamp: Optional[int] = None
    """Timestamp of when this margin was calculated."""

    vega_requirement: Optional[float] = None
    """A component margin requirement that captures risk based on vega."""

    version: Optional[str] = None
    """Unique identifier for this margin calculation."""
