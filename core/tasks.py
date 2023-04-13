from .models import File

from celery import task


@task
def add(x, y):
    return x + y


@task
def count_widgets():
    return File.objects.count()

