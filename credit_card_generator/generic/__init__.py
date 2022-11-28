from enum import Enum
from typing import NamedTuple, Optional, Tuple, Union
from datetime import date, timedelta
import random
from ..utils import luhn_compute

class CardType(int, Enum):
    VISA = (4, 'VISA')
    MasterCard = (5, 'MASTERCARD')
    Discover = (6, 'DISCOVER')
    Other = (3, 'OTHER')
    def __new__(cls, value: int, label: str):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj.label = label
        return obj


class Card(NamedTuple):
    type: str
    number: int
    exp_date: date
    cvc: int
    secret_code: int

def generate_card(card_type: CardType, 
                  bank_number: Optional[Union[int, str]] = None, 
                  account_number: Optional[Union[int, str]] = None,
                  range_exp_date: Optional[Tuple[date, date]] = None,
                  cvc: Optional[Union[int, str]] = None,
                  secret_code: Optional[Union[int, str]] = None) -> Card:

    bank_number =      f'{bank_number:0>5}'     if bank_number     else f'{random.randrange(0, 100_000):0>5}'
    account_number =   f'{account_number:0>15}' if account_number  else f'{random.randrange(0, 1_000_000_000_000_000):0>15}'
    cvc =              f'{cvc:0>3}'             if cvc             else f'{random.randrange(0, 1_000):0>3}'
    secret_code =      f'{secret_code:0>4}'     if secret_code     else f'{random.randrange(0, 10_000):0>4}'

    variable_error: Optional[Tuple[str, int]] = None
    if len(bank_number) != 5: variable_error = ("bank number", 5)
    if len(account_number) != 15: variable_error = ("account number", 15)
    if len(cvc) != 3: variable_error = ("cvc", 3)
    if variable_error:
        (variable_name, variable_len) = variable_error
        raise TypeError(f"{variable_name} shoule have a length of {variable_len}")

    card_number = str(card_type.value)
    card_number += bank_number
    card_number += account_number
    card_number += str(luhn_compute(card_number))

    if not range_exp_date:
        current_date = date.today()
        range_exp_date = (
            date(current_date.year + 2, current_date.month, 1),
            date(current_date.year + 5, current_date.month, 1),
        )
    
    (start_date, end_date) = range_exp_date
    res_dates = [start_date]
    if start_date > end_date:
        raise Exception("end date should be superior to start date")
    while start_date != end_date:
        start_date += timedelta(days=1)
        res_dates.append(start_date)
    exp_date = random.choice(res_dates)

    card = Card(
        type=card_type.label,
        number=int(card_number),
        exp_date=exp_date,
        cvc=int(cvc),
        secret_code=int(secret_code)
    )
    return card