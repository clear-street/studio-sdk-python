# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from studio_sdk import StudioSDK, AsyncStudioSDK
from tests.utils import assert_matches_type
from studio_sdk.types.accounts import PnlSumListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPnlSums:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: StudioSDK) -> None:
        pnl_sum = client.accounts.pnl_sums.list(
            account_id="x",
            ending_date=20240101,
            starting_date=20240101,
        )
        assert_matches_type(PnlSumListResponse, pnl_sum, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: StudioSDK) -> None:
        pnl_sum = client.accounts.pnl_sums.list(
            account_id="x",
            ending_date=20240101,
            starting_date=20240101,
            symbol="AAPL",
            underlying_symbol="AAPL",
        )
        assert_matches_type(PnlSumListResponse, pnl_sum, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: StudioSDK) -> None:
        response = client.accounts.pnl_sums.with_raw_response.list(
            account_id="x",
            ending_date=20240101,
            starting_date=20240101,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pnl_sum = response.parse()
        assert_matches_type(PnlSumListResponse, pnl_sum, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: StudioSDK) -> None:
        with client.accounts.pnl_sums.with_streaming_response.list(
            account_id="x",
            ending_date=20240101,
            starting_date=20240101,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pnl_sum = response.parse()
            assert_matches_type(PnlSumListResponse, pnl_sum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.pnl_sums.with_raw_response.list(
                account_id="",
                ending_date=20240101,
                starting_date=20240101,
            )


class TestAsyncPnlSums:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncStudioSDK) -> None:
        pnl_sum = await async_client.accounts.pnl_sums.list(
            account_id="x",
            ending_date=20240101,
            starting_date=20240101,
        )
        assert_matches_type(PnlSumListResponse, pnl_sum, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStudioSDK) -> None:
        pnl_sum = await async_client.accounts.pnl_sums.list(
            account_id="x",
            ending_date=20240101,
            starting_date=20240101,
            symbol="AAPL",
            underlying_symbol="AAPL",
        )
        assert_matches_type(PnlSumListResponse, pnl_sum, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.pnl_sums.with_raw_response.list(
            account_id="x",
            ending_date=20240101,
            starting_date=20240101,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pnl_sum = await response.parse()
        assert_matches_type(PnlSumListResponse, pnl_sum, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.pnl_sums.with_streaming_response.list(
            account_id="x",
            ending_date=20240101,
            starting_date=20240101,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pnl_sum = await response.parse()
            assert_matches_type(PnlSumListResponse, pnl_sum, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.pnl_sums.with_raw_response.list(
                account_id="",
                ending_date=20240101,
                starting_date=20240101,
            )
