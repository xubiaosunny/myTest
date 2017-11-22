#-*- coding:utf-8 -*-

import asyncio
import datetime
@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print("Hello again!")

async def test():
    print('hellp test')
async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)
async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

async def slow_operation(future):
    await asyncio.sleep(1)
    print('future')
    future.set_result('Future is done!')
def got_result(future):
    print(future.result())
    loop.stop()

async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1)
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))

# 获取EventLoop:
loop = asyncio.get_event_loop()
# tasks = [hello(),test(),display_date(loop)]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.run_until_complete(print_sum(2,3))
# future = asyncio.Future()
# asyncio.ensure_future(slow_operation(future))
# loop.run_until_complete(future)
# future.add_done_callback(got_result)
# try:
#     loop.run_forever()
# finally:
#     loop.close()
# print('123')
# loop.run_until_complete(asyncio.gather(
#     factorial("A", 2),
#     factorial("B", 3),
#     factorial("C", 4),
# ))
loop.close()
