# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .entity import Entity
from .._models import BaseModel

__all__ = ["EntityListResponse"]


class EntityListResponse(BaseModel):
    data: Optional[List[Entity]] = None
