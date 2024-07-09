# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.order import Order

__all__ = ["OrderListResponse"]


class OrderListResponse(BaseModel):
    data: List[Order]

    next_page_token: Optional[str] = None
    """Cursor for the next page of results."""
