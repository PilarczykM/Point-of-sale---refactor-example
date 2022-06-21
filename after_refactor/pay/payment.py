from typing import Protocol

from pay.credit_card import CreditCard
from pay.order import Order


class Payment(Protocol):
    def charge(self, card: CreditCard, amount: int) -> None:
        """Charges the card with the amount"""


def pay_order(order: Order, card: CreditCard, payment: Payment):
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    payment.charge(card, amount=order.total)
    order.pay()
