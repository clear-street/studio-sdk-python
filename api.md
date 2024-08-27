# Shared Types

```python
from studio_sdk.types import (
    LocateOrder,
    Order,
    PnlSummaryForAccount,
    Position,
    RegtMarginSimulation,
    Trade,
)
```

# Entities

Types:

```python
from studio_sdk.types import Entity, PnlSummary, PortfolioMargin, RegtMargin, EntityListResponse
```

Methods:

- <code title="get /entities/{entity_id}">client.entities.<a href="./src/studio_sdk/resources/entities/entities.py">retrieve</a>(entity_id) -> <a href="./src/studio_sdk/types/entity.py">Entity</a></code>
- <code title="get /entities">client.entities.<a href="./src/studio_sdk/resources/entities/entities.py">list</a>() -> <a href="./src/studio_sdk/types/entity_list_response.py">EntityListResponse</a></code>

## PnlSummaries

Methods:

- <code title="get /entities/{entity_id}/pnl-summary">client.entities.pnl_summaries.<a href="./src/studio_sdk/resources/entities/pnl_summaries.py">retrieve</a>(entity_id) -> <a href="./src/studio_sdk/types/pnl_summary.py">PnlSummary</a></code>

## RegtMargins

Methods:

- <code title="get /entities/{entity_id}/regt-margin">client.entities.regt_margins.<a href="./src/studio_sdk/resources/entities/regt_margins.py">retrieve</a>(entity_id) -> <a href="./src/studio_sdk/types/regt_margin.py">RegtMargin</a></code>

## PortfolioMargins

Methods:

- <code title="get /entities/{entity_id}/portfolio-margin">client.entities.portfolio_margins.<a href="./src/studio_sdk/resources/entities/portfolio_margins.py">retrieve</a>(entity_id) -> <a href="./src/studio_sdk/types/portfolio_margin.py">PortfolioMargin</a></code>

## RegtMarginSimulations

Types:

```python
from studio_sdk.types.entities import SimulationID, RegtMarginSimulationCreateResponse
```

Methods:

- <code title="post /entities/{entity_id}/regt-margin-simulations">client.entities.regt_margin_simulations.<a href="./src/studio_sdk/resources/entities/regt_margin_simulations.py">create</a>(entity_id, \*\*<a href="src/studio_sdk/types/entities/regt_margin_simulation_create_params.py">params</a>) -> <a href="./src/studio_sdk/types/entities/regt_margin_simulation_create_response.py">RegtMarginSimulationCreateResponse</a></code>
- <code title="get /entities/{entity_id}/regt-margin-simulations/{simulation_id}">client.entities.regt_margin_simulations.<a href="./src/studio_sdk/resources/entities/regt_margin_simulations.py">retrieve</a>(simulation_id, \*, entity_id) -> <a href="./src/studio_sdk/types/shared/regt_margin_simulation.py">RegtMarginSimulation</a></code>

# Accounts

Types:

```python
from studio_sdk.types import Account, AccountListResponse
```

Methods:

- <code title="get /accounts/{account_id}">client.accounts.<a href="./src/studio_sdk/resources/accounts/accounts.py">retrieve</a>(account_id) -> <a href="./src/studio_sdk/types/account.py">Account</a></code>
- <code title="get /accounts">client.accounts.<a href="./src/studio_sdk/resources/accounts/accounts.py">list</a>() -> <a href="./src/studio_sdk/types/account_list_response.py">AccountListResponse</a></code>

## BulkOrders

Types:

```python
from studio_sdk.types.accounts import BulkOrderCreateResponse
```

Methods:

- <code title="post /accounts/{account_id}/bulk-orders">client.accounts.bulk_orders.<a href="./src/studio_sdk/resources/accounts/bulk_orders.py">create</a>(account_id, \*\*<a href="src/studio_sdk/types/accounts/bulk_order_create_params.py">params</a>) -> <a href="./src/studio_sdk/types/accounts/bulk_order_create_response.py">BulkOrderCreateResponse</a></code>

## Orders

Types:

```python
from studio_sdk.types.accounts import (
    OrderCreateResponse,
    OrderRetrieveResponse,
    OrderListResponse,
    OrderDeleteResponse,
)
```

Methods:

- <code title="post /accounts/{account_id}/orders">client.accounts.orders.<a href="./src/studio_sdk/resources/accounts/orders.py">create</a>(account_id, \*\*<a href="src/studio_sdk/types/accounts/order_create_params.py">params</a>) -> <a href="./src/studio_sdk/types/accounts/order_create_response.py">OrderCreateResponse</a></code>
- <code title="get /accounts/{account_id}/orders/{order_id}">client.accounts.orders.<a href="./src/studio_sdk/resources/accounts/orders.py">retrieve</a>(order_id, \*, account_id) -> <a href="./src/studio_sdk/types/accounts/order_retrieve_response.py">OrderRetrieveResponse</a></code>
- <code title="get /accounts/{account_id}/orders">client.accounts.orders.<a href="./src/studio_sdk/resources/accounts/orders.py">list</a>(account_id, \*\*<a href="src/studio_sdk/types/accounts/order_list_params.py">params</a>) -> <a href="./src/studio_sdk/types/accounts/order_list_response.py">OrderListResponse</a></code>
- <code title="delete /accounts/{account_id}/orders">client.accounts.orders.<a href="./src/studio_sdk/resources/accounts/orders.py">delete</a>(account_id, \*\*<a href="src/studio_sdk/types/accounts/order_delete_params.py">params</a>) -> <a href="./src/studio_sdk/types/accounts/order_delete_response.py">OrderDeleteResponse</a></code>
- <code title="delete /accounts/{account_id}/orders/{order_id}">client.accounts.orders.<a href="./src/studio_sdk/resources/accounts/orders.py">cancel</a>(order_id, \*, account_id) -> None</code>

