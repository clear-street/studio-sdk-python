# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.accounts import locate_order_create_params, locate_order_update_params
from ...types.shared.locate_order import LocateOrder
from ...types.accounts.locate_order_list_response import LocateOrderListResponse

__all__ = ["LocateOrdersResource", "AsyncLocateOrdersResource"]


class LocateOrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LocateOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LocateOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LocateOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return LocateOrdersResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        mpid: str,
        quantity: str,
        reference_id: str,
        symbol: str,
        comments: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocateOrder:
        """
        Create locate order to borrow inventory for short-selling.

        Args:
          account_id: Account ID for the account.

          mpid: The market participant where the locate will be sent.

          quantity: String representation of quantity.

          reference_id: Your unique ID for this locate order.

          comments: Any additional comments for the locate request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/locate-orders",
            body=maybe_transform(
                {
                    "mpid": mpid,
                    "quantity": quantity,
                    "reference_id": reference_id,
                    "symbol": symbol,
                    "comments": comments,
                },
                locate_order_create_params.LocateOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocateOrder,
        )

    def retrieve(
        self,
        locate_order_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocateOrder:
        """
        Get locate order by its unique locate order ID.

        Args:
          account_id: Account ID for the account.

          locate_order_id: Locate order ID to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not locate_order_id:
            raise ValueError(f"Expected a non-empty value for `locate_order_id` but received {locate_order_id!r}")
        return self._get(
            f"/accounts/{account_id}/locate-orders/{locate_order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocateOrder,
        )

    def update(
        self,
        locate_order_id: str,
        *,
        account_id: str,
        accept: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Accept or decline locate order that has been offered.

        Args:
          account_id: Account ID for the account.

          locate_order_id: Unique locate ID assigned by us.

          accept: Accept or decline the locate order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not locate_order_id:
            raise ValueError(f"Expected a non-empty value for `locate_order_id` but received {locate_order_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/accounts/{account_id}/locate-orders/{locate_order_id}",
            body=maybe_transform({"accept": accept}, locate_order_update_params.LocateOrderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocateOrderListResponse:
        """
        List all locate orders

        Args:
          account_id: Account ID for the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/locate-orders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocateOrderListResponse,
        )


class AsyncLocateOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLocateOrdersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLocateOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLocateOrdersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return AsyncLocateOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        mpid: str,
        quantity: str,
        reference_id: str,
        symbol: str,
        comments: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocateOrder:
        """
        Create locate order to borrow inventory for short-selling.

        Args:
          account_id: Account ID for the account.

          mpid: The market participant where the locate will be sent.

          quantity: String representation of quantity.

          reference_id: Your unique ID for this locate order.

          comments: Any additional comments for the locate request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/locate-orders",
            body=await async_maybe_transform(
                {
                    "mpid": mpid,
                    "quantity": quantity,
                    "reference_id": reference_id,
                    "symbol": symbol,
                    "comments": comments,
                },
                locate_order_create_params.LocateOrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocateOrder,
        )

    async def retrieve(
        self,
        locate_order_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocateOrder:
        """
        Get locate order by its unique locate order ID.

        Args:
          account_id: Account ID for the account.

          locate_order_id: Locate order ID to get.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not locate_order_id:
            raise ValueError(f"Expected a non-empty value for `locate_order_id` but received {locate_order_id!r}")
        return await self._get(
            f"/accounts/{account_id}/locate-orders/{locate_order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocateOrder,
        )

    async def update(
        self,
        locate_order_id: str,
        *,
        account_id: str,
        accept: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Accept or decline locate order that has been offered.

        Args:
          account_id: Account ID for the account.

          locate_order_id: Unique locate ID assigned by us.

          accept: Accept or decline the locate order.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not locate_order_id:
            raise ValueError(f"Expected a non-empty value for `locate_order_id` but received {locate_order_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/accounts/{account_id}/locate-orders/{locate_order_id}",
            body=await async_maybe_transform({"accept": accept}, locate_order_update_params.LocateOrderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LocateOrderListResponse:
        """
        List all locate orders

        Args:
          account_id: Account ID for the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/locate-orders",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LocateOrderListResponse,
        )


class LocateOrdersResourceWithRawResponse:
    def __init__(self, locate_orders: LocateOrdersResource) -> None:
        self._locate_orders = locate_orders

        self.create = to_raw_response_wrapper(
            locate_orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            locate_orders.retrieve,
        )
        self.update = to_raw_response_wrapper(
            locate_orders.update,
        )
        self.list = to_raw_response_wrapper(
            locate_orders.list,
        )


class AsyncLocateOrdersResourceWithRawResponse:
    def __init__(self, locate_orders: AsyncLocateOrdersResource) -> None:
        self._locate_orders = locate_orders

        self.create = async_to_raw_response_wrapper(
            locate_orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            locate_orders.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            locate_orders.update,
        )
        self.list = async_to_raw_response_wrapper(
            locate_orders.list,
        )


class LocateOrdersResourceWithStreamingResponse:
    def __init__(self, locate_orders: LocateOrdersResource) -> None:
        self._locate_orders = locate_orders

        self.create = to_streamed_response_wrapper(
            locate_orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            locate_orders.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            locate_orders.update,
        )
        self.list = to_streamed_response_wrapper(
            locate_orders.list,
        )


class AsyncLocateOrdersResourceWithStreamingResponse:
    def __init__(self, locate_orders: AsyncLocateOrdersResource) -> None:
        self._locate_orders = locate_orders

        self.create = async_to_streamed_response_wrapper(
            locate_orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            locate_orders.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            locate_orders.update,
        )
        self.list = async_to_streamed_response_wrapper(
            locate_orders.list,
        )
