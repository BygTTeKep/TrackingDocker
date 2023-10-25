from django.urls import path, re_path
from rest_framework_swagger.views import get_swagger_view

# from django.conf.urls import url
from .views import (
    get_сontainers,
    detail_containers,
    get_images,
    get_containers_json,
    get_image_json,
    get_networks,
    get_volumes,
    get_volumes_json,
    detail_images,
    create_container,
    leave_docker_swarm,
    get_services_json,
    login_docker,
    init_docker_swarm,
    ContainerApi,
    ImageApi,
    NetworkApi,
    VolumesApi
)
# from .tasks import init_docker_swarm_task


app_name="tracking"
urlpatterns = [
    path("containers", get_сontainers, name="getContainers"),
    path("containers/<str:id>", detail_containers, name="detailContainers"),
    path("images", get_images, name="getImages"),
    path("images/<str:id>", detail_images, name="detailImages"),
    path("api/containers", get_containers_json, name="getContainersApi"),
    path("api/images", get_image_json, name="getImagesApi"),
    path("networks", get_networks, name="getNetworks"),
    path("volumes", get_volumes, name="getVolumes"),
    path("api/volumes", get_volumes_json, name="getVolumesApi"),
    path("api/services", get_services_json, name="getServicesApi"),
    path("create", create_container, name="create"),
    path("initSwarm", init_docker_swarm, name="initSwarm"),
    path("leaveSwarm", leave_docker_swarm, name="leaveSwarm"),
    path("login", login_docker, name="login"),
    path("doc/containers", ContainerApi.as_view()),
    path("doc/images", ImageApi.as_view()),
    path("doc/networks", NetworkApi.as_view()),
    path("doc/volumes", VolumesApi.as_view()),

    
]
