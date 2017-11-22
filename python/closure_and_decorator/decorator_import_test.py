
def register(func):
    print(123)
    return func


@register
def test1():
    print(456)


@register
def test2():
    print(789)

if __name__ == '__main__':
    print('start')
    test1()
    test2()