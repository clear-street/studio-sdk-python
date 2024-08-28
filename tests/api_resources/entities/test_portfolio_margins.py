# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from studio_sdk import StudioSDK, AsyncStudioSDK
from tests.utils import assert_matches_type
from studio_sdk.types import PortfolioMargin

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPortfolioMargins:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: StudioSDK) -> None:
        portfolio_margin = client.entities.portfolio_margins.retrieve(
            "x",
        )
        assert_matches_type(PortfolioMargin, portfolio_margin, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: StudioSDK) -> None:
        response = client.entities.portfolio_margins.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio_margin = response.parse()
        assert_matches_type(PortfolioMargin, portfolio_margin, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: StudioSDK) -> None:
        with client.entities.portfolio_margins.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio_margin = response.parse()
            assert_matches_type(PortfolioMargin, portfolio_margin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            client.entities.portfolio_margins.with_raw_response.retrieve(
                "",
            )


class TestAsyncPortfolioMargins:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStudioSDK) -> None:
        portfolio_margin = await async_client.entities.portfolio_margins.retrieve(
            "x",
        )
        assert_matches_type(PortfolioMargin, portfolio_margin, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.entities.portfolio_margins.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio_margin = await response.parse()
        assert_matches_type(PortfolioMargin, portfolio_margin, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.entities.portfolio_margins.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio_margin = await response.parse()
            assert_matches_type(PortfolioMargin, portfolio_margin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `entity_id` but received ''"):
            await async_client.entities.portfolio_margins.with_raw_response.retrieve(
                "",
            )
