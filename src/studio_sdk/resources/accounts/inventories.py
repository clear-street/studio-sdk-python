# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.accounts.inventory_retrieve_response import InventoryRetrieveResponse

__all__ = ["InventoriesResource", "AsyncInventoriesResource"]


class InventoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InventoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return InventoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InventoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return InventoriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventoryRetrieveResponse:
        """
        Get located inventory for a symbol.

        Args:
          account_id: The account ID or account number to get the inventory for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/accounts/{account_id}/inventories/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryRetrieveResponse,
        )


class AsyncInventoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInventoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInventoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInventoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return AsyncInventoriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InventoryRetrieveResponse:
        """
        Get located inventory for a symbol.

        Args:
          account_id: The account ID or account number to get the inventory for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/accounts/{account_id}/inventories/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InventoryRetrieveResponse,
        )


class InventoriesResourceWithRawResponse:
    def __init__(self, inventories: InventoriesResource) -> None:
        self._inventories = inventories

        self.retrieve = to_raw_response_wrapper(
            inventories.retrieve,
        )


class AsyncInventoriesResourceWithRawResponse:
    def __init__(self, inventories: AsyncInventoriesResource) -> None:
        self._inventories = inventories

        self.retrieve = async_to_raw_response_wrapper(
            inventories.retrieve,
        )


class InventoriesResourceWithStreamingResponse:
    def __init__(self, inventories: InventoriesResource) -> None:
        self._inventories = inventories

        self.retrieve = to_streamed_response_wrapper(
            inventories.retrieve,
        )


class AsyncInventoriesResourceWithStreamingResponse:
    def __init__(self, inventories: AsyncInventoriesResource) -> None:
        self._inventories = inventories

        self.retrieve = async_to_streamed_response_wrapper(
            inventories.retrieve,
        )
