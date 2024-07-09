# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["InstrumentRetrieveParams"]


class InstrumentRetrieveParams(TypedDict, total=False):
    symbol_format: Literal["cms", "osi"]
    """The format of the provided symbol."""
