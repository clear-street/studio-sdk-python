# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from studio_sdk import StudioSDK, AsyncStudioSDK
from tests.utils import assert_matches_type
from studio_sdk.types.accounts import BulkOrderCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulkOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: StudioSDK) -> None:
        bulk_order = client.accounts.bulk_orders.create(
            account_id="x",
            orders=[
                {
                    "order_type": "limit",
                    "quantity": "x",
                    "side": "buy",
                    "symbol": "AAPL",
                    "time_in_force": "day",
                }
            ],
        )
        assert_matches_type(BulkOrderCreateResponse, bulk_order, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: StudioSDK) -> None:
        response = client.accounts.bulk_orders.with_raw_response.create(
            account_id="x",
            orders=[
                {
                    "order_type": "limit",
                    "quantity": "x",
                    "side": "buy",
                    "symbol": "AAPL",
                    "time_in_force": "day",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_order = response.parse()
        assert_matches_type(BulkOrderCreateResponse, bulk_order, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: StudioSDK) -> None:
        with client.accounts.bulk_orders.with_streaming_response.create(
            account_id="x",
            orders=[
                {
                    "order_type": "limit",
                    "quantity": "x",
                    "side": "buy",
                    "symbol": "AAPL",
                    "time_in_force": "day",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_order = response.parse()
            assert_matches_type(BulkOrderCreateResponse, bulk_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.bulk_orders.with_raw_response.create(
                account_id="",
                orders=[
                    {
                        "order_type": "limit",
                        "quantity": "x",
                        "side": "buy",
                        "symbol": "AAPL",
                        "time_in_force": "day",
                    }
                ],
            )


class TestAsyncBulkOrders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStudioSDK) -> None:
        bulk_order = await async_client.accounts.bulk_orders.create(
            account_id="x",
            orders=[
                {
                    "order_type": "limit",
                    "quantity": "x",
                    "side": "buy",
                    "symbol": "AAPL",
                    "time_in_force": "day",
                }
            ],
        )
        assert_matches_type(BulkOrderCreateResponse, bulk_order, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.bulk_orders.with_raw_response.create(
            account_id="x",
            orders=[
                {
                    "order_type": "limit",
                    "quantity": "x",
                    "side": "buy",
                    "symbol": "AAPL",
                    "time_in_force": "day",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_order = await response.parse()
        assert_matches_type(BulkOrderCreateResponse, bulk_order, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.bulk_orders.with_streaming_response.create(
            account_id="x",
            orders=[
                {
                    "order_type": "limit",
                    "quantity": "x",
                    "side": "buy",
                    "symbol": "AAPL",
                    "time_in_force": "day",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_order = await response.parse()
            assert_matches_type(BulkOrderCreateResponse, bulk_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.bulk_orders.with_raw_response.create(
                account_id="",
                orders=[
                    {
                        "order_type": "limit",
                        "quantity": "x",
                        "side": "buy",
                        "symbol": "AAPL",
                        "time_in_force": "day",
                    }
                ],
            )
