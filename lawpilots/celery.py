from __future__ import absolute_import, unicode_literals

from celery import Celery
import os

RABBITMQ_DEFAULT_USER = os.getenv("RABBITMQ_DEFAULT_USER")
RABBITMQ_DEFAULT_PASS = os.getenv("RABBITMQ_DEFAULT_PASS")

app = Celery(
    "lawpilots",
    broker=f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@rabbitmq:5672",
    backend="rpc://",
    include=["lawpilots.tasks"],
)
if __name__ == "__main__":
    app.start()
