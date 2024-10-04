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
from ...types.regt_margin import RegtMargin

__all__ = ["RegtMarginsResource", "AsyncRegtMarginsResource"]


class RegtMarginsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegtMarginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return RegtMarginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegtMarginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return RegtMarginsResourceWithStreamingResponse(self)

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
    ) -> RegtMargin:
        """
        Get the latest Reg-T margin calculation for the given entity

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
            f"/entities/{entity_id}/regt-margin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegtMargin,
        )


class AsyncRegtMarginsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegtMarginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegtMarginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegtMarginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return AsyncRegtMarginsResourceWithStreamingResponse(self)

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
    ) -> RegtMargin:
        """
        Get the latest Reg-T margin calculation for the given entity

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
            f"/entities/{entity_id}/regt-margin",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegtMargin,
        )


class RegtMarginsResourceWithRawResponse:
    def __init__(self, regt_margins: RegtMarginsResource) -> None:
        self._regt_margins = regt_margins

        self.retrieve = to_raw_response_wrapper(
            regt_margins.retrieve,
        )


class AsyncRegtMarginsResourceWithRawResponse:
    def __init__(self, regt_margins: AsyncRegtMarginsResource) -> None:
        self._regt_margins = regt_margins

        self.retrieve = async_to_raw_response_wrapper(
            regt_margins.retrieve,
        )


class RegtMarginsResourceWithStreamingResponse:
    def __init__(self, regt_margins: RegtMarginsResource) -> None:
        self._regt_margins = regt_margins

        self.retrieve = to_streamed_response_wrapper(
            regt_margins.retrieve,
        )


class AsyncRegtMarginsResourceWithStreamingResponse:
    def __init__(self, regt_margins: AsyncRegtMarginsResource) -> None:
        self._regt_margins = regt_margins

        self.retrieve = async_to_streamed_response_wrapper(
            regt_margins.retrieve,
        )
