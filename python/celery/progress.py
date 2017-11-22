from __future__ import absolute_import
from mycelery.tasks import hello

def on_raw_message(body):
    print(body)

r = hello.apply_async((1,2))
print(r.get(on_message=on_raw_message, propagate=False))
