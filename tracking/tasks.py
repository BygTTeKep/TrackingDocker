from celery import shared_task
import time
import docker
from celery_singleton import Singleton

# @app.task()
# def status_container():
#     while True:
#         for container in client.containers.list(all=True):
#             if container.attrs["State"]["Running"]:

#добавить else

@shared_task(base=Singleton)
def status_container() -> dict:
        client = docker.from_env()
        cs = {}
        for container in client.containers.list(all=True):
            if container.attrs["State"]["Running"]:
                cs[container.short_id] = True
            else: cs[container.short_id] = False
        return cs