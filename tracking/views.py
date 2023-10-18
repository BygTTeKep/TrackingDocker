from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse, HttpResponse
import docker
import json
# from .tasks import status_container
import re
import time
from django.contrib import messages
from .forms import LoginForm
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


def login_docker(request:HttpRequest):
    # Добавить аутентификацию 
    # Пользователя в бд для токена
    '''
        Описать модель с полями 
        email
        username
        password
        и валидировать полученные данные из post запроса
    '''
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["Email"]
            username = form.cleaned_data["UserName"]
            password = form.cleaned_data["Password"]
            response = client.login(email=email, username=username, password=password)
            if response["Status"] == "Login Succeeded":
                return redirect("tracking:getContainers")
        # if HttpResponse.status_code == 401:
        #     return redirect("tracking:login")
        # print(response) => {'IdentityToken': '', 'Status': 'Login Succeeded'}
    else:
        form = LoginForm()
        return render(request, "tracking/login.html", {"form": form})

def create_container(request:HttpRequest): #<=====================================
    if request.method == "POST":
        image = request.POST.get("inputImage")
        commands = str(request.POST.get("textAreaCommand"))
        client.containers.create(image, command=commands)
        messages.success(request, "Created")
    else:
        return render(request, "tracking/createContainer.html", {"dockerVersion": client.version()["Version"],})
    return render(request, "tracking/createContainer.html", {"dockerVersion": client.version()["Version"],})

def init_docker_swarm(request:HttpRequest):
    #Добавить проверки на существование
    if request.method == "POST":
        command = request.POST.get("initDockerSwarm")
        client.swarm.init(command)
        return redirect("tracking:getContainers")
    else:
        return render(request, "tracking/initDockerSwarm.html", {"dockerVersion": client.version()["Version"],})
    # return render(request, "tracking/initDockerSwarm.html", {})


def leave_docker_swarm(request:HttpRequest):
    if docker.DockerClient.info(client)["Swarm"]["ControlAvailable"]:
        if docker.DockerClient.info(client)["Swarm"]["Managers"] == 1:
            client.swarm.leave(force=True)
        else: client.swarm.leave()
        messages.success(request, "Succes")
    else: messages.info(request, "Docker Swarm is not initialized")
    return redirect("tracking:getContainers")

#===============================================================================

def get_сontainers(request:HttpRequest):
    if client.ping():
        context = {
            "containers":client.containers.list(all=True),
            "dockerVersion": client.version()["Version"],
            # "statusContainer": status_container.delay()
        }
        return render(request, "tracking/home.html", context)
    else: ...

def get_images(request: HttpRequest):
    # print(decode_dict(client.images.list(all=True)[-1].attrs))
    context = {
        "images": client.images.list(all=True),
        "dockerVersion": client.version()["Version"],
    }
    return render(request, "tracking/allImages.html", context)

def get_networks(request:HttpRequest):
    context = {
        "networks": client.networks.list(),
        "dockerVersion": client.version()["Version"],
    }
    return render(request, "tracking/allNetworks.html", context)

def get_volumes(request:HttpRequest):
    context = {
        "volumes": client.volumes.list(),
        "dockerVersion": client.version()["Version"],
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
def get_nodes_json(request:HttpRequest):
    context = {}
    for i in range(0, len(client.nodes.list())):
        context[i] = decode_dict(client.nodes.list()[i].attrs)
    return JsonResponse(context)

def get_volumes_json(request:HttpRequest):
    context = {}
    for i in range(0, len(client.volumes.list())):
        context[i] = client.volumes.list()[i].attrs
    return JsonResponse(client.volumes.list().attrs)

#docker-swarm
def get_services_json(request:HttpRequest):
    context = {}
    for i in range(0, len(client.services.list())):
        context[i] = client.services.list()[i].attrs
    return JsonResponse(context)