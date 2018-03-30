from django.forms import (Form, CharField, ModelChoiceField, PasswordInput)

from .models import Apartment

all_apartments = Apartment.objects.all()


class AddApartmentForm(Form):
    name = CharField(label='Name', strip=True)
    password = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Password again', widget=PasswordInput)


class AddRoommateForm(Form):
    name = CharField(label='Name', strip=True)
    apartment = ModelChoiceField(label = 'Apartment', queryset=all_apartments)


class AddRoomForm(Form):
    name = CharField(label='Name', strip=True)
    apartment = ModelChoiceField(label='Apartment', queryset=all_apartments)

class LoginForm(Form):
    username = CharField(label='Name', strip=True)
    password = CharField(label='Password', widget=PasswordInput)
