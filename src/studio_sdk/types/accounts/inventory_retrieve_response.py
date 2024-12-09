# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["InventoryRetrieveResponse"]


class InventoryRetrieveResponse(BaseModel):
    account_id: Optional[str] = None
    """Account ID for the account."""

    account_number: Optional[str] = None
    """Account number for the account."""

    available: Optional[str] = None
    """String representation of quantity."""

    reserved: Optional[str] = None
    """String representation of quantity."""

    symbol: Optional[str] = None

    used: Optional[str] = None
    """String representation of quantity."""
