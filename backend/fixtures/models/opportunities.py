from dataclasses import dataclass
from datetime import datetime


@dataclass
class OpportunityStub:
    name: str
    description: str

    expires_at: datetime
