
from django.urls import path
from .views import (
    get_сontainers,
    detail_containers,
    get_images,
    get_containers_json,
    get_image_json,
    get_networks,
)


app_name="tracking"
urlpatterns = [
    path("containers", get_сontainers, name="getContainers"),
    path("containers/<str:id>", detail_containers, name="detailContainers"),
    path("images", get_images, name="getImages"),
    path("api/containers", get_containers_json, name="getContainersApi"),
    path("api/images", get_image_json, name="getImagesApi"),
    path("networks", get_networks, name="getNetworks")
]
