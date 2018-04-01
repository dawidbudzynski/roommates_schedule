from django.contrib.auth.models import User
from django.db import models


class Roommate(models.Model):
    name = models.CharField(max_length=64)
    account = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    colour = models.CharField(max_length=32, null=True)


class Room(models.Model):
    name = models.CharField(max_length=64)
    account = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Cleaning(models.Model):
    roommate = models.ForeignKey(Roommate, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    index = models.IntegerField(null=True)
