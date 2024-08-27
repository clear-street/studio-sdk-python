# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..._models import BaseModel

__all__ = ["PnlSummary"]


class PnlSummary(BaseModel):
    day_pnl: float
    """Profit and loss from intraday trading activities."""

    entity_id: str
    """Entity ID for the legal entity."""

    equity: float
    """Net value of instruments held in the portfolio."""

    gross_market_value: float
    """Absolute market value of long and short market values."""

    long_market_value: float
    """Market value of securities positioned long."""

    net_market_value: float
    """Market value net of long and short market values."""

    net_pnl: float
    """`total_pnl + total_fees`"""

    overnight_pnl: float
    """Profit and loss from previous trading date."""

    realized_pnl: float
    """Profit and loss realized from position closing trading activity"""

    short_market_value: float
    """Market value of securities positioned short."""

    sod_equity: float
    """Net value of instruments held in the portfolio at the start of a trading day."""

    sod_gross_market_value: float
    """Absolute market value at the start of a trading day."""

    sod_long_market_value: float
    """Market value of securities positioned long at the start of a trading day."""

    sod_short_market_value: float
    """Market value of securities positioned short at the start of a trading day."""

    timestamp: int
    """Milliseconds since epoch."""

    total_fees: float
    """Total fees incurred from trading activities."""

    total_pnl: float
    """`realized_pnl + unrealized_pnl`"""

    unrealized_pnl: float
    """Profit and loss from market changes."""
