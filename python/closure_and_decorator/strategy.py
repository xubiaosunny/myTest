from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:  
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0 
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):
    @abstractmethod
    def discount(self, order):
        ''''''

class FidelityPromo(Promotion):
    def discount(self, order):
        return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount 


class LargeOrderPromo(Promotion):
    def discount(self, order):
        discount_items = {item.product for item in order.cart}
        if len(discount_items) >= 10:
            return order.total() * .07
        return 0


if __name__ == '__main__':
    joe = Customer('Jone Doe', 0)
    ann = Customer('Ann Smith', 1100)
    cart = [
        LineItem('banana', 30, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0),
        ]
    joe_order = Order(joe, cart, FidelityPromo())
    ann_order = Order(ann, cart, FidelityPromo())
    print(joe_order, ann_order)
    print(
        Order(ann, cart, BulkItemPromo()),
        Order(ann, cart, LargeOrderPromo())
        )

