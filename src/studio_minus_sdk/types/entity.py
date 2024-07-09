# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Entity"]


class Entity(BaseModel):
    client_code: str

    entity_id: str
    """Entity ID for the legal entity."""

    legal_name: Optional[str] = None
