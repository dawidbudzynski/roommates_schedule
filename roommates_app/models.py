from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Apartment(models.Model):
    user = models.ForeignKey(User, on_delete=None)

    def __str__(self):
        return self.user.username


class Roommate(models.Model):
    name = models.CharField(max_length=64)
    apartment = models.ForeignKey(Apartment, on_delete=None, null=True)


class Room(models.Model):
    name = models.CharField(max_length=64)


class Cleaning(models.Model):
    roommate = models.ForeignKey(Roommate, on_delete=None)
    room = models.ForeignKey(Room, on_delete=None)
    date = models.DateField
