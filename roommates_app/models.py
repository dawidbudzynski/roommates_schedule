from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Apartment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.user.username


class Roommate(models.Model):
    name = models.CharField(max_length=64)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True)


class Room(models.Model):
    name = models.CharField(max_length=64)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE, null=True)


class Cleaning(models.Model):
    roommate = models.ForeignKey(Roommate, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=None)
    date = models.DateField
