from __future__ import annotations

from dataclasses import dataclass

from .account import Account
from .statement_period import StatementPeriod
from .transaction import Transaction


@dataclass(slots=True, frozen=True)
class Statement:
    """
    Complete bank statement.
    """

    account: Account
    period: StatementPeriod
    transactions: list[Transaction]