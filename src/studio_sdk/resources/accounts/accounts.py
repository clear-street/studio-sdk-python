# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .orders import (
    OrdersResource,
    AsyncOrdersResource,
    OrdersResourceWithRawResponse,
    AsyncOrdersResourceWithRawResponse,
    OrdersResourceWithStreamingResponse,
    AsyncOrdersResourceWithStreamingResponse,
)
from .trades import (
    TradesResource,
    AsyncTradesResource,
    TradesResourceWithRawResponse,
    AsyncTradesResourceWithRawResponse,
    TradesResourceWithStreamingResponse,
    AsyncTradesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from .positions import (
    PositionsResource,
    AsyncPositionsResource,
    PositionsResourceWithRawResponse,
    AsyncPositionsResourceWithRawResponse,
    PositionsResourceWithStreamingResponse,
    AsyncPositionsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .bulk_orders import (
    BulkOrdersResource,
    AsyncBulkOrdersResource,
    BulkOrdersResourceWithRawResponse,
    AsyncBulkOrdersResourceWithRawResponse,
    BulkOrdersResourceWithStreamingResponse,
    AsyncBulkOrdersResourceWithStreamingResponse,
)
from .pnl_details import (
    PnlDetailsResource,
    AsyncPnlDetailsResource,
    PnlDetailsResourceWithRawResponse,
    AsyncPnlDetailsResourceWithRawResponse,
    PnlDetailsResourceWithStreamingResponse,
    AsyncPnlDetailsResourceWithStreamingResponse,
)
from .pnl_summary import (
    PnlSummaryResource,
    AsyncPnlSummaryResource,
    PnlSummaryResourceWithRawResponse,
    AsyncPnlSummaryResourceWithRawResponse,
    PnlSummaryResourceWithStreamingResponse,
    AsyncPnlSummaryResourceWithStreamingResponse,
)
from .easy_borrows import (
    EasyBorrowsResource,
    AsyncEasyBorrowsResource,
    EasyBorrowsResourceWithRawResponse,
    AsyncEasyBorrowsResourceWithRawResponse,
    EasyBorrowsResourceWithStreamingResponse,
    AsyncEasyBorrowsResourceWithStreamingResponse,
)
from .locate_orders import (
    LocateOrdersResource,
    AsyncLocateOrdersResource,
    LocateOrdersResourceWithRawResponse,
    AsyncLocateOrdersResourceWithRawResponse,
    LocateOrdersResourceWithStreamingResponse,
    AsyncLocateOrdersResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.account import Account
from ...types.account_list_response import AccountListResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def bulk_orders(self) -> BulkOrdersResource:
        return BulkOrdersResource(self._client)

    @cached_property
    def orders(self) -> OrdersResource:
        return OrdersResource(self._client)

    @cached_property
    def trades(self) -> TradesResource:
        return TradesResource(self._client)

    @cached_property
    def positions(self) -> PositionsResource:
        return PositionsResource(self._client)

    @cached_property
    def locate_orders(self) -> LocateOrdersResource:
        return LocateOrdersResource(self._client)

    @cached_property
    def easy_borrows(self) -> EasyBorrowsResource:
        return EasyBorrowsResource(self._client)

    @cached_property
    def pnl_summary(self) -> PnlSummaryResource:
        return PnlSummaryResource(self._client)

    @cached_property
    def pnl_details(self) -> PnlDetailsResource:
        return PnlDetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Get an account by its ID.

        Args:
          account_id: Account ID for the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountListResponse:
        """List all available accounts."""
        return self._get(
            "/accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountListResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def bulk_orders(self) -> AsyncBulkOrdersResource:
        return AsyncBulkOrdersResource(self._client)

    @cached_property
    def orders(self) -> AsyncOrdersResource:
        return AsyncOrdersResource(self._client)

    @cached_property
    def trades(self) -> AsyncTradesResource:
        return AsyncTradesResource(self._client)

    @cached_property
    def positions(self) -> AsyncPositionsResource:
        return AsyncPositionsResource(self._client)

    @cached_property
    def locate_orders(self) -> AsyncLocateOrdersResource:
        return AsyncLocateOrdersResource(self._client)

    @cached_property
    def easy_borrows(self) -> AsyncEasyBorrowsResource:
        return AsyncEasyBorrowsResource(self._client)

    @cached_property
    def pnl_summary(self) -> AsyncPnlSummaryResource:
        return AsyncPnlSummaryResource(self._client)

    @cached_property
    def pnl_details(self) -> AsyncPnlDetailsResource:
        return AsyncPnlDetailsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/clear-street/studio-sdk-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Account:
        """
        Get an account by its ID.

        Args:
          account_id: Account ID for the account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Account,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountListResponse:
        """List all available accounts."""
        return await self._get(
            "/accounts",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountListResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.list = to_raw_response_wrapper(
            accounts.list,
        )

    @cached_property
    def bulk_orders(self) -> BulkOrdersResourceWithRawResponse:
        return BulkOrdersResourceWithRawResponse(self._accounts.bulk_orders)

    @cached_property
    def orders(self) -> OrdersResourceWithRawResponse:
        return OrdersResourceWithRawResponse(self._accounts.orders)

    @cached_property
    def trades(self) -> TradesResourceWithRawResponse:
        return TradesResourceWithRawResponse(self._accounts.trades)

    @cached_property
    def positions(self) -> PositionsResourceWithRawResponse:
        return PositionsResourceWithRawResponse(self._accounts.positions)

    @cached_property
    def locate_orders(self) -> LocateOrdersResourceWithRawResponse:
        return LocateOrdersResourceWithRawResponse(self._accounts.locate_orders)

    @cached_property
    def easy_borrows(self) -> EasyBorrowsResourceWithRawResponse:
        return EasyBorrowsResourceWithRawResponse(self._accounts.easy_borrows)

    @cached_property
    def pnl_summary(self) -> PnlSummaryResourceWithRawResponse:
        return PnlSummaryResourceWithRawResponse(self._accounts.pnl_summary)

    @cached_property
    def pnl_details(self) -> PnlDetailsResourceWithRawResponse:
        return PnlDetailsResourceWithRawResponse(self._accounts.pnl_details)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            accounts.list,
        )

    @cached_property
    def bulk_orders(self) -> AsyncBulkOrdersResourceWithRawResponse:
        return AsyncBulkOrdersResourceWithRawResponse(self._accounts.bulk_orders)

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithRawResponse:
        return AsyncOrdersResourceWithRawResponse(self._accounts.orders)

    @cached_property
    def trades(self) -> AsyncTradesResourceWithRawResponse:
        return AsyncTradesResourceWithRawResponse(self._accounts.trades)

    @cached_property
    def positions(self) -> AsyncPositionsResourceWithRawResponse:
        return AsyncPositionsResourceWithRawResponse(self._accounts.positions)

    @cached_property
    def locate_orders(self) -> AsyncLocateOrdersResourceWithRawResponse:
        return AsyncLocateOrdersResourceWithRawResponse(self._accounts.locate_orders)

    @cached_property
    def easy_borrows(self) -> AsyncEasyBorrowsResourceWithRawResponse:
        return AsyncEasyBorrowsResourceWithRawResponse(self._accounts.easy_borrows)

    @cached_property
    def pnl_summary(self) -> AsyncPnlSummaryResourceWithRawResponse:
        return AsyncPnlSummaryResourceWithRawResponse(self._accounts.pnl_summary)

    @cached_property
    def pnl_details(self) -> AsyncPnlDetailsResourceWithRawResponse:
        return AsyncPnlDetailsResourceWithRawResponse(self._accounts.pnl_details)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            accounts.list,
        )

    @cached_property
    def bulk_orders(self) -> BulkOrdersResourceWithStreamingResponse:
        return BulkOrdersResourceWithStreamingResponse(self._accounts.bulk_orders)

    @cached_property
    def orders(self) -> OrdersResourceWithStreamingResponse:
        return OrdersResourceWithStreamingResponse(self._accounts.orders)

    @cached_property
    def trades(self) -> TradesResourceWithStreamingResponse:
        return TradesResourceWithStreamingResponse(self._accounts.trades)

    @cached_property
    def positions(self) -> PositionsResourceWithStreamingResponse:
        return PositionsResourceWithStreamingResponse(self._accounts.positions)

    @cached_property
    def locate_orders(self) -> LocateOrdersResourceWithStreamingResponse:
        return LocateOrdersResourceWithStreamingResponse(self._accounts.locate_orders)

    @cached_property
    def easy_borrows(self) -> EasyBorrowsResourceWithStreamingResponse:
        return EasyBorrowsResourceWithStreamingResponse(self._accounts.easy_borrows)

    @cached_property
    def pnl_summary(self) -> PnlSummaryResourceWithStreamingResponse:
        return PnlSummaryResourceWithStreamingResponse(self._accounts.pnl_summary)

    @cached_property
    def pnl_details(self) -> PnlDetailsResourceWithStreamingResponse:
        return PnlDetailsResourceWithStreamingResponse(self._accounts.pnl_details)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            accounts.list,
        )

    @cached_property
    def bulk_orders(self) -> AsyncBulkOrdersResourceWithStreamingResponse:
        return AsyncBulkOrdersResourceWithStreamingResponse(self._accounts.bulk_orders)

    @cached_property
    def orders(self) -> AsyncOrdersResourceWithStreamingResponse:
        return AsyncOrdersResourceWithStreamingResponse(self._accounts.orders)

    @cached_property
    def trades(self) -> AsyncTradesResourceWithStreamingResponse:
        return AsyncTradesResourceWithStreamingResponse(self._accounts.trades)

    @cached_property
    def positions(self) -> AsyncPositionsResourceWithStreamingResponse:
        return AsyncPositionsResourceWithStreamingResponse(self._accounts.positions)

    @cached_property
    def locate_orders(self) -> AsyncLocateOrdersResourceWithStreamingResponse:
        return AsyncLocateOrdersResourceWithStreamingResponse(self._accounts.locate_orders)

    @cached_property
    def easy_borrows(self) -> AsyncEasyBorrowsResourceWithStreamingResponse:
        return AsyncEasyBorrowsResourceWithStreamingResponse(self._accounts.easy_borrows)

    @cached_property
    def pnl_summary(self) -> AsyncPnlSummaryResourceWithStreamingResponse:
        return AsyncPnlSummaryResourceWithStreamingResponse(self._accounts.pnl_summary)

    @cached_property
    def pnl_details(self) -> AsyncPnlDetailsResourceWithStreamingResponse:
        return AsyncPnlDetailsResourceWithStreamingResponse(self._accounts.pnl_details)
