# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["BulkOrderCreateResponse", "Data"]


class Data(BaseModel):
    submitted: bool
    """True if the order was submitted successfully, false otherwise."""

    order_id: Optional[str] = None
    """If the order was submitted, the order ID assigned to this order.

    Empty if the order was rejected.
    """

    reason: Optional[str] = None
    """If the order rejected, the reason for rejection.

    Empty if the order was accepted.
    """


class BulkOrderCreateResponse(BaseModel):
    data: List[Data]
    """Array indicating whether each respective order was submitted or not.

    This array is guaranteed to be sorted in the same order as the orders you
    provided in your request.
    """

    rejected: int
    """Total number of orders rejected"""

    submitted: int
    """Total number of orders submitted"""
