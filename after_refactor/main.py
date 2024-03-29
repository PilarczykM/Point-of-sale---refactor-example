from pay.order import Order, LineItem
from pay.payment import pay_order


def main():
    # Test card number: 1249190007575069

    card = input("Please enter card number: ")
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))

    order = Order()
    order.line_items.append(LineItem(name="Shoes", price=100_00, quantity=2))
    order.line_items.append(LineItem(name="Hat", price=10_00))
    pay_order(order)


if __name__ == '__main__':
    main()
