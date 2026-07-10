from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal


@dataclass(slots=True, frozen=True)
class Transaction:
    """
    Represents a single account transaction.
    """

    date: datetime
    transaction_id: str
    from_to: str
    purpose: str
    amount: Decimal
    balance: Decimal