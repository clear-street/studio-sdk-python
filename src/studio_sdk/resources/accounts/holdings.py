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
from ...types.accounts import holding_list_params
from ...types.accounts.holding_list_response import HoldingListResponse

__all__ = ["HoldingsResource", "AsyncHoldingsResource"]


class HoldingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HoldingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return HoldingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HoldingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return HoldingsResourceWithStreamingResponse(self)

    def list(
        self,
        account_id: str,
        *,
        date: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HoldingListResponse:
        """List holdings for a given account, filtered on the given query parameters.

        This
        endpoint will return either historical or real-time holdings directly from our
        custodial systems. Positions returned here are can be different than positions
        returned from the Execution API. While the Execution API returns positions based
        on trading activity within Studio, our custodial system returns all positions
        regardless of where trades occur.

        Args:
          account_id: Account ID for the account.

          date: The historical date to get holdings for. If omitted, current real-time holdings
              will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/holdings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, holding_list_params.HoldingListParams),
            ),
            cast_to=HoldingListResponse,
        )


class AsyncHoldingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHoldingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHoldingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHoldingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return AsyncHoldingsResourceWithStreamingResponse(self)

    async def list(
        self,
        account_id: str,
        *,
        date: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HoldingListResponse:
        """List holdings for a given account, filtered on the given query parameters.

        This
        endpoint will return either historical or real-time holdings directly from our
        custodial systems. Positions returned here are can be different than positions
        returned from the Execution API. While the Execution API returns positions based
        on trading activity within Studio, our custodial system returns all positions
        regardless of where trades occur.

        Args:
          account_id: Account ID for the account.

          date: The historical date to get holdings for. If omitted, current real-time holdings
              will be returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/holdings",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"date": date}, holding_list_params.HoldingListParams),
            ),
            cast_to=HoldingListResponse,
        )


class HoldingsResourceWithRawResponse:
    def __init__(self, holdings: HoldingsResource) -> None:
        self._holdings = holdings

        self.list = to_raw_response_wrapper(
            holdings.list,
        )


class AsyncHoldingsResourceWithRawResponse:
    def __init__(self, holdings: AsyncHoldingsResource) -> None:
        self._holdings = holdings

        self.list = async_to_raw_response_wrapper(
            holdings.list,
        )


class HoldingsResourceWithStreamingResponse:
    def __init__(self, holdings: HoldingsResource) -> None:
        self._holdings = holdings

        self.list = to_streamed_response_wrapper(
            holdings.list,
        )


class AsyncHoldingsResourceWithStreamingResponse:
    def __init__(self, holdings: AsyncHoldingsResource) -> None:
        self._holdings = holdings

        self.list = async_to_streamed_response_wrapper(
            holdings.list,
        )
