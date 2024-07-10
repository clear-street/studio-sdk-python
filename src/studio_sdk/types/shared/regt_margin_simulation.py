# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..._models import BaseModel
from ..regt_margin import RegtMargin
from ..entities.simulation_id import SimulationID

__all__ = ["RegtMarginSimulation"]


class RegtMarginSimulation(BaseModel):
    after: RegtMargin
    """The margin calculation after applying simulated trades."""

    before: RegtMargin
    """The margin calculation before applying simulated trades."""

    created_at: int
    """Timestamp of when this simulation was created."""

    name: str
    """Name of this simulation that you provided when creating it."""

    simulation_id: SimulationID
    """Unique ID for a simulation."""
