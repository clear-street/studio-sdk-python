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
from ...types.portfolio_margin import PortfolioMargin

__all__ = ["PortfolioMarginsResource", "AsyncPortfolioMarginsResource"]


class PortfolioMarginsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PortfolioMarginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PortfolioMarginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortfolioMarginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return PortfolioMarginsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortfolioMargin:
        """
        Get latest portfolio margin calculation for the given entity

        Args:
          entity_id: Entity ID for the legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._get(
            f"/entities/{entity_id}/portfolio-margin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortfolioMargin,
        )


class AsyncPortfolioMarginsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPortfolioMarginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortfolioMarginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortfolioMarginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return AsyncPortfolioMarginsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        entity_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PortfolioMargin:
        """
        Get latest portfolio margin calculation for the given entity

        Args:
          entity_id: Entity ID for the legal entity.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._get(
            f"/entities/{entity_id}/portfolio-margin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortfolioMargin,
        )


class PortfolioMarginsResourceWithRawResponse:
    def __init__(self, portfolio_margins: PortfolioMarginsResource) -> None:
        self._portfolio_margins = portfolio_margins

        self.retrieve = to_raw_response_wrapper(
            portfolio_margins.retrieve,
        )


class AsyncPortfolioMarginsResourceWithRawResponse:
    def __init__(self, portfolio_margins: AsyncPortfolioMarginsResource) -> None:
        self._portfolio_margins = portfolio_margins

        self.retrieve = async_to_raw_response_wrapper(
            portfolio_margins.retrieve,
        )


class PortfolioMarginsResourceWithStreamingResponse:
    def __init__(self, portfolio_margins: PortfolioMarginsResource) -> None:
        self._portfolio_margins = portfolio_margins

        self.retrieve = to_streamed_response_wrapper(
            portfolio_margins.retrieve,
        )


class AsyncPortfolioMarginsResourceWithStreamingResponse:
    def __init__(self, portfolio_margins: AsyncPortfolioMarginsResource) -> None:
        self._portfolio_margins = portfolio_margins

        self.retrieve = async_to_streamed_response_wrapper(
            portfolio_margins.retrieve,
        )
