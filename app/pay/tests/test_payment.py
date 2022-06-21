import pytest

from pay.order import Order, LineItem
from pay.payment import pay_order

from pytest import MonkeyPatch

def test_pay_order_with_total_zero_raises_value_error() -> None:
    order = Order()
    with pytest.raises(ValueError):
        pay_order(order)


def test_pay_order_default(monkeypatch: MonkeyPatch) -> None:
    responses = iter(["1249190007575069", "12", "2024"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    order = Order()
    order.line_items.append(LineItem(name="Test", price=100))
    pay_order(order)
