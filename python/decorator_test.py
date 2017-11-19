#-*- coding: utf-8 -*-
'''
lru_cache
'''
import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        ret = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))

        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_list.append(', ',join(pairs))

        arg_str = ', '.join(arg_list)

        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, ret))
        return ret
    
    return clocked

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


if __name__ == '__main__':
    fibonacci(200)