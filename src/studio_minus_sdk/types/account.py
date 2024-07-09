# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from .._models import BaseModel

__all__ = ["Account"]


class Account(BaseModel):
    account_id: str
    """Account ID for the account."""

    entity_id: str
    """Entity ID for the legal entity."""

    name: str
