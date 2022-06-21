from pay.order import LineItem


def test_line_item_default() -> None:
    line_item = LineItem("Test", 100)
    assert line_item.total == 100


def test_line_item_qith_quantity_equal_5_returns_correct_total_price() -> None:
    line_item = LineItem("Test", 200, 5)
    assert line_item.total == 1000
