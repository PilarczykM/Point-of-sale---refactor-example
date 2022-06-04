from pay.order import Order
from pay.processor import PaymentProcessor


def pay_order(order: Order):
    if order.total == 0:
        raise ValueError("Can not pay an order with total of 0 items.")
    card = input("Please enter your credit number: ")
    month = int(input("Please enter the card expiry month: "))
    year = int(input("Please enter the card expiry year: "))
    payment_process = PaymentProcessor("6cfb67f3-6281-4031-b893-ea85db0dce20")
    payment_process.charge(card, month, year, order.total)
    order.pay()
