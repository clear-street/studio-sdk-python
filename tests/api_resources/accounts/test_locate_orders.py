# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from studio_sdk import StudioSDK, AsyncStudioSDK
from tests.utils import assert_matches_type
from studio_sdk.types.shared import LocateOrder
from studio_sdk.types.accounts import LocateOrderListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLocateOrders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: StudioSDK) -> None:
        locate_order = client.accounts.locate_orders.create(
            account_id="x",
            mpid="x",
            quantity="x",
            reference_id="my-order-id-123",
            symbol="AAPL",
        )
        assert_matches_type(LocateOrder, locate_order, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: StudioSDK) -> None:
        locate_order = client.accounts.locate_orders.create(
            account_id="x",
            mpid="x",
            quantity="x",
            reference_id="my-order-id-123",
            symbol="AAPL",
            comments="comments",
        )
        assert_matches_type(LocateOrder, locate_order, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: StudioSDK) -> None:
        response = client.accounts.locate_orders.with_raw_response.create(
            account_id="x",
            mpid="x",
            quantity="x",
            reference_id="my-order-id-123",
            symbol="AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate_order = response.parse()
        assert_matches_type(LocateOrder, locate_order, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: StudioSDK) -> None:
        with client.accounts.locate_orders.with_streaming_response.create(
            account_id="x",
            mpid="x",
            quantity="x",
            reference_id="my-order-id-123",
            symbol="AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate_order = response.parse()
            assert_matches_type(LocateOrder, locate_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.locate_orders.with_raw_response.create(
                account_id="",
                mpid="x",
                quantity="x",
                reference_id="my-order-id-123",
                symbol="AAPL",
            )

    @parametrize
    def test_method_retrieve(self, client: StudioSDK) -> None:
        locate_order = client.accounts.locate_orders.retrieve(
            locate_order_id="x",
            account_id="x",
        )
        assert_matches_type(LocateOrder, locate_order, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: StudioSDK) -> None:
        response = client.accounts.locate_orders.with_raw_response.retrieve(
            locate_order_id="x",
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate_order = response.parse()
        assert_matches_type(LocateOrder, locate_order, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: StudioSDK) -> None:
        with client.accounts.locate_orders.with_streaming_response.retrieve(
            locate_order_id="x",
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate_order = response.parse()
            assert_matches_type(LocateOrder, locate_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.locate_orders.with_raw_response.retrieve(
                locate_order_id="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locate_order_id` but received ''"):
            client.accounts.locate_orders.with_raw_response.retrieve(
                locate_order_id="",
                account_id="x",
            )

    @parametrize
    def test_method_update(self, client: StudioSDK) -> None:
        locate_order = client.accounts.locate_orders.update(
            locate_order_id="x",
            account_id="x",
            accept=True,
        )
        assert locate_order is None

    @parametrize
    def test_raw_response_update(self, client: StudioSDK) -> None:
        response = client.accounts.locate_orders.with_raw_response.update(
            locate_order_id="x",
            account_id="x",
            accept=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate_order = response.parse()
        assert locate_order is None

    @parametrize
    def test_streaming_response_update(self, client: StudioSDK) -> None:
        with client.accounts.locate_orders.with_streaming_response.update(
            locate_order_id="x",
            account_id="x",
            accept=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate_order = response.parse()
            assert locate_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.locate_orders.with_raw_response.update(
                locate_order_id="x",
                account_id="",
                accept=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locate_order_id` but received ''"):
            client.accounts.locate_orders.with_raw_response.update(
                locate_order_id="",
                account_id="x",
                accept=True,
            )

    @parametrize
    def test_method_list(self, client: StudioSDK) -> None:
        locate_order = client.accounts.locate_orders.list(
            "x",
        )
        assert_matches_type(LocateOrderListResponse, locate_order, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: StudioSDK) -> None:
        response = client.accounts.locate_orders.with_raw_response.list(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate_order = response.parse()
        assert_matches_type(LocateOrderListResponse, locate_order, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: StudioSDK) -> None:
        with client.accounts.locate_orders.with_streaming_response.list(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate_order = response.parse()
            assert_matches_type(LocateOrderListResponse, locate_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.locate_orders.with_raw_response.list(
                "",
            )


class TestAsyncLocateOrders:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncStudioSDK) -> None:
        locate_order = await async_client.accounts.locate_orders.create(
            account_id="x",
            mpid="x",
            quantity="x",
            reference_id="my-order-id-123",
            symbol="AAPL",
        )
        assert_matches_type(LocateOrder, locate_order, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncStudioSDK) -> None:
        locate_order = await async_client.accounts.locate_orders.create(
            account_id="x",
            mpid="x",
            quantity="x",
            reference_id="my-order-id-123",
            symbol="AAPL",
            comments="comments",
        )
        assert_matches_type(LocateOrder, locate_order, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.locate_orders.with_raw_response.create(
            account_id="x",
            mpid="x",
            quantity="x",
            reference_id="my-order-id-123",
            symbol="AAPL",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate_order = await response.parse()
        assert_matches_type(LocateOrder, locate_order, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.locate_orders.with_streaming_response.create(
            account_id="x",
            mpid="x",
            quantity="x",
            reference_id="my-order-id-123",
            symbol="AAPL",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate_order = await response.parse()
            assert_matches_type(LocateOrder, locate_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.locate_orders.with_raw_response.create(
                account_id="",
                mpid="x",
                quantity="x",
                reference_id="my-order-id-123",
                symbol="AAPL",
            )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStudioSDK) -> None:
        locate_order = await async_client.accounts.locate_orders.retrieve(
            locate_order_id="x",
            account_id="x",
        )
        assert_matches_type(LocateOrder, locate_order, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.locate_orders.with_raw_response.retrieve(
            locate_order_id="x",
            account_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate_order = await response.parse()
        assert_matches_type(LocateOrder, locate_order, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.locate_orders.with_streaming_response.retrieve(
            locate_order_id="x",
            account_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate_order = await response.parse()
            assert_matches_type(LocateOrder, locate_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.locate_orders.with_raw_response.retrieve(
                locate_order_id="x",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locate_order_id` but received ''"):
            await async_client.accounts.locate_orders.with_raw_response.retrieve(
                locate_order_id="",
                account_id="x",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncStudioSDK) -> None:
        locate_order = await async_client.accounts.locate_orders.update(
            locate_order_id="x",
            account_id="x",
            accept=True,
        )
        assert locate_order is None

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.locate_orders.with_raw_response.update(
            locate_order_id="x",
            account_id="x",
            accept=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate_order = await response.parse()
        assert locate_order is None

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.locate_orders.with_streaming_response.update(
            locate_order_id="x",
            account_id="x",
            accept=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate_order = await response.parse()
            assert locate_order is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.locate_orders.with_raw_response.update(
                locate_order_id="x",
                account_id="",
                accept=True,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `locate_order_id` but received ''"):
            await async_client.accounts.locate_orders.with_raw_response.update(
                locate_order_id="",
                account_id="x",
                accept=True,
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncStudioSDK) -> None:
        locate_order = await async_client.accounts.locate_orders.list(
            "x",
        )
        assert_matches_type(LocateOrderListResponse, locate_order, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.locate_orders.with_raw_response.list(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        locate_order = await response.parse()
        assert_matches_type(LocateOrderListResponse, locate_order, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.locate_orders.with_streaming_response.list(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            locate_order = await response.parse()
            assert_matches_type(LocateOrderListResponse, locate_order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.locate_orders.with_raw_response.list(
                "",
            )
