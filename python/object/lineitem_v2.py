# -*- coding: utf-8 -*-


class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')


if __name__ == '__main__':
    line_item = LineItem('test', 10, 5.22)
    print(line_item.subtotal())
    line_item.weight = 20
    print(line_item.subtotal())
    line_item.weight = -10
