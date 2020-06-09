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


class LineItem2:
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    def get_weight(self):
        return self.__weight

    def set_weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('value must be > 0')

    weight = property(get_weight, set_weight)

if __name__ == '__main__':
    line_item = LineItem('test', 10, 5.22)
    print(line_item.subtotal())
    line_item.weight = 20
    print(line_item.subtotal())
    # line_item.weight = -10

    line_item = LineItem2('test', 10, 5.22)
    print(line_item.subtotal())
    line_item.weight = 20
    print(line_item.subtotal())
    # line_item.weight = -10
