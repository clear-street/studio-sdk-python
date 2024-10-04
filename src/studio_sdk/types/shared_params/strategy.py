# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .base_strategy import BaseStrategy

__all__ = ["Strategy", "DmaStrategy"]


class DmaStrategy(TypedDict, total=False):
    destination: Required[
        Literal[
            "arcx",
            "bats",
            "baty",
            "edga",
            "edgx",
            "eprl",
            "gotc",
            "iexg",
            "memx",
            "xase",
            "xbos",
            "xcis",
            "xchi",
            "xnms",
            "xnys",
            "xphl",
        ]
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
    <td>GOTC</td>
    <td>ARCA Global OTC</td>
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
    <td>XCHI</td>
    <td>Chicago Stock Exchange</td>
    </tr>
    <tr>
    <td>XNMS</td>
    <td>NASDAQ/NMS (Global Market)</td>
    </tr>
    <tr>
    <td>XNYS</td>
    <td>New York Stock Exchange</td>
    </tr>
    <tr>
    <td>XPHL</td>
    <td>NASDAQ PHLX Exchange</td>
    </tr>
    </tbody></table>
    """

    type: Required[Literal["sor", "dark", "ap", "pov", "twap", "vwap", "dma"]]
    """The type of strategy. This must be set to the respective strategy type."""


Strategy: TypeAlias = Union[
    BaseStrategy, BaseStrategy, BaseStrategy, BaseStrategy, BaseStrategy, BaseStrategy, DmaStrategy
]
