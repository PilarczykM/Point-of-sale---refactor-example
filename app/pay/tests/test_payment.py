import pytest
from pay.order import Order
from pay.payment import pay_order


def test_pay_order_with_total_zero_rises_value_error() -> None:
    order = Order()
    with pytest.raises(ValueError):
        pay_order(order)
