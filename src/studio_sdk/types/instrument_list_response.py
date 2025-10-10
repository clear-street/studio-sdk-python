# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .instrument import Instrument

__all__ = ["InstrumentListResponse"]


class InstrumentListResponse(BaseModel):
    data: Optional[List[Instrument]] = None
