import dataclasses
from enum import Enum


class OrderStatus(Enum):
    OPEN = "open"
    PAID = "paid"


@dataclasses
class Item:
    name: str
    price: int
    quantity: int = 1

    @property
    def total(self):
        return self.price * self.quantity


@dataclasses
class Order:
    item: list[Item] = dataclasses.field(default_factory=list)
    status: OrderStatus = OrderStatus.OPEN

    @property
    def total(self) -> int:
        return sum(item.total for item in self.item)

    @property
    def pay(self):
        self.status = OrderStatus.PAID
