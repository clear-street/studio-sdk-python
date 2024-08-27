# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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
from ...types.accounts import order_list_params, order_create_params, order_delete_params
from ...types.accounts.order_list_response import OrderListResponse
from ...types.accounts.order_create_response import OrderCreateResponse
from ...types.accounts.order_delete_response import OrderDeleteResponse
from ...types.accounts.order_retrieve_response import OrderRetrieveResponse

__all__ = ["OrdersResource", "AsyncOrdersResource"]


class OrdersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OrdersResourceWithRawResponse:
        return OrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrdersResourceWithStreamingResponse:
        return OrdersResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: str,
        *,
        order_type: Literal["limit", "market", "stop"],
        quantity: str,
        side: Literal["buy", "sell", "sell-short"],
        symbol: str,
        time_in_force: Literal["day", "ioc", "day-plus", "at-open", "at-close"],
        locate_broker: str | NotGiven = NOT_GIVEN,
        price: str | NotGiven = NOT_GIVEN,
        reference_id: str | NotGiven = NOT_GIVEN,
        stop_price: str | NotGiven = NOT_GIVEN,
        strategy: order_create_params.Strategy | NotGiven = NOT_GIVEN,
        symbol_format: Literal["cms", "osi"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderCreateResponse:
        """Creates a new order and sends to our internal systems for execution.

        Note that a
        successful call to this endpoint does not necessarily mean your order has been
        accepted, e.g. a downstream venue might reject your order. You should therefore
        utilize our WebSocket APIs to listen for changes in order lifecycle events.

        Args:
          account_id: Account ID for the account.

          order_type:
              The type of order, can be one of the following:

              - `limit`: A limit order will execute at-or-better than the limit price you
                specify
              - `market`: An order that will execute at the prevailing market prices
              - `stop`: A stop order will result in a market order when the market price
                reaches the specified stop price

          quantity: The maximum quantity to be executed.

          side: Buy, sell, sell-short indicator.

          symbol: The symbol this order is for. See `symbol_format` for supported symbol formats.

          time_in_force: The lifecycle enforcement of this order.

              - `day`: The order will exist for the duration of the current trading session
              - `ioc`: The order will immediately be executed or cancelled
              - `day-plus`: The order will exist only for the duration the current trading
                session plus extended hours, if applicable
              - `at-open`: The order will exist only for the opening auction of the next
                session
              - `at-close`: The order will exist only for the closing auction of the current
                session

          locate_broker: If you're short-selling and using an away broker for a locate, provide the
              broker name here.

          price: The price to execute at-or-better for limit orders.

          reference_id: An ID that you provide.

          stop_price: The price at which stop orders become marketable.

          strategy: The execution strategy to use for this order. If not provided, our smart
              order-router will handle execution for your order.

          symbol_format: Denotes the format of the provided `symbol` field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/orders",
            body=maybe_transform(
                {
                    "order_type": order_type,
                    "quantity": quantity,
                    "side": side,
                    "symbol": symbol,
                    "time_in_force": time_in_force,
                    "locate_broker": locate_broker,
                    "price": price,
                    "reference_id": reference_id,
                    "stop_price": stop_price,
                    "strategy": strategy,
                    "symbol_format": symbol_format,
                },
                order_create_params.OrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderCreateResponse,
        )

    def retrieve(
        self,
        order_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderRetrieveResponse:
        """
        Get an order that was previously created.

        Args:
          account_id: Account ID for the account.

          order_id: Unique order ID assigned by us.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return self._get(
            f"/accounts/{account_id}/orders/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderRetrieveResponse,
        )

    def list(
        self,
        account_id: str,
        *,
        from_: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        to: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderListResponse:
        """
        List orders for a given account for the current trading day, filtered on the
        given query parameters.

        Args:
          account_id: Account ID for the account.

          from_: Milliseconds since epoch timestamp. This will constrain the search for orders
              created after this timestamp, inclusively. Timestamps for orders prior the
              current trading day will be ignored.

          page_size: Number of orders to return per page.

          page_token: Cursor for the page to return.

          to: Milliseconds since epoch timestamp. This will constrain the search for orders
              created before this timestamp, inclusively. Timestamps for orders beyond the
              current trading day will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/orders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "page_size": page_size,
                        "page_token": page_token,
                        "to": to,
                    },
                    order_list_params.OrderListParams,
                ),
            ),
            cast_to=OrderListResponse,
        )

    def delete(
        self,
        account_id: str,
        *,
        symbol: str | NotGiven = NOT_GIVEN,
        symbol_format: Literal["cms", "osi"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderDeleteResponse:
        """Attempts to cancel all open orders for a given account.

        Cancelling an order
        cannot be guaranteed as there might be in-flight executions.

        Args:
          account_id: Account ID for the account.

          symbol: Cancel orders only for this specific symbol. If this is omitted, all open orders
              will be cancelled.

          symbol_format: Format of the provided symbol.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            f"/accounts/{account_id}/orders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbol": symbol,
                        "symbol_format": symbol_format,
                    },
                    order_delete_params.OrderDeleteParams,
                ),
            ),
            cast_to=OrderDeleteResponse,
        )

    def cancel(
        self,
        order_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Attempts to cancel an existing order.

        Cancelling an order cannot be guaranteed
        as there might be in-flight executions.

        Args:
          account_id: Account ID for the account.

          order_id: Unique order ID assigned by us.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/accounts/{account_id}/orders/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncOrdersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOrdersResourceWithRawResponse:
        return AsyncOrdersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrdersResourceWithStreamingResponse:
        return AsyncOrdersResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: str,
        *,
        order_type: Literal["limit", "market", "stop"],
        quantity: str,
        side: Literal["buy", "sell", "sell-short"],
        symbol: str,
        time_in_force: Literal["day", "ioc", "day-plus", "at-open", "at-close"],
        locate_broker: str | NotGiven = NOT_GIVEN,
        price: str | NotGiven = NOT_GIVEN,
        reference_id: str | NotGiven = NOT_GIVEN,
        stop_price: str | NotGiven = NOT_GIVEN,
        strategy: order_create_params.Strategy | NotGiven = NOT_GIVEN,
        symbol_format: Literal["cms", "osi"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderCreateResponse:
        """Creates a new order and sends to our internal systems for execution.

        Note that a
        successful call to this endpoint does not necessarily mean your order has been
        accepted, e.g. a downstream venue might reject your order. You should therefore
        utilize our WebSocket APIs to listen for changes in order lifecycle events.

        Args:
          account_id: Account ID for the account.

          order_type:
              The type of order, can be one of the following:

              - `limit`: A limit order will execute at-or-better than the limit price you
                specify
              - `market`: An order that will execute at the prevailing market prices
              - `stop`: A stop order will result in a market order when the market price
                reaches the specified stop price

          quantity: The maximum quantity to be executed.

          side: Buy, sell, sell-short indicator.

          symbol: The symbol this order is for. See `symbol_format` for supported symbol formats.

          time_in_force: The lifecycle enforcement of this order.

              - `day`: The order will exist for the duration of the current trading session
              - `ioc`: The order will immediately be executed or cancelled
              - `day-plus`: The order will exist only for the duration the current trading
                session plus extended hours, if applicable
              - `at-open`: The order will exist only for the opening auction of the next
                session
              - `at-close`: The order will exist only for the closing auction of the current
                session

          locate_broker: If you're short-selling and using an away broker for a locate, provide the
              broker name here.

          price: The price to execute at-or-better for limit orders.

          reference_id: An ID that you provide.

          stop_price: The price at which stop orders become marketable.

          strategy: The execution strategy to use for this order. If not provided, our smart
              order-router will handle execution for your order.

          symbol_format: Denotes the format of the provided `symbol` field.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/orders",
            body=await async_maybe_transform(
                {
                    "order_type": order_type,
                    "quantity": quantity,
                    "side": side,
                    "symbol": symbol,
                    "time_in_force": time_in_force,
                    "locate_broker": locate_broker,
                    "price": price,
                    "reference_id": reference_id,
                    "stop_price": stop_price,
                    "strategy": strategy,
                    "symbol_format": symbol_format,
                },
                order_create_params.OrderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderCreateResponse,
        )

    async def retrieve(
        self,
        order_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderRetrieveResponse:
        """
        Get an order that was previously created.

        Args:
          account_id: Account ID for the account.

          order_id: Unique order ID assigned by us.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        return await self._get(
            f"/accounts/{account_id}/orders/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrderRetrieveResponse,
        )

    async def list(
        self,
        account_id: str,
        *,
        from_: int | NotGiven = NOT_GIVEN,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        to: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderListResponse:
        """
        List orders for a given account for the current trading day, filtered on the
        given query parameters.

        Args:
          account_id: Account ID for the account.

          from_: Milliseconds since epoch timestamp. This will constrain the search for orders
              created after this timestamp, inclusively. Timestamps for orders prior the
              current trading day will be ignored.

          page_size: Number of orders to return per page.

          page_token: Cursor for the page to return.

          to: Milliseconds since epoch timestamp. This will constrain the search for orders
              created before this timestamp, inclusively. Timestamps for orders beyond the
              current trading day will be ignored.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/orders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "page_size": page_size,
                        "page_token": page_token,
                        "to": to,
                    },
                    order_list_params.OrderListParams,
                ),
            ),
            cast_to=OrderListResponse,
        )

    async def delete(
        self,
        account_id: str,
        *,
        symbol: str | NotGiven = NOT_GIVEN,
        symbol_format: Literal["cms", "osi"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrderDeleteResponse:
        """Attempts to cancel all open orders for a given account.

        Cancelling an order
        cannot be guaranteed as there might be in-flight executions.

        Args:
          account_id: Account ID for the account.

          symbol: Cancel orders only for this specific symbol. If this is omitted, all open orders
              will be cancelled.

          symbol_format: Format of the provided symbol.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/orders",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbol": symbol,
                        "symbol_format": symbol_format,
                    },
                    order_delete_params.OrderDeleteParams,
                ),
            ),
            cast_to=OrderDeleteResponse,
        )

    async def cancel(
        self,
        order_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Attempts to cancel an existing order.

        Cancelling an order cannot be guaranteed
        as there might be in-flight executions.

        Args:
          account_id: Account ID for the account.

          order_id: Unique order ID assigned by us.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not order_id:
            raise ValueError(f"Expected a non-empty value for `order_id` but received {order_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/accounts/{account_id}/orders/{order_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class OrdersResourceWithRawResponse:
    def __init__(self, orders: OrdersResource) -> None:
        self._orders = orders

        self.create = to_raw_response_wrapper(
            orders.create,
        )
        self.retrieve = to_raw_response_wrapper(
            orders.retrieve,
        )
        self.list = to_raw_response_wrapper(
            orders.list,
        )
        self.delete = to_raw_response_wrapper(
            orders.delete,
        )
        self.cancel = to_raw_response_wrapper(
            orders.cancel,
        )


class AsyncOrdersResourceWithRawResponse:
    def __init__(self, orders: AsyncOrdersResource) -> None:
        self._orders = orders

        self.create = async_to_raw_response_wrapper(
            orders.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            orders.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            orders.list,
        )
        self.delete = async_to_raw_response_wrapper(
            orders.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            orders.cancel,
        )


class OrdersResourceWithStreamingResponse:
    def __init__(self, orders: OrdersResource) -> None:
        self._orders = orders

        self.create = to_streamed_response_wrapper(
            orders.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            orders.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            orders.list,
        )
        self.delete = to_streamed_response_wrapper(
            orders.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            orders.cancel,
        )


class AsyncOrdersResourceWithStreamingResponse:
    def __init__(self, orders: AsyncOrdersResource) -> None:
        self._orders = orders

        self.create = async_to_streamed_response_wrapper(
            orders.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            orders.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            orders.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            orders.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            orders.cancel,
        )
