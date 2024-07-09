# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..shared.position import Position

__all__ = ["PositionListResponse"]


class PositionListResponse(BaseModel):
    data: List[Position]

    next_page_token: Optional[str] = None
    """Cursor for the next page of results."""
