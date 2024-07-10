# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..pnl_summary import PnlSummary

__all__ = ["PnlSummaryForAccount"]


class PnlSummaryForAccount(PnlSummary):
    account_id: str
    """Account ID"""