## Trades

Types:

```python
from studio_sdk.types.accounts import TradeListResponse
```

Methods:

- <code title="get /accounts/{account_id}/trades/{trade_id}">client.accounts.trades.<a href="./src/studio_sdk/resources/accounts/trades.py">retrieve</a>(trade_id, \*, account_id) -> <a href="./src/studio_sdk/types/shared/trade.py">Trade</a></code>
- <code title="get /accounts/{account_id}/trades">client.accounts.trades.<a href="./src/studio_sdk/resources/accounts/trades.py">list</a>(account_id, \*\*<a href="src/studio_sdk/types/accounts/trade_list_params.py">params</a>) -> <a href="./src/studio_sdk/types/accounts/trade_list_response.py">TradeListResponse</a></code>

## Positions

Types:

```python
from studio_sdk.types.accounts import PositionListResponse
```

Methods:

- <code title="get /accounts/{account_id}/positions/{symbol}">client.accounts.positions.<a href="./src/studio_sdk/resources/accounts/positions.py">retrieve</a>(symbol, \*, account_id) -> <a href="./src/studio_sdk/types/shared/position.py">Position</a></code>
- <code title="get /accounts/{account_id}/positions">client.accounts.positions.<a href="./src/studio_sdk/resources/accounts/positions.py">list</a>(account_id, \*\*<a href="src/studio_sdk/types/accounts/position_list_params.py">params</a>) -> <a href="./src/studio_sdk/types/accounts/position_list_response.py">PositionListResponse</a></code>

## LocateOrders

Types:

```python
from studio_sdk.types.accounts import LocateOrderListResponse
```

Methods:

- <code title="post /accounts/{account_id}/locate-orders">client.accounts.locate_orders.<a href="./src/studio_sdk/resources/accounts/locate_orders.py">create</a>(account_id, \*\*<a href="src/studio_sdk/types/accounts/locate_order_create_params.py">params</a>) -> <a href="./src/studio_sdk/types/shared/locate_order.py">LocateOrder</a></code>
- <code title="get /accounts/{account_id}/locate-orders/{locate_order_id}">client.accounts.locate_orders.<a href="./src/studio_sdk/resources/accounts/locate_orders.py">retrieve</a>(locate_order_id, \*, account_id) -> <a href="./src/studio_sdk/types/shared/locate_order.py">LocateOrder</a></code>
- <code title="patch /accounts/{account_id}/locate-orders/{locate_order_id}">client.accounts.locate_orders.<a href="./src/studio_sdk/resources/accounts/locate_orders.py">update</a>(locate_order_id, \*, account_id, \*\*<a href="src/studio_sdk/types/accounts/locate_order_update_params.py">params</a>) -> None</code>
- <code title="get /accounts/{account_id}/locate-orders">client.accounts.locate_orders.<a href="./src/studio_sdk/resources/accounts/locate_orders.py">list</a>(account_id) -> <a href="./src/studio_sdk/types/accounts/locate_order_list_response.py">LocateOrderListResponse</a></code>

## EasyBorrows

Types:

```python
from studio_sdk.types.accounts import EasyBorrowListResponse
```

Methods:

- <code title="get /accounts/{account_id}/easy-borrows">client.accounts.easy_borrows.<a href="./src/studio_sdk/resources/accounts/easy_borrows.py">list</a>(account_id) -> <a href="./src/studio_sdk/types/accounts/easy_borrow_list_response.py">EasyBorrowListResponse</a></code>

## PnlSummary

Methods:

- <code title="get /accounts/{account_id}/pnl-summary">client.accounts.pnl_summary.<a href="./src/studio_sdk/resources/accounts/pnl_summary.py">retrieve</a>(account_id) -> <a href="./src/studio_sdk/types/pnl_summary.py">PnlSummary</a></code>

## PnlDetails

Types:

```python
from studio_sdk.types.accounts import PnlDetailListResponse
```

Methods:

- <code title="get /accounts/{account_id}/pnl-details">client.accounts.pnl_details.<a href="./src/studio_sdk/resources/accounts/pnl_details.py">list</a>(account_id) -> <a href="./src/studio_sdk/types/accounts/pnl_detail_list_response.py">PnlDetailListResponse</a></code>

# Instruments

Types:

```python
from studio_sdk.types import Instrument
```

Methods:

- <code title="get /instruments/{symbol}">client.instruments.<a href="./src/studio_sdk/resources/instruments.py">retrieve</a>(symbol, \*\*<a href="src/studio_sdk/types/instrument_retrieve_params.py">params</a>) -> <a href="./src/studio_sdk/types/instrument.py">Instrument</a></code>
