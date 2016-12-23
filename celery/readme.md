# Celery Demo

## 1.相关配置

```python
from __future__ import absolute_import
from celery import Celery

app = Celery("mycelery")
app.config_from_object("celeryconfig")
``` 
> `from __future__ import absolute_import` 不导入absolute_import会报KeyError

> config_from_object 从文件中导入配置，celeryconfig.py:
```python
## Broker settings.
broker_url = 'redis://localhost:6379/0'
# List of modules to import when the Celery worker starts.
imports = ('mycelery.tasks',)
## Using the database to store task state and results.
result_backend = 'redis://localhost:6379/0'
task_serializer = 'json'
```
>> broker_url 采用redis作为中间人

>> imports 不配置，会报KeyError

>> 更多配置[http://docs.celeryproject.org/en/latest/userguide/configuration.html](http://docs.celeryproject.org/en/latest/userguide/configuration.html)

也可以直接配置

```python 
app = Celery('tasks', backend='redis://localhost', broker='pyamqp://')
```
或者
```python
app = Celery("mycelery")
app.conf.task_serializer = 'json'
```
配置多项
```python
app.conf.update(
    task_serializer='json',
    accept_content=['json'],  # Ignore other content
    result_serializer='json',
    timezone='Europe/Oslo',
    enable_utc=True,
)
```
## 2.运行Celery
```shell
celery -A mycelery worker --loglevel=info
```
## 3.[Flower](http://flower.readthedocs.io/en/latest/)监控工具
> 通过celery启动
```shell
celery flower -A mycelery --address=127.0.0.1 --port=5555
```
> 也可以通过flower本身启动,但是这样不知道如何指定地址（文档中没有发现）
```shell
flower -A proj --port=5555
```
## 4.[调用task](http://docs.celeryq.org/en/latest/userguide/calling.html#guide-calling)
> delay()
```python
from tasks import add
add.delay(4, 4)
```
> apply_async(args[, kwargs[, …]])
```python
add.apply_async((2, 2), link=add.s(16))
```

