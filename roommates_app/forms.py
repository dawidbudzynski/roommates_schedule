from django.forms import (Form, CharField, PasswordInput, ChoiceField)

from .models import (Roommate, Room)

all_roommates = Roommate.objects.all()
all_rooms = Room.objects.all()
COLOURS = {('red', 'red'), ('yellow', 'yellow'), ('orange', 'orange'),
           ('gray', 'gray'), ('green', 'green'), ('blue', 'blue'), ('white', 'white')}


class AddAccountForm(Form):
    name = CharField(label='Name', strip=True)
    password = CharField(label='Password', widget=PasswordInput)
    password2 = CharField(label='Password again', widget=PasswordInput)


class AddRoommateForm(Form):
    name = CharField(label='Name', strip=True)
    colour = ChoiceField(choices=COLOURS)


class AddRoomForm(Form):
    name = CharField(label='Name', strip=True)


class LoginForm(Form):
    username = CharField(label='Name', strip=True)
    password = CharField(label='Password', widget=PasswordInput)
