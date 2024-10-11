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
from ...types.accounts import pnl_sum_list_params
from ...types.accounts.pnl_sum_list_response import PnlSumListResponse

__all__ = ["PnlSumsResource", "AsyncPnlSumsResource"]


class PnlSumsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PnlSumsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PnlSumsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PnlSumsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return PnlSumsResourceWithStreamingResponse(self)

    def list(
        self,
        account_id: str,
        *,
        ending_date: int,
        starting_date: int,
        symbol: str | NotGiven = NOT_GIVEN,
        underlying_symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PnlSumListResponse:
        """
        List historical PNL summations for a given account over a given date range,
        filtered on the given query parameters.

        Args:
          account_id: Account ID for the account.

          ending_date: The ending date to accumulate PNL data for, inclusive.

          starting_date: The starting date to accumulate PNL data for.

          symbol: Filters for a specific symbol.

          underlying_symbol: Filters for a specific underlying symbol, e.g. all options for a particular
              underlying.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/pnl-sums",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "ending_date": ending_date,
                        "starting_date": starting_date,
                        "symbol": symbol,
                        "underlying_symbol": underlying_symbol,
                    },
                    pnl_sum_list_params.PnlSumListParams,
                ),
            ),
            cast_to=PnlSumListResponse,
        )


class AsyncPnlSumsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPnlSumsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPnlSumsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPnlSumsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return AsyncPnlSumsResourceWithStreamingResponse(self)

    async def list(
        self,
        account_id: str,
        *,
        ending_date: int,
        starting_date: int,
        symbol: str | NotGiven = NOT_GIVEN,
        underlying_symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PnlSumListResponse:
        """
        List historical PNL summations for a given account over a given date range,
        filtered on the given query parameters.

        Args:
          account_id: Account ID for the account.

          ending_date: The ending date to accumulate PNL data for, inclusive.

          starting_date: The starting date to accumulate PNL data for.

          symbol: Filters for a specific symbol.

          underlying_symbol: Filters for a specific underlying symbol, e.g. all options for a particular
              underlying.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/pnl-sums",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "ending_date": ending_date,
                        "starting_date": starting_date,
                        "symbol": symbol,
                        "underlying_symbol": underlying_symbol,
                    },
                    pnl_sum_list_params.PnlSumListParams,
                ),
            ),
            cast_to=PnlSumListResponse,
        )


class PnlSumsResourceWithRawResponse:
    def __init__(self, pnl_sums: PnlSumsResource) -> None:
        self._pnl_sums = pnl_sums

        self.list = to_raw_response_wrapper(
            pnl_sums.list,
        )


class AsyncPnlSumsResourceWithRawResponse:
    def __init__(self, pnl_sums: AsyncPnlSumsResource) -> None:
        self._pnl_sums = pnl_sums

        self.list = async_to_raw_response_wrapper(
            pnl_sums.list,
        )


class PnlSumsResourceWithStreamingResponse:
    def __init__(self, pnl_sums: PnlSumsResource) -> None:
        self._pnl_sums = pnl_sums

        self.list = to_streamed_response_wrapper(
            pnl_sums.list,
        )


class AsyncPnlSumsResourceWithStreamingResponse:
    def __init__(self, pnl_sums: AsyncPnlSumsResource) -> None:
        self._pnl_sums = pnl_sums

        self.list = async_to_streamed_response_wrapper(
            pnl_sums.list,
        )
