# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from studio_sdk import StudioSDK, AsyncStudioSDK
from tests.utils import assert_matches_type
from studio_sdk.types.shared import Trade
from studio_sdk.types.accounts import TradeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrades:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: StudioSDK) -> None:
        trade = client.accounts.trades.retrieve(
            trade_id="x",
            account_id="x",
        )
        assert_matches_type(Trade, trade, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: StudioSDK) -> None:
        response = client.accounts.trades.with_raw_response.retrieve(
            trade_id="x",
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trade = response.parse()
        assert_matches_type(Trade, trade, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: StudioSDK) -> None:
        with client.accounts.trades.with_streaming_response.retrieve(
            trade_id="x",
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trade = response.parse()
            assert_matches_type(Trade, trade, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.trades.with_raw_response.retrieve(
                trade_id="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trade_id` but received ''"):
            client.accounts.trades.with_raw_response.retrieve(
                trade_id="",
                account_id="x",
            )

    @parametrize
    def test_method_list(self, client: StudioSDK) -> None:
        trade = client.accounts.trades.list(
            account_id="x",
        )
        assert_matches_type(TradeListResponse, trade, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: StudioSDK) -> None:
        trade = client.accounts.trades.list(
            account_id="x",
            page_size=1,
            page_token="page_token",
        )
        assert_matches_type(TradeListResponse, trade, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: StudioSDK) -> None:
        response = client.accounts.trades.with_raw_response.list(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trade = response.parse()
        assert_matches_type(TradeListResponse, trade, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: StudioSDK) -> None:
        with client.accounts.trades.with_streaming_response.list(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trade = response.parse()
            assert_matches_type(TradeListResponse, trade, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.trades.with_raw_response.list(
                account_id="",
            )


class TestAsyncTrades:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStudioSDK) -> None:
        trade = await async_client.accounts.trades.retrieve(
            trade_id="x",
            account_id="x",
        )
        assert_matches_type(Trade, trade, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.trades.with_raw_response.retrieve(
            trade_id="x",
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trade = await response.parse()
        assert_matches_type(Trade, trade, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.trades.with_streaming_response.retrieve(
            trade_id="x",
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trade = await response.parse()
            assert_matches_type(Trade, trade, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.trades.with_raw_response.retrieve(
                trade_id="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trade_id` but received ''"):
            await async_client.accounts.trades.with_raw_response.retrieve(
                trade_id="",
                account_id="x",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStudioSDK) -> None:
        trade = await async_client.accounts.trades.list(
            account_id="x",
        )
        assert_matches_type(TradeListResponse, trade, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStudioSDK) -> None:
        trade = await async_client.accounts.trades.list(
            account_id="x",
            page_size=1,
            page_token="page_token",
        )
        assert_matches_type(TradeListResponse, trade, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.trades.with_raw_response.list(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trade = await response.parse()
        assert_matches_type(TradeListResponse, trade, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.trades.with_streaming_response.list(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trade = await response.parse()
            assert_matches_type(TradeListResponse, trade, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.trades.with_raw_response.list(
                account_id="",
            )
