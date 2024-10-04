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
from ...types.accounts.pnl_detail_list_response import PnlDetailListResponse

__all__ = ["PnlDetailsResource", "AsyncPnlDetailsResource"]


class PnlDetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PnlDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PnlDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PnlDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return PnlDetailsResourceWithStreamingResponse(self)

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
    ) -> PnlDetailListResponse:
        """
        List PNL details for a given account.

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
            f"/accounts/{account_id}/pnl-details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PnlDetailListResponse,
        )


class AsyncPnlDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPnlDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPnlDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPnlDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return AsyncPnlDetailsResourceWithStreamingResponse(self)

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
    ) -> PnlDetailListResponse:
        """
        List PNL details for a given account.

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
            f"/accounts/{account_id}/pnl-details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PnlDetailListResponse,
        )


class PnlDetailsResourceWithRawResponse:
    def __init__(self, pnl_details: PnlDetailsResource) -> None:
        self._pnl_details = pnl_details

        self.list = to_raw_response_wrapper(
            pnl_details.list,
        )


class AsyncPnlDetailsResourceWithRawResponse:
    def __init__(self, pnl_details: AsyncPnlDetailsResource) -> None:
        self._pnl_details = pnl_details

        self.list = async_to_raw_response_wrapper(
            pnl_details.list,
        )


class PnlDetailsResourceWithStreamingResponse:
    def __init__(self, pnl_details: PnlDetailsResource) -> None:
        self._pnl_details = pnl_details

        self.list = to_streamed_response_wrapper(
            pnl_details.list,
        )


class AsyncPnlDetailsResourceWithStreamingResponse:
    def __init__(self, pnl_details: AsyncPnlDetailsResource) -> None:
        self._pnl_details = pnl_details

        self.list = async_to_streamed_response_wrapper(
            pnl_details.list,
        )
