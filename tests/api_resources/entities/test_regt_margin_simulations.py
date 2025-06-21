# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from studio_sdk import StudioSDK, AsyncStudioSDK
from tests.utils import assert_matches_type
from studio_sdk.types.shared import RegtMarginSimulation
from studio_sdk.types.entities import (
    RegtMarginSimulationCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRegtMarginSimulations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: StudioSDK) -> None:
        regt_margin_simulation = client.entities.regt_margin_simulations.create(
            entity_id="100000",
            name="name",
        )
        assert_matches_type(RegtMarginSimulationCreateResponse, regt_margin_simulation, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: StudioSDK) -> None:
        regt_margin_simulation = client.entities.regt_margin_simulations.create(
            entity_id="100000",
            name="name",
            ignore_existing=True,
            prices=[
                {
                    "price": "123.99",
                    "symbol": "AAPL",
                    "symbol_format": "cms",
                }
            ],
            trades=[
                {
                    "price": "123.99",
                    "quantity": "100",
                    "side": "buy",
                    "symbol": "AAPL",
                    "symbol_format": "cms",
                }
            ],
        )
        assert_matches_type(RegtMarginSimulationCreateResponse, regt_margin_simulation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: StudioSDK) -> None:
        response = client.entities.regt_margin_simulations.with_raw_response.create(
            entity_id="100000",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regt_margin_simulation = response.parse()
        assert_matches_type(RegtMarginSimulationCreateResponse, regt_margin_simulation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: StudioSDK) -> None:
        with client.entities.regt_margin_simulations.with_streaming_response.create(
            entity_id="100000",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regt_margin_simulation = response.parse()
            assert_matches_type(RegtMarginSimulationCreateResponse, regt_margin_simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.regt_margin_simulations.with_raw_response.create(
                entity_id="",
                name="name",
            )

    @parametrize
    def test_method_retrieve(self, client: StudioSDK) -> None:
        regt_margin_simulation = client.entities.regt_margin_simulations.retrieve(
            simulation_id="6460030d-8ed4-19d3-818e-e87b36e90005",
            entity_id="100000",
        )
        assert_matches_type(RegtMarginSimulation, regt_margin_simulation, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: StudioSDK) -> None:
        response = client.entities.regt_margin_simulations.with_raw_response.retrieve(
            simulation_id="6460030d-8ed4-19d3-818e-e87b36e90005",
            entity_id="100000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regt_margin_simulation = response.parse()
        assert_matches_type(RegtMarginSimulation, regt_margin_simulation, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: StudioSDK) -> None:
        with client.entities.regt_margin_simulations.with_streaming_response.retrieve(
            simulation_id="6460030d-8ed4-19d3-818e-e87b36e90005",
            entity_id="100000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regt_margin_simulation = response.parse()
            assert_matches_type(RegtMarginSimulation, regt_margin_simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.regt_margin_simulations.with_raw_response.retrieve(
                simulation_id="6460030d-8ed4-19d3-818e-e87b36e90005",
                entity_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `simulation_id` but received ''"):
            client.entities.regt_margin_simulations.with_raw_response.retrieve(
                simulation_id="",
                entity_id="100000",
            )


class TestAsyncRegtMarginSimulations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncStudioSDK) -> None:
        regt_margin_simulation = await async_client.entities.regt_margin_simulations.create(
            entity_id="100000",
            name="name",
        )
        assert_matches_type(RegtMarginSimulationCreateResponse, regt_margin_simulation, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStudioSDK) -> None:
        regt_margin_simulation = await async_client.entities.regt_margin_simulations.create(
            entity_id="100000",
            name="name",
            ignore_existing=True,
            prices=[
                {
                    "price": "123.99",
                    "symbol": "AAPL",
                    "symbol_format": "cms",
                }
            ],
            trades=[
                {
                    "price": "123.99",
                    "quantity": "100",
                    "side": "buy",
                    "symbol": "AAPL",
                    "symbol_format": "cms",
                }
            ],
        )
        assert_matches_type(RegtMarginSimulationCreateResponse, regt_margin_simulation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.entities.regt_margin_simulations.with_raw_response.create(
            entity_id="100000",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regt_margin_simulation = await response.parse()
        assert_matches_type(RegtMarginSimulationCreateResponse, regt_margin_simulation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.entities.regt_margin_simulations.with_streaming_response.create(
            entity_id="100000",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regt_margin_simulation = await response.parse()
            assert_matches_type(RegtMarginSimulationCreateResponse, regt_margin_simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.regt_margin_simulations.with_raw_response.create(
                entity_id="",
                name="name",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStudioSDK) -> None:
        regt_margin_simulation = await async_client.entities.regt_margin_simulations.retrieve(
            simulation_id="6460030d-8ed4-19d3-818e-e87b36e90005",
            entity_id="100000",
        )
        assert_matches_type(RegtMarginSimulation, regt_margin_simulation, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.entities.regt_margin_simulations.with_raw_response.retrieve(
            simulation_id="6460030d-8ed4-19d3-818e-e87b36e90005",
            entity_id="100000",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        regt_margin_simulation = await response.parse()
        assert_matches_type(RegtMarginSimulation, regt_margin_simulation, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.entities.regt_margin_simulations.with_streaming_response.retrieve(
            simulation_id="6460030d-8ed4-19d3-818e-e87b36e90005",
            entity_id="100000",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            regt_margin_simulation = await response.parse()
            assert_matches_type(RegtMarginSimulation, regt_margin_simulation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.regt_margin_simulations.with_raw_response.retrieve(
                simulation_id="6460030d-8ed4-19d3-818e-e87b36e90005",
                entity_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `simulation_id` but received ''"):
            await async_client.entities.regt_margin_simulations.with_raw_response.retrieve(
                simulation_id="",
                entity_id="100000",
            )
