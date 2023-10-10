from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
import docker
import json
from .tasks import status_container
import re
import time
# Create your views here.
client = docker.from_env()

# переписать 
def decode_dict(objectIndex: int, objectName:str) -> str:
    objectFormat = str(client.objectName.list(all=True)[objectIndex].attrs).replace("'", '"').replace("None", '"None"').replace("False", '"False"').replace("True", '"True"').replace('""False""', '"False"')
    # print(re.search("CMD [\""+ r"[\w\.-]+"+ "\"]",str(client.objectName.list(all=True)[objectIndex].attrs).replace("'", '"').replace("None", '"None"').replace("False", '"False"').replace("True", '"True"').replace('""False""', '"False"')))
    if re.search("CMD [\""+ r"[\w\.-]+"+ "\"]", objectFormat) == None:
        return json.loads(objectFormat)
    else:
        objectAttrs = re.sub("CMD [\""+ r"[\w\.-]+"+ "\"]", re.search("CMD [\""+ r"[\w\.-]+"+ "\"]",objectFormat).group().replace('"', "'"), objectFormat)
        return json.loads(objectAttrs)


def get_сontainers(request:HttpRequest):
    context = {
        "containers":client.containers.list(all=True),
        "statusContainer": status_container.delay()
    }
    return render(request, "tracking/allContainers.html", context)

def get_containers_json(request:HttpRequest):
    context = {}
    objectName = "containers"
    for i in range(0, len(client.containers.list(all=True))):
        # context[i] = json.loads(str(client.containers.list(all=True)[i].attrs).replace("'", '"').replace("None", '"None"').replace("False", '"False"').replace("True", '"True"').replace('""False""', '"False"'))
        context[i] = decode_dict(i, client.containers)
    return JsonResponse(context)

def get_images(request: HttpRequest):
    context = {
        "images": client.images.list(all=True)
    }
    return render(request, "tracking/allImages.html", context)

def get_image_json(request:HttpRequest):
    context = {}
    objectName = "images"
    print(len(client.images.list(all=True)))
    # time.sleep(100)
    for i in range(0, len(client.images.list(all=True))):
        print(i)
        context[i] = decode_dict(i, objectName)
    return JsonResponse(context)

def detail_containers(request:HttpRequest, id:str):
    context = {
        "container": client.containers.get(id).attrs
    }
    return render(request, "tracking/detailContainers.html", context)

def get_networks(request:HttpRequest):
    print(client.networks.list()[0].attrs)
    context = {
        "networks": client.networks.list()
    }
    time.sleep(100)
    return render(request, "tracking/allNetworks.html", context)