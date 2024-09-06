# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..shared.locate_order import LocateOrder

__all__ = ["LocateOrderListResponse"]


class LocateOrderListResponse(BaseModel):
    data: List[LocateOrder]
