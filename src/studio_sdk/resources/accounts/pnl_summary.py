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
from ...types.accounts.pnl_summary_retrieve_response import PnlSummaryRetrieveResponse

__all__ = ["PnlSummaryResource", "AsyncPnlSummaryResource"]


class PnlSummaryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PnlSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PnlSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PnlSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return PnlSummaryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PnlSummaryRetrieveResponse:
        """
        Get PNL summary for a given account.

        Args:
          account_id: The account ID or account number to get a PNL summary for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/pnl-summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PnlSummaryRetrieveResponse,
        )


class AsyncPnlSummaryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPnlSummaryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPnlSummaryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPnlSummaryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return AsyncPnlSummaryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PnlSummaryRetrieveResponse:
        """
        Get PNL summary for a given account.

        Args:
          account_id: The account ID or account number to get a PNL summary for.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/pnl-summary",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PnlSummaryRetrieveResponse,
        )


class PnlSummaryResourceWithRawResponse:
    def __init__(self, pnl_summary: PnlSummaryResource) -> None:
        self._pnl_summary = pnl_summary

        self.retrieve = to_raw_response_wrapper(
            pnl_summary.retrieve,
        )


class AsyncPnlSummaryResourceWithRawResponse:
    def __init__(self, pnl_summary: AsyncPnlSummaryResource) -> None:
        self._pnl_summary = pnl_summary

        self.retrieve = async_to_raw_response_wrapper(
            pnl_summary.retrieve,
        )


class PnlSummaryResourceWithStreamingResponse:
    def __init__(self, pnl_summary: PnlSummaryResource) -> None:
        self._pnl_summary = pnl_summary

        self.retrieve = to_streamed_response_wrapper(
            pnl_summary.retrieve,
        )


class AsyncPnlSummaryResourceWithStreamingResponse:
    def __init__(self, pnl_summary: AsyncPnlSummaryResource) -> None:
        self._pnl_summary = pnl_summary

        self.retrieve = async_to_streamed_response_wrapper(
            pnl_summary.retrieve,
        )
