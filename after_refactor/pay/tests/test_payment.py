import pytest

from pay.order import Order, LineItem
from pay.payment import pay_order

from pytest import MonkeyPatch

from pay.processor import PaymentProcessor


def test_pay_order_with_total_zero_raises_value_error() -> None:
    order = Order()
    with pytest.raises(ValueError):
        pay_order(order)


def test_pay_order_default(monkeypatch: MonkeyPatch) -> None:
    def charge_mock(self: PaymentProcessor, card: str, month: int, year: int, amount: int) -> None:
        pass

    responses = iter(["1249190007575069", "12", "2024"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))
    monkeypatch.setattr(PaymentProcessor, "_check_api_key", lambda _: True)
    monkeypatch.setattr(PaymentProcessor, "charge", charge_mock)

    order = Order()
    order.line_items.append(LineItem(name="Test", price=100))
    pay_order(order)
