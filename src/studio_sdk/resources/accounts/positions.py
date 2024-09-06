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
from ...types.accounts import position_list_params
from ...types.shared.position import Position
from ...types.accounts.position_list_response import PositionListResponse

__all__ = ["PositionsResource", "AsyncPositionsResource"]


class PositionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PositionsResourceWithRawResponse:
        return PositionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PositionsResourceWithStreamingResponse:
        return PositionsResourceWithStreamingResponse(self)

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
    ) -> Position:
        """
        Get current positions for a given account for a given symbol.

        Args:
          account_id: Account ID for the account.

          symbol: Symbol to get position for.

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
            f"/accounts/{account_id}/positions/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Position,
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
    ) -> PositionListResponse:
        """
        List current positions for a given account.

        Args:
          account_id: Account ID for the account.

          page_size: Number of positions to return per page.

          page_token: Cursor for the page to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/positions",
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
                    position_list_params.PositionListParams,
                ),
            ),
            cast_to=PositionListResponse,
        )


class AsyncPositionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPositionsResourceWithRawResponse:
        return AsyncPositionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPositionsResourceWithStreamingResponse:
        return AsyncPositionsResourceWithStreamingResponse(self)

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
    ) -> Position:
        """
        Get current positions for a given account for a given symbol.

        Args:
          account_id: Account ID for the account.

          symbol: Symbol to get position for.

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
            f"/accounts/{account_id}/positions/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Position,
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
    ) -> PositionListResponse:
        """
        List current positions for a given account.

        Args:
          account_id: Account ID for the account.

          page_size: Number of positions to return per page.

          page_token: Cursor for the page to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/positions",
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
                    position_list_params.PositionListParams,
                ),
            ),
            cast_to=PositionListResponse,
        )


class PositionsResourceWithRawResponse:
    def __init__(self, positions: PositionsResource) -> None:
        self._positions = positions

        self.retrieve = to_raw_response_wrapper(
            positions.retrieve,
        )
        self.list = to_raw_response_wrapper(
            positions.list,
        )


class AsyncPositionsResourceWithRawResponse:
    def __init__(self, positions: AsyncPositionsResource) -> None:
        self._positions = positions

        self.retrieve = async_to_raw_response_wrapper(
            positions.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            positions.list,
        )


class PositionsResourceWithStreamingResponse:
    def __init__(self, positions: PositionsResource) -> None:
        self._positions = positions

        self.retrieve = to_streamed_response_wrapper(
            positions.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            positions.list,
        )


class AsyncPositionsResourceWithStreamingResponse:
    def __init__(self, positions: AsyncPositionsResource) -> None:
        self._positions = positions

        self.retrieve = async_to_streamed_response_wrapper(
            positions.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            positions.list,
        )
