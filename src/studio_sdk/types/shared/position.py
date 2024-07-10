# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Position"]


class Position(BaseModel):
    account_id: Optional[str] = None
    """Account ID for the account."""

    quantity: Optional[str] = None
    """String representation of quantity."""

    symbol: Optional[str] = None
