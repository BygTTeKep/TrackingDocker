from celery import shared_task, signals
from celery_config import app
import time
import docker
from celery_singleton import Singleton
# from .views import client


# @shared_task(base=Singleton)
# def status_container() -> dict:
#         client = docker.from_env()
#         cs = {}
#         for container in client.containers.list(all=True):
#             # добавить проверку для кэширования
#             if container.attrs["State"]["Running"]:
#                 cs[container.short_id] = True
#             else: cs[container.short_id] = False
#         return cs
# На фон инициализация docker swarm и leave
@app.task
def init_docker_swarm_task(command):
    client = docker.from_env()
    return client.swarm.init(command)
    # print("id")

# @shared_task(base=Singleton)
# def leave_docker_swarm():
#     client = docker.from_env()
#     if docker.DockerClient.info(client)["Swarm"]["Managers"] == 1:
#         client.swarm.leave(force=True)
#     else: client.swarm.leave()
