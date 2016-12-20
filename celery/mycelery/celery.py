#-*- coding:utf-8 -*-
from celery import Celery

app = Celery("mycelery")
app.config_from_object("celeryconfig")

if __name__ == "__main__":
    app.start()
