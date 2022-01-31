from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # to add custom fields in the future
    pass

# Many Lead has One Agent


class Lead(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    # every lead has an agent."Agent" means Agent class is in this file but doesn't follow topdown approach
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Agent(models.Model):
    # every agent has one user
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
