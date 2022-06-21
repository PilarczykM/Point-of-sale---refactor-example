from pay.order import Order, OrderStatus, LineItem


def test_order_default() -> None:
    order = Order()
    assert order.status == OrderStatus.OPEN
    assert order.total == 0


def test_order_with_one_item() -> None:
    order = Order()
    order.line_items.append(LineItem(name="test", price=100))
    assert order.total == 100


def test_order_pay_change_status() -> None:
    order = Order()
    order.pay()
    assert order.status == OrderStatus.PAID
