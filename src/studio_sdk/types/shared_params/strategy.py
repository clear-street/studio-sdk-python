# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .base_strategy import BaseStrategy

__all__ = ["Strategy", "VwapStrategy", "TwapStrategy", "ApStrategy", "PovStrategy", "DarkStrategy", "DmaStrategy"]


class VwapStrategy(BaseStrategy):
    max_percent: int
    """The maximum percentage of market volume.

    Must be an integer between 0 and 50 (inclusive).
    """

    min_percent: int
    """The minimum percentage of market volume.

    Must be an integer between 0 and 100 (inclusive).
    """


class TwapStrategy(BaseStrategy):
    max_percent: int
    """The maximum percentage of market volume.

    Must be an integer between 0 and 50 (inclusive).
    """

    min_percent: int
    """The minimum percentage of market volume.

    Must be an integer between 0 and 100 (inclusive).
    """


class ApStrategy(BaseStrategy):
    max_percent: int
    """The maximum percentage of market volume.

    Must be an integer between 0 and 100 (inclusive).
    """

    min_percent: int
    """The minimum percentage of market volume.

    Must be an integer between 0 and 100 (inclusive).
    """


class PovStrategy(BaseStrategy):
    target_percent: Required[int]
    """The target percentage of market volume.

    Must be an integer between 0 and 100 (inclusive).
    """


class DarkStrategy(BaseStrategy):
    max_percent: int
    """The maximum percentage of market volume.

    Must be an integer between 0 and 100 (inclusive).
    """


class DmaStrategy(TypedDict, total=False):
    destination: Required[
        Literal["arcx", "bats", "baty", "edga", "edgx", "eprl", "iexg", "memx", "xase", "xbos", "xcis", "xnms", "xnys"]
    ]
    """Order Destination.

    <table><thead>
    <tr>
    <th>MIC</th>
    <th>Exchange</th>
    </tr></thead>
    <tbody>
    <tr>
    <td>ARCX</td>
    <td>NYSE ARCA</td>
    </tr>
    <tr>
    <td>BATS</td>
    <td>BATS Exchange</td>
    </tr>
    <tr>
    <td>BATY</td>
    <td>BATS Y Exchange</td>
    </tr>
    <tr>
    <td>EDGA</td>
    <td>EDGA Exchange</td>
    </tr>
    <tr>
    <td>EDGX</td>
    <td>EDGX Exchange</td>
    </tr>
    <tr>
    <td>EPRL</td>
    <td>MIAX Pearl Equities</td>
    </tr>
    <tr>
    <td>IEXG</td>
    <td>Investors' Exchange</td>
    </tr>
    <tr>
    <td>MEMX</td>
    <td>Members' Exchange</td>
    </tr>
    <tr>
    <td>XASE</td>
    <td>NYSE American</td>
    </tr>
    <tr>
    <td>XBOS</td>
    <td>NASDAQ BX Exchange</td>
    </tr>
    <tr>
    <td>XCIS</td>
    <td>NYSE National</td>
    </tr>
    <tr>
    <td>XNMS</td>
    <td>NASDAQ/NMS (Global Market)</td>
    </tr>
    <tr>
    <td>XNYS</td>
    <td>New York Stock Exchange</td>
    </tr>
    </tbody></table>
    """

    type: Required[Literal["sor", "dark", "ap", "pov", "twap", "vwap", "dma"]]
    """Strategy type used for execution, can be one of below.

    - `sor`: Smart order router (default)
    - `dark`: Dark pool
    - `ap`: Arrival price
    - `pov`: Percentage of volume
    - `twap`: Time weighted average price
    - `vwap`: Volume weighted average price
    - `dma`: Direct market access

    For more information on these strategies, please refer to our
    [documentation](https://docs.clearstreet.io/studio/docs/execution-strategies).
    """


Strategy: TypeAlias = Union[
    BaseStrategy, VwapStrategy, TwapStrategy, ApStrategy, PovStrategy, DarkStrategy, DmaStrategy
]
