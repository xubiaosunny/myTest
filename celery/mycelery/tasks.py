#-*- coding:utf-8 -*-
from __future__ import absolute_import
from .celery import app
import time
@app.task
def add(x,y):
    return x+y
    
@app.task(bind=True)
def hello(self, a, b):
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 50})
    time.sleep(1)
    self.update_state(state="PROGRESS", meta={'progress': 90})
    time.sleep(1)
    return 'hello world: %i' % (a+b)

@app.task
def mytest():
    with open("test.txt", "w") as f:
        f.write('123\r\n')
        f.write('123\r\n')

from celery.signals import after_task_publish

@after_task_publish.connect
def task_sent_handler(sender=None, headers=None, body=None, **kwargs):
    # information about task are located in headers for task messages
    # using the task protocol version 2.
    info = headers if 'task' in headers else body
    print('after_task_publish for task id {info[id]}'.format(
        info=info,
    ))