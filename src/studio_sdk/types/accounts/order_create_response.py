# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..._models import BaseModel

__all__ = ["OrderCreateResponse"]


class OrderCreateResponse(BaseModel):
    order_id: str
    """An internally generated unique ID for this order."""
