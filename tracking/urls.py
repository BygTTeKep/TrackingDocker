from django.urls import path, re_path

# from django.conf.urls import url
from .views import (
    get_сontainers,
    detail_containers,
    get_images,
    get_networks,
    get_volumes,
    detail_images,
    create_container,
    leave_docker_swarm,
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
    # path("api/containers", get_containers_json, name="getContainersApi"),
    # path("api/volumes", get_volumes_json, name="getVolumesApi"),
    # path("api/services", get_services_json, name="getServicesApi"),
    # path("api/images", get_image_json, name="getImagesApi"),
    path("networks", get_networks, name="getNetworks"),
    path("volumes", get_volumes, name="getVolumes"),
    path("create", create_container, name="create"),
    path("initSwarm", init_docker_swarm, name="initSwarm"),
    path("leaveSwarm", leave_docker_swarm, name="leaveSwarm"),
    path("login", login_docker, name="login"),
    path("api/containers", ContainerApi.as_view()),
    path("api/images", ImageApi.as_view()),
    path("api/networks", NetworkApi.as_view()),
    path("api/volumes", VolumesApi.as_view()),

    
]
