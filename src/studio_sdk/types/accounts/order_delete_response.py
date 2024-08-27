# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["OrderDeleteResponse"]


class OrderDeleteResponse(BaseModel):
    data: List[str]
    """Array of order IDs that were attempted to be cancelled."""
