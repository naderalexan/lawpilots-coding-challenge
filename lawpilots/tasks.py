from .celery import app


@app.task
def say_hello(name):
    return f"Hello {name}"
