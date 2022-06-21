from typing import Protocol
from pay.order import Order


class Payment(Protocol):
    def charge(self, card: str, month: int, year: int, amount: int) -> None:
        """Charges the card with the amount"""


def pay_order(order: Order, payment: Payment):
    if order.total == 0:
        raise ValueError("Can't pay an order with total 0.")
    card = input("Please enter card number: ")
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))
    payment.charge(card, month, year, amount=order.total)
    order.pay()
