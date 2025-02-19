# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from studio_sdk import StudioSDK, AsyncStudioSDK
from tests.utils import assert_matches_type
from studio_sdk.types.accounts import InventoryRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInventories:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: StudioSDK) -> None:
        inventory = client.accounts.inventories.retrieve(
            symbol="AAPL",
            account_id="x",
        )
        assert_matches_type(InventoryRetrieveResponse, inventory, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: StudioSDK) -> None:
        response = client.accounts.inventories.with_raw_response.retrieve(
            symbol="AAPL",
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory = response.parse()
        assert_matches_type(InventoryRetrieveResponse, inventory, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: StudioSDK) -> None:
        with client.accounts.inventories.with_streaming_response.retrieve(
            symbol="AAPL",
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory = response.parse()
            assert_matches_type(InventoryRetrieveResponse, inventory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.inventories.with_raw_response.retrieve(
                symbol="AAPL",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            client.accounts.inventories.with_raw_response.retrieve(
                symbol="",
                account_id="x",
            )


class TestAsyncInventories:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStudioSDK) -> None:
        inventory = await async_client.accounts.inventories.retrieve(
            symbol="AAPL",
            account_id="x",
        )
        assert_matches_type(InventoryRetrieveResponse, inventory, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.inventories.with_raw_response.retrieve(
            symbol="AAPL",
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inventory = await response.parse()
        assert_matches_type(InventoryRetrieveResponse, inventory, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.inventories.with_streaming_response.retrieve(
            symbol="AAPL",
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inventory = await response.parse()
            assert_matches_type(InventoryRetrieveResponse, inventory, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.inventories.with_raw_response.retrieve(
                symbol="AAPL",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            await async_client.accounts.inventories.with_raw_response.retrieve(
                symbol="",
                account_id="x",
            )
