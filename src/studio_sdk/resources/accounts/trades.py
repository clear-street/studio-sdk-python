# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.accounts import trade_list_params
from ...types.shared.trade import Trade
from ...types.accounts.trade_list_response import TradeListResponse

__all__ = ["TradesResource", "AsyncTradesResource"]


class TradesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return TradesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        trade_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Trade:
        """
        Get trade a trade by its unique trade ID.

        Args:
          account_id: Account ID for the account.

          trade_id: Unique trade ID assigned by us.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not trade_id:
            raise ValueError(f"Expected a non-empty value for `trade_id` but received {trade_id!r}")
        return self._get(
            f"/accounts/{account_id}/trades/{trade_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Trade,
        )

    def list(
        self,
        account_id: str,
        *,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TradeListResponse:
        """
        List trades for a given account for the current trading day.

        Args:
          account_id: Account ID for the account.

          page_size: Number of trades to return per page.

          page_token: Cursor for the page to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/trades",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    trade_list_params.TradeListParams,
                ),
            ),
            cast_to=TradeListResponse,
        )


class AsyncTradesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTradesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTradesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTradesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return AsyncTradesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        trade_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Trade:
        """
        Get trade a trade by its unique trade ID.

        Args:
          account_id: Account ID for the account.

          trade_id: Unique trade ID assigned by us.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not trade_id:
            raise ValueError(f"Expected a non-empty value for `trade_id` but received {trade_id!r}")
        return await self._get(
            f"/accounts/{account_id}/trades/{trade_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Trade,
        )

    async def list(
        self,
        account_id: str,
        *,
        page_size: int | NotGiven = NOT_GIVEN,
        page_token: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TradeListResponse:
        """
        List trades for a given account for the current trading day.

        Args:
          account_id: Account ID for the account.

          page_size: Number of trades to return per page.

          page_token: Cursor for the page to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/trades",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    trade_list_params.TradeListParams,
                ),
            ),
            cast_to=TradeListResponse,
        )


class TradesResourceWithRawResponse:
    def __init__(self, trades: TradesResource) -> None:
        self._trades = trades

        self.retrieve = to_raw_response_wrapper(
            trades.retrieve,
        )
        self.list = to_raw_response_wrapper(
            trades.list,
        )


class AsyncTradesResourceWithRawResponse:
    def __init__(self, trades: AsyncTradesResource) -> None:
        self._trades = trades

        self.retrieve = async_to_raw_response_wrapper(
            trades.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            trades.list,
        )


class TradesResourceWithStreamingResponse:
    def __init__(self, trades: TradesResource) -> None:
        self._trades = trades

        self.retrieve = to_streamed_response_wrapper(
            trades.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            trades.list,
        )


class AsyncTradesResourceWithStreamingResponse:
    def __init__(self, trades: AsyncTradesResource) -> None:
        self._trades = trades

        self.retrieve = async_to_streamed_response_wrapper(
            trades.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            trades.list,
        )
