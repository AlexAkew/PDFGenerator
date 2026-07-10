from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True, frozen=True)
class StatementPeriod:
    """
    Reporting period.
    """

    start: datetime
    end: datetime