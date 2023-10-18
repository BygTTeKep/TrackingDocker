from django.db import models

# Create your models here.

class DockerUser(models.Model):
    Email = models.EmailField()
    UserName = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)