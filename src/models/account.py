from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class Account:
    """
    Account information displayed in the statement.
    """

    holder_name: str
    address: str
    registration_number: str
    account_number: str
    currency: str