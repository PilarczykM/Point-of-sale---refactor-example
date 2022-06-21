import pytest

from pay.credit_card import CreditCard
from pay.order import Order, LineItem
from pay.payment import pay_order


@pytest.fixture
def card() -> CreditCard:
    return CreditCard("1249190007575069", 12, 2024)


class PaymentProcessorMock:
    @staticmethod
    def charge(card: CreditCard, amount: int) -> None:
        print(f"Charging {card.number} with amount ${amount / 100:.2f}.")


def test_pay_order_with_total_zero_raises_value_error(card: CreditCard) -> None:
    order = Order()
    with pytest.raises(ValueError):
        pay_order(order, card, PaymentProcessorMock())


def test_pay_order_default(card: CreditCard) -> None:
    order = Order()
    order.line_items.append(LineItem(name="Test", price=100))
    pay_order(order, card, PaymentProcessorMock())
