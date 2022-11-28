from enum import Enum
from typing import NamedTuple, Optional, Tuple
from datetime import date
from ..utils import luhn_compute

class CardType(int, Enum):
    VISA = (4, 'VISA')
    MasterCard = (5, 'MASTERCARD')
    Discover = (6, 'DISCOVER')
    Other = (3, 'OTHER')
    def __new__(cls, value, label):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.label = label
        return obj


class Card(NamedTuple):
    type: CardType
    number: int
    exp_date: date
    cvc: int
    secret_code: int

def generate_card(card_type: CardType, 
                  bank_number: Optional[int] = None, 
                  account_number: Optional[int] = None,
                  range_exp_date: Optional[Tuple[date, date]] = None,
                  cvc: Optional[int] = None,
                  secret_code: Optional[int] = None) -> Card:
    card_number = card_type.value * pow(10, 14)
    card_number += bank_number * pow(10, 9)
    card_number += account_number
    card_number = (card_number*10) + luhn_compute(card_number)
    card = Card(
        type=card_type.label
        # number=
    )