# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from studio_sdk import StudioSDK, AsyncStudioSDK
from tests.utils import assert_matches_type
from studio_sdk.types.accounts import HoldingListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHoldings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: StudioSDK) -> None:
        holding = client.accounts.holdings.list(
            account_id="x",
        )
        assert_matches_type(HoldingListResponse, holding, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: StudioSDK) -> None:
        holding = client.accounts.holdings.list(
            account_id="x",
            date=20240101,
        )
        assert_matches_type(HoldingListResponse, holding, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: StudioSDK) -> None:
        response = client.accounts.holdings.with_raw_response.list(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        holding = response.parse()
        assert_matches_type(HoldingListResponse, holding, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: StudioSDK) -> None:
        with client.accounts.holdings.with_streaming_response.list(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            holding = response.parse()
            assert_matches_type(HoldingListResponse, holding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.holdings.with_raw_response.list(
                account_id="",
            )


class TestAsyncHoldings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncStudioSDK) -> None:
        holding = await async_client.accounts.holdings.list(
            account_id="x",
        )
        assert_matches_type(HoldingListResponse, holding, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStudioSDK) -> None:
        holding = await async_client.accounts.holdings.list(
            account_id="x",
            date=20240101,
        )
        assert_matches_type(HoldingListResponse, holding, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.holdings.with_raw_response.list(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        holding = await response.parse()
        assert_matches_type(HoldingListResponse, holding, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.holdings.with_streaming_response.list(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            holding = await response.parse()
            assert_matches_type(HoldingListResponse, holding, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.holdings.with_raw_response.list(
                account_id="",
            )
