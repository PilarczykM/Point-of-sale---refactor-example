from pay.order import Order, LineItem, OrderStatus


def test_empty_order_total() -> None:
    order = Order()
    assert order.total == 0
    assert order.status == OrderStatus.OPEN


def test_order_total() -> None:
    order = Order()
    order.line_items.append(LineItem("Test", 100))
    assert order.total == 100


def test_order_pay() -> None:
    order = Order()
    order.pay()

    assert order.status == OrderStatus.PAID
