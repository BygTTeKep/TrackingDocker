from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
import docker
import json
# from .tasks import status_container
import re
import time
# Create your views here.
client = docker.from_env()

# переписать 
def decode_dict(objectData:dict):
    objectFormat = str(objectData).replace("'", '"').replace("None", '"None"').replace("False", '"False"').replace("True", '"True"').replace('""False""', '"False"')
    print(objectFormat)
    # if re.search("CMD [\""+ r"[\w\.-]+"+ "\"]", objectFormat) == None:
    #     print( json.loads(objectFormat))
    # else:
    #     objectAttrs = re.sub("CMD [\""+ r"[\w\.-]+"+ "\"]", re.search("CMD [\""+ r"[\w\.-]+"+ "\"]",objectFormat).group().replace('"', "'"), objectFormat)
    #     print( json.loads(objectAttrs))


def create_container(request:HttpRequest): #<=====================================
    if request.method == "POST":
        image = request.POST.get("inputImage")
        commands = str(request.POST.get("textAreaCommand"))
        client.containers.create(image, command=commands)
    else:
        return render(request, "tracking/createContainer.html", {})
    return render(request, "tracking/createContainer.html", {})


def get_сontainers(request:HttpRequest):
    context = {
        "containers":client.containers.list(all=True),
        # "statusContainer": status_container.delay()
    }
    return render(request, "tracking/home.html", context)

def get_images(request: HttpRequest):
    # print(decode_dict(client.images.list(all=True)[-1].attrs))
    context = {
        "images": client.images.list(all=True),
    }
    return render(request, "tracking/allImages.html", context)

def get_networks(request:HttpRequest):
    context = {
        "networks": client.networks.list()
    }
    return render(request, "tracking/allNetworks.html", context)

def get_volumes(request:HttpRequest):
    context = {
        "volumes": client.volumes.list()
    }
    return render(request, "tracking/allVolumes.html", context)

#===============================================================================
def get_image_json(request:HttpRequest):
    context = {}
    for i in range(0, len(client.images.list(all=True))):
        context[i] = client.images.list(all=True)[i].attrs
    return JsonResponse(context)


def get_containers_json(request:HttpRequest):
    context = {}
    for i in range(0, len(client.containers.list(all=True))):
        context[i] = client.containers.list(all=True)[i].attrs
    return JsonResponse(context)


#===============================================================================

def detail_containers(request:HttpRequest, id:str):
    context = {
        "container": client.containers.get(id).attrs
    }
    return render(request, "tracking/detailContainers.html", context)

def detail_images(request:HttpRequest, id:str):
    context = {
        "images": client.images.get(id).attrs
    }
    return render(request, "tracking/detailImages.html", context)



#===============================================================================
# def get_nodes_json(request:HttpRequest):
#     context = {}
#     for i in range(0, len(client.nodes.list())):
#         context[i] = decode_dict(client.nodes.list()[i].attrs)
#     return JsonResponse(context)

def get_volumes_json(request:HttpRequest):
    context = {}
    for i in range(0, len(client.volumes.list())):
        context[i] = client.volumes.list()[i].attrs
    return JsonResponse(client.volumes.list().attrs)

#docker-swarm
# def get_services_json(request:HttpRequest):
#     context = {}
#     for i in range(0, len(client.services.list())):
#         context[i] = client.services.list()[i].attrs
#     return JsonResponse(context)