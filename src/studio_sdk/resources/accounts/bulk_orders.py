# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.accounts import bulk_order_create_params
from ...types.accounts.bulk_order_create_response import BulkOrderCreateResponse

__all__ = ["BulkOrdersResource", "AsyncBulkOrdersResource"]


class BulkOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return BulkOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return BulkOrdersResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        orders: Iterable[bulk_order_create_params.Order],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkOrderCreateResponse:
        """Creates multiple orders in a single request, up to 1000.

        Note that a successful
        call to this endpoint does not necessarily mean your orders have been accepted,
        e.g. a downstream venue might reject your order. You should therefore utilize
        our WebSocket APIs to listen for changes in order lifecycle events.

        The response will contain an array of objects, indicating whether your order was
        submitted. If the order was submitted, the `order_id` field will be populated
        with the order ID assigned to this order. If the order was rejected, the
        `reason` field will be populated with the reason for rejection. The data array
        returned in the response object is guaranteed to be ordered in the same order as
        the orders you provided in the request. Again, note that even if your order was
        submitted, that doesn't mean it was _accepted_, and may still be rejected by
        downstream venues.

        Args:
          account_id: Account ID for the account.

          orders: An array of orders to create.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/bulk-orders",
            body=maybe_transform({"orders": orders}, bulk_order_create_params.BulkOrderCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOrderCreateResponse,
        )


class AsyncBulkOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return AsyncBulkOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        orders: Iterable[bulk_order_create_params.Order],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkOrderCreateResponse:
        """Creates multiple orders in a single request, up to 1000.

        Note that a successful
        call to this endpoint does not necessarily mean your orders have been accepted,
        e.g. a downstream venue might reject your order. You should therefore utilize
        our WebSocket APIs to listen for changes in order lifecycle events.

        The response will contain an array of objects, indicating whether your order was
        submitted. If the order was submitted, the `order_id` field will be populated
        with the order ID assigned to this order. If the order was rejected, the
        `reason` field will be populated with the reason for rejection. The data array
        returned in the response object is guaranteed to be ordered in the same order as
        the orders you provided in the request. Again, note that even if your order was
        submitted, that doesn't mean it was _accepted_, and may still be rejected by
        downstream venues.

        Args:
          account_id: Account ID for the account.

          orders: An array of orders to create.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/bulk-orders",
            body=await async_maybe_transform({"orders": orders}, bulk_order_create_params.BulkOrderCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkOrderCreateResponse,
        )


class BulkOrdersResourceWithRawResponse:
    def __init__(self, bulk_orders: BulkOrdersResource) -> None:
        self._bulk_orders = bulk_orders

        self.create = to_raw_response_wrapper(
            bulk_orders.create,
        )


class AsyncBulkOrdersResourceWithRawResponse:
    def __init__(self, bulk_orders: AsyncBulkOrdersResource) -> None:
        self._bulk_orders = bulk_orders

        self.create = async_to_raw_response_wrapper(
            bulk_orders.create,
        )


class BulkOrdersResourceWithStreamingResponse:
    def __init__(self, bulk_orders: BulkOrdersResource) -> None:
        self._bulk_orders = bulk_orders

        self.create = to_streamed_response_wrapper(
            bulk_orders.create,
        )


class AsyncBulkOrdersResourceWithStreamingResponse:
    def __init__(self, bulk_orders: AsyncBulkOrdersResource) -> None:
        self._bulk_orders = bulk_orders

        self.create = async_to_streamed_response_wrapper(
            bulk_orders.create,
        )
