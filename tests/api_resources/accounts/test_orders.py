# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from studio_sdk import StudioSDK, AsyncStudioSDK
from tests.utils import assert_matches_type
from studio_sdk.types.accounts import (
    OrderListResponse,
    OrderCreateResponse,
    OrderDeleteResponse,
    OrderRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: StudioSDK) -> None:
        order = client.accounts.orders.create(
            account_id="x",
            order_type="limit",
            quantity="x",
            side="buy",
            symbol="AAPL",
            time_in_force="day",
        )
        assert_matches_type(OrderCreateResponse, order, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: StudioSDK) -> None:
        order = client.accounts.orders.create(
            account_id="x",
            order_type="limit",
            quantity="x",
            side="buy",
            symbol="AAPL",
            time_in_force="day",
            locate_broker="x",
            price="x",
            reference_id="my-order-id-123",
            stop_price="x",
            strategy={
                "type": "sor",
                "end_at": 1710613560668,
                "start_at": 1710613560668,
                "urgency": "super-passive",
            },
            symbol_format="cms",
        )
        assert_matches_type(OrderCreateResponse, order, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: StudioSDK) -> None:
        response = client.accounts.orders.with_raw_response.create(
            account_id="x",
            order_type="limit",
            quantity="x",
            side="buy",
            symbol="AAPL",
            time_in_force="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderCreateResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: StudioSDK) -> None:
        with client.accounts.orders.with_streaming_response.create(
            account_id="x",
            order_type="limit",
            quantity="x",
            side="buy",
            symbol="AAPL",
            time_in_force="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderCreateResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.orders.with_raw_response.create(
                account_id="",
                order_type="limit",
                quantity="x",
                side="buy",
                symbol="AAPL",
                time_in_force="day",
            )

    @parametrize
    def test_method_retrieve(self, client: StudioSDK) -> None:
        order = client.accounts.orders.retrieve(
            order_id="x",
            account_id="x",
        )
        assert_matches_type(OrderRetrieveResponse, order, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: StudioSDK) -> None:
        response = client.accounts.orders.with_raw_response.retrieve(
            order_id="x",
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderRetrieveResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: StudioSDK) -> None:
        with client.accounts.orders.with_streaming_response.retrieve(
            order_id="x",
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderRetrieveResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.orders.with_raw_response.retrieve(
                order_id="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.accounts.orders.with_raw_response.retrieve(
                order_id="",
                account_id="x",
            )

    @parametrize
    def test_method_list(self, client: StudioSDK) -> None:
        order = client.accounts.orders.list(
            account_id="x",
        )
        assert_matches_type(OrderListResponse, order, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: StudioSDK) -> None:
        order = client.accounts.orders.list(
            account_id="x",
            from_=1710613560668,
            page_size=1,
            page_token="page_token",
            to=1710613560668,
        )
        assert_matches_type(OrderListResponse, order, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: StudioSDK) -> None:
        response = client.accounts.orders.with_raw_response.list(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderListResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: StudioSDK) -> None:
        with client.accounts.orders.with_streaming_response.list(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderListResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.orders.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: StudioSDK) -> None:
        order = client.accounts.orders.delete(
            account_id="x",
        )
        assert_matches_type(OrderDeleteResponse, order, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: StudioSDK) -> None:
        order = client.accounts.orders.delete(
            account_id="x",
            symbol="AAPL",
            symbol_format="cms",
        )
        assert_matches_type(OrderDeleteResponse, order, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: StudioSDK) -> None:
        response = client.accounts.orders.with_raw_response.delete(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(OrderDeleteResponse, order, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: StudioSDK) -> None:
        with client.accounts.orders.with_streaming_response.delete(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(OrderDeleteResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.orders.with_raw_response.delete(
                account_id="",
            )

    @parametrize
    def test_method_cancel(self, client: StudioSDK) -> None:
        order = client.accounts.orders.cancel(
            order_id="x",
            account_id="x",
        )
        assert order is None

    @parametrize
    def test_raw_response_cancel(self, client: StudioSDK) -> None:
        response = client.accounts.orders.with_raw_response.cancel(
            order_id="x",
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert order is None

    @parametrize
    def test_streaming_response_cancel(self, client: StudioSDK) -> None:
        with client.accounts.orders.with_streaming_response.cancel(
            order_id="x",
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_cancel(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.orders.with_raw_response.cancel(
                order_id="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            client.accounts.orders.with_raw_response.cancel(
                order_id="",
                account_id="x",
            )


class TestAsyncOrders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStudioSDK) -> None:
        order = await async_client.accounts.orders.create(
            account_id="x",
            order_type="limit",
            quantity="x",
            side="buy",
            symbol="AAPL",
            time_in_force="day",
        )
        assert_matches_type(OrderCreateResponse, order, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStudioSDK) -> None:
        order = await async_client.accounts.orders.create(
            account_id="x",
            order_type="limit",
            quantity="x",
            side="buy",
            symbol="AAPL",
            time_in_force="day",
            locate_broker="x",
            price="x",
            reference_id="my-order-id-123",
            stop_price="x",
            strategy={
                "type": "sor",
                "end_at": 1710613560668,
                "start_at": 1710613560668,
                "urgency": "super-passive",
            },
            symbol_format="cms",
        )
        assert_matches_type(OrderCreateResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.orders.with_raw_response.create(
            account_id="x",
            order_type="limit",
            quantity="x",
            side="buy",
            symbol="AAPL",
            time_in_force="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderCreateResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.orders.with_streaming_response.create(
            account_id="x",
            order_type="limit",
            quantity="x",
            side="buy",
            symbol="AAPL",
            time_in_force="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderCreateResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.orders.with_raw_response.create(
                account_id="",
                order_type="limit",
                quantity="x",
                side="buy",
                symbol="AAPL",
                time_in_force="day",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStudioSDK) -> None:
        order = await async_client.accounts.orders.retrieve(
            order_id="x",
            account_id="x",
        )
        assert_matches_type(OrderRetrieveResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.orders.with_raw_response.retrieve(
            order_id="x",
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderRetrieveResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.orders.with_streaming_response.retrieve(
            order_id="x",
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderRetrieveResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.orders.with_raw_response.retrieve(
                order_id="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.accounts.orders.with_raw_response.retrieve(
                order_id="",
                account_id="x",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStudioSDK) -> None:
        order = await async_client.accounts.orders.list(
            account_id="x",
        )
        assert_matches_type(OrderListResponse, order, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncStudioSDK) -> None:
        order = await async_client.accounts.orders.list(
            account_id="x",
            from_=1710613560668,
            page_size=1,
            page_token="page_token",
            to=1710613560668,
        )
        assert_matches_type(OrderListResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.orders.with_raw_response.list(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderListResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.orders.with_streaming_response.list(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderListResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.orders.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncStudioSDK) -> None:
        order = await async_client.accounts.orders.delete(
            account_id="x",
        )
        assert_matches_type(OrderDeleteResponse, order, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncStudioSDK) -> None:
        order = await async_client.accounts.orders.delete(
            account_id="x",
            symbol="AAPL",
            symbol_format="cms",
        )
        assert_matches_type(OrderDeleteResponse, order, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.orders.with_raw_response.delete(
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(OrderDeleteResponse, order, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.orders.with_streaming_response.delete(
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(OrderDeleteResponse, order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.orders.with_raw_response.delete(
                account_id="",
            )

    @parametrize
    async def test_method_cancel(self, async_client: AsyncStudioSDK) -> None:
        order = await async_client.accounts.orders.cancel(
            order_id="x",
            account_id="x",
        )
        assert order is None

    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.orders.with_raw_response.cancel(
            order_id="x",
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert order is None

    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.orders.with_streaming_response.cancel(
            order_id="x",
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.orders.with_raw_response.cancel(
                order_id="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `order_id` but received ''"):
            await async_client.accounts.orders.with_raw_response.cancel(
                order_id="",
                account_id="x",
            )
