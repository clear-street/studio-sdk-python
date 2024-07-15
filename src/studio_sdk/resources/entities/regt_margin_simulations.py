# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

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
from ...types.entities import SimulationID, regt_margin_simulation_create_params
from ...types.entities.simulation_id import SimulationID
from ...types.shared.regt_margin_simulation import RegtMarginSimulation
from ...types.entities.regt_margin_simulation_create_response import RegtMarginSimulationCreateResponse

__all__ = ["RegtMarginSimulationsResource", "AsyncRegtMarginSimulationsResource"]


class RegtMarginSimulationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegtMarginSimulationsResourceWithRawResponse:
        return RegtMarginSimulationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegtMarginSimulationsResourceWithStreamingResponse:
        return RegtMarginSimulationsResourceWithStreamingResponse(self)

    def create(
        self,
        entity_id: str,
        *,
        name: str,
        ignore_existing: bool | NotGiven = NOT_GIVEN,
        prices: Iterable[regt_margin_simulation_create_params.Price] | NotGiven = NOT_GIVEN,
        trades: Iterable[regt_margin_simulation_create_params.Trade] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegtMarginSimulationCreateResponse:
        """
        Simulate Reg-T margin calculation for a given hypothetical set of prices and/or
        trades. This is useful for understanding the impact of price fluctuations or
        trades on margin requirements. Once a simulation is created, it remains
        available for 48-hours, after which it will automatically be deleted.

        Simulations created through the API are visible in the Studio UI under the Risk
        & Margin section, after enabling the "Risk Simulations" toggle.

        Args:
          entity_id: Entity ID for the legal entity.

          name: A name for this simulation for reference.

          ignore_existing: If true, the simulation will ignore any existing positions and balances in the
              account. Set to true if you want to simulate from a clean slate, i.e. an empty
              account.

          prices: List of prices to use in the simulation, i.e. fair-market-values you specify for
              each symbol. If this is not provided, current market prices will be used, if
              they are available.

          trades: List of hypothetical trades to include in the simulation, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return self._post(
            f"/entities/{entity_id}/regt-margin-simulations",
            body=maybe_transform(
                {
                    "name": name,
                    "ignore_existing": ignore_existing,
                    "prices": prices,
                    "trades": trades,
                },
                regt_margin_simulation_create_params.RegtMarginSimulationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegtMarginSimulationCreateResponse,
        )

    def retrieve(
        self,
        simulation_id: SimulationID,
        *,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegtMarginSimulation:
        """Get a Reg-T margin simluation that was previously created.

        Note, simulations are
        automatically deleted after 48-hours.

        Args:
          entity_id: Entity ID for the legal entity.

          simulation_id: Unique ID for a simulation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        if not simulation_id:
            raise ValueError(f"Expected a non-empty value for `simulation_id` but received {simulation_id!r}")
        return self._get(
            f"/entities/{entity_id}/regt-margin-simulations/{simulation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegtMarginSimulation,
        )


class AsyncRegtMarginSimulationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegtMarginSimulationsResourceWithRawResponse:
        return AsyncRegtMarginSimulationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegtMarginSimulationsResourceWithStreamingResponse:
        return AsyncRegtMarginSimulationsResourceWithStreamingResponse(self)

    async def create(
        self,
        entity_id: str,
        *,
        name: str,
        ignore_existing: bool | NotGiven = NOT_GIVEN,
        prices: Iterable[regt_margin_simulation_create_params.Price] | NotGiven = NOT_GIVEN,
        trades: Iterable[regt_margin_simulation_create_params.Trade] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegtMarginSimulationCreateResponse:
        """
        Simulate Reg-T margin calculation for a given hypothetical set of prices and/or
        trades. This is useful for understanding the impact of price fluctuations or
        trades on margin requirements. Once a simulation is created, it remains
        available for 48-hours, after which it will automatically be deleted.

        Simulations created through the API are visible in the Studio UI under the Risk
        & Margin section, after enabling the "Risk Simulations" toggle.

        Args:
          entity_id: Entity ID for the legal entity.

          name: A name for this simulation for reference.

          ignore_existing: If true, the simulation will ignore any existing positions and balances in the
              account. Set to true if you want to simulate from a clean slate, i.e. an empty
              account.

          prices: List of prices to use in the simulation, i.e. fair-market-values you specify for
              each symbol. If this is not provided, current market prices will be used, if
              they are available.

          trades: List of hypothetical trades to include in the simulation, if any.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        return await self._post(
            f"/entities/{entity_id}/regt-margin-simulations",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "ignore_existing": ignore_existing,
                    "prices": prices,
                    "trades": trades,
                },
                regt_margin_simulation_create_params.RegtMarginSimulationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegtMarginSimulationCreateResponse,
        )

    async def retrieve(
        self,
        simulation_id: SimulationID,
        *,
        entity_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegtMarginSimulation:
        """Get a Reg-T margin simluation that was previously created.

        Note, simulations are
        automatically deleted after 48-hours.

        Args:
          entity_id: Entity ID for the legal entity.

          simulation_id: Unique ID for a simulation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not entity_id:
            raise ValueError(f"Expected a non-empty value for `entity_id` but received {entity_id!r}")
        if not simulation_id:
            raise ValueError(f"Expected a non-empty value for `simulation_id` but received {simulation_id!r}")
        return await self._get(
            f"/entities/{entity_id}/regt-margin-simulations/{simulation_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RegtMarginSimulation,
        )


class RegtMarginSimulationsResourceWithRawResponse:
    def __init__(self, regt_margin_simulations: RegtMarginSimulationsResource) -> None:
        self._regt_margin_simulations = regt_margin_simulations

        self.create = to_raw_response_wrapper(
            regt_margin_simulations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            regt_margin_simulations.retrieve,
        )


class AsyncRegtMarginSimulationsResourceWithRawResponse:
    def __init__(self, regt_margin_simulations: AsyncRegtMarginSimulationsResource) -> None:
        self._regt_margin_simulations = regt_margin_simulations

        self.create = async_to_raw_response_wrapper(
            regt_margin_simulations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            regt_margin_simulations.retrieve,
        )


class RegtMarginSimulationsResourceWithStreamingResponse:
    def __init__(self, regt_margin_simulations: RegtMarginSimulationsResource) -> None:
        self._regt_margin_simulations = regt_margin_simulations

        self.create = to_streamed_response_wrapper(
            regt_margin_simulations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            regt_margin_simulations.retrieve,
        )


class AsyncRegtMarginSimulationsResourceWithStreamingResponse:
    def __init__(self, regt_margin_simulations: AsyncRegtMarginSimulationsResource) -> None:
        self._regt_margin_simulations = regt_margin_simulations

        self.create = async_to_streamed_response_wrapper(
            regt_margin_simulations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            regt_margin_simulations.retrieve,
        )
