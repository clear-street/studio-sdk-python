# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TradeListParams"]


class TradeListParams(TypedDict, total=False):
    page_size: int
    """Number of trades to return per page."""

    page_token: str
    """Cursor for the page to return."""
