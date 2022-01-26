from importlib.machinery import SOURCE_SUFFIXES
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # to add custom fields in the future
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    # every lead has an agent
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)


class Agent(models.Model):
    # every agent has one user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
