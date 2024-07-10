# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from studio_sdk import StudioSDK, AsyncStudioSDK
from tests.utils import assert_matches_type
from studio_sdk.types.shared import PnlSummaryForAccount

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPnlSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: StudioSDK) -> None:
        pnl_summary = client.accounts.pnl_summary.retrieve(
            "x",
        )
        assert_matches_type(PnlSummaryForAccount, pnl_summary, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: StudioSDK) -> None:
        response = client.accounts.pnl_summary.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pnl_summary = response.parse()
        assert_matches_type(PnlSummaryForAccount, pnl_summary, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: StudioSDK) -> None:
        with client.accounts.pnl_summary.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pnl_summary = response.parse()
            assert_matches_type(PnlSummaryForAccount, pnl_summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: StudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.pnl_summary.with_raw_response.retrieve(
                "",
            )


class TestAsyncPnlSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncStudioSDK) -> None:
        pnl_summary = await async_client.accounts.pnl_summary.retrieve(
            "x",
        )
        assert_matches_type(PnlSummaryForAccount, pnl_summary, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        response = await async_client.accounts.pnl_summary.with_raw_response.retrieve(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pnl_summary = await response.parse()
        assert_matches_type(PnlSummaryForAccount, pnl_summary, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncStudioSDK) -> None:
        async with async_client.accounts.pnl_summary.with_streaming_response.retrieve(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pnl_summary = await response.parse()
            assert_matches_type(PnlSummaryForAccount, pnl_summary, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncStudioSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.pnl_summary.with_raw_response.retrieve(
                "",
            )
