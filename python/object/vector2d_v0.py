from array import array
import math


class Vector2d:
    # 想实例把弱引用目标，要把'__weakref__' 加入__slots__
    # 每个子类都要定义__slots__,因为解释器会忽略继承的__slots__属性
    # 实例只能拥有__slots__中列出的属性，除非把__dict__加入__solts__中（这样就会失去节省内存的功效）
    __slots__ = ('__x', '__y', '__weakref__')
    typecode = 'd'
    
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes([array(self.typecode, self)]))

    def __eq__(self):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast(typecode))
        return cls(*memv)
    
    # def __format__(self, fmt_spec=''):
    #     components = (format(c, fmt_spec) for c in self)
    #     return '({!r}, {!r})'.format(*components)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '<{}, {}>'

        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    def angle(self):
        return math.atan2(self.x, self.y)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


if __name__ == "__main__":
    v = Vector2d(3, 5)
    print('repr',repr(v))
    print('format',format(v, '.2fp'))
    print(hash(v))
    print(v.__slots__)