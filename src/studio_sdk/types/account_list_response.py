# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .account import Account
from .._models import BaseModel

__all__ = ["AccountListResponse"]


class AccountListResponse(BaseModel):
    data: Optional[List[Account]] = None
