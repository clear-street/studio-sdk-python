# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..._models import BaseModel
from .simulation_id import SimulationID

__all__ = ["RegtMarginSimulationCreateResponse"]


class RegtMarginSimulationCreateResponse(BaseModel):
    simulation_id: SimulationID
    """Unique ID for a simulation."""
