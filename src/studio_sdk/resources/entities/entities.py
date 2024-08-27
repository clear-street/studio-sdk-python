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
from .regt_margins import (
    RegtMarginsResource,
    AsyncRegtMarginsResource,
    RegtMarginsResourceWithRawResponse,
    AsyncRegtMarginsResourceWithRawResponse,
    RegtMarginsResourceWithStreamingResponse,
    AsyncRegtMarginsResourceWithStreamingResponse,
)
from .pnl_summaries import (
    PnlSummariesResource,
    AsyncPnlSummariesResource,
    PnlSummariesResourceWithRawResponse,
    AsyncPnlSummariesResourceWithRawResponse,
    PnlSummariesResourceWithStreamingResponse,
    AsyncPnlSummariesResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.entity import Entity
from .portfolio_margins import (
    PortfolioMarginsResource,
    AsyncPortfolioMarginsResource,
    PortfolioMarginsResourceWithRawResponse,
    AsyncPortfolioMarginsResourceWithRawResponse,
    PortfolioMarginsResourceWithStreamingResponse,
    AsyncPortfolioMarginsResourceWithStreamingResponse,
)
from .regt_margin_simulations import (
    RegtMarginSimulationsResource,
    AsyncRegtMarginSimulationsResource,
    RegtMarginSimulationsResourceWithRawResponse,
    AsyncRegtMarginSimulationsResourceWithRawResponse,
    RegtMarginSimulationsResourceWithStreamingResponse,
    AsyncRegtMarginSimulationsResourceWithStreamingResponse,
)
from ...types.entity_list_response import EntityListResponse

__all__ = ["EntitiesResource", "AsyncEntitiesResource"]


class EntitiesResource(SyncAPIResource):
    @cached_property
    def pnl_summaries(self) -> PnlSummariesResource:
        return PnlSummariesResource(self._client)

    @cached_property
    def regt_margins(self) -> RegtMarginsResource:
        return RegtMarginsResource(self._client)

    @cached_property
    def portfolio_margins(self) -> PortfolioMarginsResource:
        return PortfolioMarginsResource(self._client)

    @cached_property
    def regt_margin_simulations(self) -> RegtMarginSimulationsResource:
        return RegtMarginSimulationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EntitiesResourceWithRawResponse:
        return EntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EntitiesResourceWithStreamingResponse:
        return EntitiesResourceWithStreamingResponse(self)

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
    ) -> Entity:
        """
        Get an entity by its ID.

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
            f"/entities/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entity,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListResponse:
        """List all available entities."""
        return self._get(
            "/entities",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityListResponse,
        )


class AsyncEntitiesResource(AsyncAPIResource):
    @cached_property
    def pnl_summaries(self) -> AsyncPnlSummariesResource:
        return AsyncPnlSummariesResource(self._client)

    @cached_property
    def regt_margins(self) -> AsyncRegtMarginsResource:
        return AsyncRegtMarginsResource(self._client)

    @cached_property
    def portfolio_margins(self) -> AsyncPortfolioMarginsResource:
        return AsyncPortfolioMarginsResource(self._client)

    @cached_property
    def regt_margin_simulations(self) -> AsyncRegtMarginSimulationsResource:
        return AsyncRegtMarginSimulationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEntitiesResourceWithRawResponse:
        return AsyncEntitiesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEntitiesResourceWithStreamingResponse:
        return AsyncEntitiesResourceWithStreamingResponse(self)

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
    ) -> Entity:
        """
        Get an entity by its ID.

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
            f"/entities/{entity_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Entity,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EntityListResponse:
        """List all available entities."""
        return await self._get(
            "/entities",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EntityListResponse,
        )


class EntitiesResourceWithRawResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.retrieve = to_raw_response_wrapper(
            entities.retrieve,
        )
        self.list = to_raw_response_wrapper(
            entities.list,
        )

    @cached_property
    def pnl_summaries(self) -> PnlSummariesResourceWithRawResponse:
        return PnlSummariesResourceWithRawResponse(self._entities.pnl_summaries)

    @cached_property
    def regt_margins(self) -> RegtMarginsResourceWithRawResponse:
        return RegtMarginsResourceWithRawResponse(self._entities.regt_margins)

    @cached_property
    def portfolio_margins(self) -> PortfolioMarginsResourceWithRawResponse:
        return PortfolioMarginsResourceWithRawResponse(self._entities.portfolio_margins)

    @cached_property
    def regt_margin_simulations(self) -> RegtMarginSimulationsResourceWithRawResponse:
        return RegtMarginSimulationsResourceWithRawResponse(self._entities.regt_margin_simulations)


class AsyncEntitiesResourceWithRawResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.retrieve = async_to_raw_response_wrapper(
            entities.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            entities.list,
        )

    @cached_property
    def pnl_summaries(self) -> AsyncPnlSummariesResourceWithRawResponse:
        return AsyncPnlSummariesResourceWithRawResponse(self._entities.pnl_summaries)

    @cached_property
    def regt_margins(self) -> AsyncRegtMarginsResourceWithRawResponse:
        return AsyncRegtMarginsResourceWithRawResponse(self._entities.regt_margins)

    @cached_property
    def portfolio_margins(self) -> AsyncPortfolioMarginsResourceWithRawResponse:
        return AsyncPortfolioMarginsResourceWithRawResponse(self._entities.portfolio_margins)

    @cached_property
    def regt_margin_simulations(self) -> AsyncRegtMarginSimulationsResourceWithRawResponse:
        return AsyncRegtMarginSimulationsResourceWithRawResponse(self._entities.regt_margin_simulations)


class EntitiesResourceWithStreamingResponse:
    def __init__(self, entities: EntitiesResource) -> None:
        self._entities = entities

        self.retrieve = to_streamed_response_wrapper(
            entities.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            entities.list,
        )

    @cached_property
    def pnl_summaries(self) -> PnlSummariesResourceWithStreamingResponse:
        return PnlSummariesResourceWithStreamingResponse(self._entities.pnl_summaries)

    @cached_property
    def regt_margins(self) -> RegtMarginsResourceWithStreamingResponse:
        return RegtMarginsResourceWithStreamingResponse(self._entities.regt_margins)

    @cached_property
    def portfolio_margins(self) -> PortfolioMarginsResourceWithStreamingResponse:
        return PortfolioMarginsResourceWithStreamingResponse(self._entities.portfolio_margins)

    @cached_property
    def regt_margin_simulations(self) -> RegtMarginSimulationsResourceWithStreamingResponse:
        return RegtMarginSimulationsResourceWithStreamingResponse(self._entities.regt_margin_simulations)


class AsyncEntitiesResourceWithStreamingResponse:
    def __init__(self, entities: AsyncEntitiesResource) -> None:
        self._entities = entities

        self.retrieve = async_to_streamed_response_wrapper(
            entities.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            entities.list,
        )

    @cached_property
    def pnl_summaries(self) -> AsyncPnlSummariesResourceWithStreamingResponse:
        return AsyncPnlSummariesResourceWithStreamingResponse(self._entities.pnl_summaries)

    @cached_property
    def regt_margins(self) -> AsyncRegtMarginsResourceWithStreamingResponse:
        return AsyncRegtMarginsResourceWithStreamingResponse(self._entities.regt_margins)

    @cached_property
    def portfolio_margins(self) -> AsyncPortfolioMarginsResourceWithStreamingResponse:
        return AsyncPortfolioMarginsResourceWithStreamingResponse(self._entities.portfolio_margins)

    @cached_property
    def regt_margin_simulations(self) -> AsyncRegtMarginSimulationsResourceWithStreamingResponse:
        return AsyncRegtMarginSimulationsResourceWithStreamingResponse(self._entities.regt_margin_simulations)
