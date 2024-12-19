# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ..._models import BaseModel

__all__ = ["Position"]


class Position(BaseModel):
    account_id: str
    """Account ID for the account."""

    account_number: str
    """Account number for the account."""

    average_cost: float
    """The average cost of the position."""

    quantity: str
    """String representation of quantity."""

    symbol: str
